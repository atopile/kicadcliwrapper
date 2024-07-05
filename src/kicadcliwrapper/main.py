# This file is part of the faebryk project
# SPDX-License-Identifier: MIT


import logging
import re
import subprocess
from pathlib import Path
from textwrap import indent

import black
import typer
from kicadcliwrapper.lib import (
    ParserL1,
    ParserL2,
    sanitize_flag_arg_name,
    sanitize_name,
)

logger = logging.getLogger(__name__)


def run_command(chain: list[str]) -> str:
    result = subprocess.run(chain, capture_output=True, text=True)
    return result.stdout


def _split_strip(s: str, sep: str, max_split: int = -1) -> list[str]:
    return [ss.strip() for ss in s.split(sep, max_split)]


def parse_l1_command(chain: list[str]) -> ParserL1.Command:
    chain = chain or []
    print(chain)

    output = run_command(chain + ["--help"])
    sections = output.split("\n\n")

    csections = []
    subcommands = []
    for section in sections:
        lines = [ls for li in section.strip().split("\n") if (ls := li.strip())]
        # filter cli bugs
        lines = [li for li in lines if not li.startswith("input: ")]
        section_header = lines[0].split(":")
        section_name = section_header[0]
        csections.append(
            ParserL1.Section(
                section_name,
                lines,
            )
        )
        if section_name == "Subcommands":
            for line in lines[1:]:
                subcmd = line.split()[0]
                sub = parse_l1_command(chain + [subcmd])
                subcommands.append(sub)

    return ParserL1.Command(
        command=chain[-1],
        sections=csections,
        subcommands=subcommands,
    )


def parse_l2_command(l1_command: ParserL1.Command) -> ParserL2.Command:
    sections = {s.name: s for s in l1_command.sections}

    args = []
    flags = []

    usage = next(line for line in sections["Usage"].lines if line.startswith("Usage: "))
    param_str = re.findall(r"\[([^\]]+)\]", usage)
    params = {(s := p.split(" "))[0]: s[1] if len(s) > 1 else None for p in param_str}

    if "Positional arguments" in sections:
        for line in sections["Positional arguments"].lines[1:]:
            arg, desc = _split_strip(line, " ", 1)
            args.append(
                ParserL2.Argument(
                    name=arg, description=desc, arg_description=arg, required=True
                )
            )

    if "Optional arguments" in sections:
        for line in sections["Optional arguments"].lines[1:]:
            if not line.startswith("-"):
                logger.warning(f"Skipping line: {line}")
                continue
            args_str, desc = _split_strip(line, "  ", 1)
            args_variants = _split_strip(args_str, ",")
            name = args_variants[-1]
            if (argdesc := params.get(name)) is not None:
                args.append(
                    ParserL2.Argument(
                        name=name,
                        description=desc,
                        arg_description=argdesc,
                        required=False,
                    )
                )
            else:
                flags.append(
                    ParserL2.Flag(
                        name=name,
                        commands=args_variants,
                        description=desc,
                        default=False,
                    )
                )

    subcommands = [parse_l2_command(sub) for sub in l1_command.subcommands]
    description = l1_command.sections[1].name if len(l1_command.sections) > 3 else ""

    return ParserL2.Command(
        name=l1_command.command,
        description=description,
        args=args,
        flags=flags,
        subcommands=subcommands,
    )


def parse_l3_command(l2_command: ParserL2.Command) -> str:
    def sanitize_string(s: str) -> str:
        return s.replace('"""', '" " "')

    def _sanitize_flag_arg_name(name: str) -> str:
        return sanitize_flag_arg_name(name, l2_command)

    out = ""

    out += "@dataclass\n"
    out += f"class {sanitize_name(l2_command.name)}:\n"

    out += '    """\n'
    out += "    Args:\n"
    for flag_arg in l2_command.args + l2_command.flags:
        out += f"        {_sanitize_flag_arg_name(flag_arg.name)}: {sanitize_string(flag_arg.description)}\n"  # noqa: E501
    out += '    """\n'

    if l2_command.subcommands:
        out += f"    cmd : '{' | '.join([sanitize_name(c.name) for c in l2_command.subcommands])}'\n"  # noqa: E501

    out += "    # Arguments (Required)\n"
    for arg in l2_command.args:
        if not arg.required:
            continue
        out += f"    {_sanitize_flag_arg_name(arg.name)}: str\n"

    out += "    # Arguments (Optional)\n"
    for arg in l2_command.args:
        if arg.required:
            continue
        out += f"    {_sanitize_flag_arg_name(arg.name)}: str | None = None\n"

    out += "    # Flags\n"
    for flag in l2_command.flags:
        out += f"    {_sanitize_flag_arg_name(flag.name)}: bool = False\n"

    if l2_command.subcommands:
        out += "    # Commands\n"
    for sub in l2_command.subcommands:
        out += indent(parse_l3_command(sub), prefix="    ")

    return out


def main(out_dir: Path = Path(__file__).parent / Path("generated")):
    out_l1 = out_dir / Path("kicad_cli_l1.py")
    out_l2 = out_dir / Path("kicad_cli_l2.py")
    out = out_dir / Path("kicad_cli.py")

    logger.info(f"Parsing L1 {'-'*20}")
    l1 = parse_l1_command(["kicad-cli"])

    header_license = "# This file is part of the faebryk project\n# SPDX-License-Identifier: MIT\n\n\n"  # noqa: E501

    header_l1 = header_license + "from kicadcliwrapper.lib import ParserL1\n"
    l1_formatted = black.format_str(repr(l1), mode=black.FileMode())
    out_l1.write_text(header_l1 + "\n" + l1_formatted)

    logger.info(f"Parsing L2 {'-'*20}")
    l2 = parse_l2_command(l1)

    header_l2 = header_license + "from kicadcliwrapper.lib import ParserL2\n"
    l2_formatted = black.format_str("kicad_cli_l2=" + repr(l2), mode=black.FileMode())
    out_l2.write_text(header_l2 + "\n" + l2_formatted)

    logger.info(f"Parsing L3 {'-'*20}")
    l3 = parse_l3_command(l2)
    header_l3 = header_license + (
        "from dataclasses import dataclass\n"
        + "from subprocess import check_output\n"
        + "\n"
        + "from kicadcliwrapper.generated.kicad_cli_l2 import kicad_cli_l2\n"
        + "from kicadcliwrapper.lib import make_command\n"
    )
    trailer_l3 = (
        "    def exec(self):\n"
        + "        return check_output(make_command(kicad_cli_l2, self))\n"
    )
    out.write_text(
        black.format_str(
            header_l3 + "\n\n" + l3 + "\n" + trailer_l3, mode=black.FileMode()
        )
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    typer.run(main)
