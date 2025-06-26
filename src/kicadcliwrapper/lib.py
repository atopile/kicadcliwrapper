# This file is part of the faebryk project
# SPDX-License-Identifier: MIT


import logging
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from subprocess import check_output

logger = logging.getLogger(__name__)


class ParserL1:
    @dataclass
    class Section:
        name: str
        lines: list[str]

    @dataclass
    class Command:
        command: str
        sections: list["ParserL1.Section"]
        subcommands: list["ParserL1.Command"]


class ParserL2:
    @dataclass
    class Argument:
        name: str
        description: str
        arg_description: str
        required: bool

    @dataclass
    class Flag:
        name: str
        commands: list[str]
        description: str
        default: bool

    @dataclass
    class Command:
        name: str
        description: str
        args: list["ParserL2.Argument"]
        flags: list["ParserL2.Flag"]
        subcommands: list["ParserL2.Command"]


def sanitize_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]", "_", name)


def sanitize_flag_arg_name(name: str, l2_command: ParserL2.Command) -> str:
    out = sanitize_name(name.removeprefix("--").removeprefix("-"))
    if out in [cmd.name for cmd in l2_command.subcommands]:
        return f"a_{out}"
    return out


def make_command(l2_root: ParserL2.Command, cmd) -> list[str]:
    out = []

    cmd_name = type(cmd).__name__
    assert sanitize_name(l2_root.name) == cmd_name

    out.append(l2_root.name)

    for flag in l2_root.flags:
        if getattr(cmd, sanitize_flag_arg_name(flag.name, l2_root)):
            out.append(flag.name)

    for arg in l2_root.args:
        if arg.required:
            out.append(getattr(cmd, sanitize_flag_arg_name(arg.name, l2_root)))
        else:
            if val := getattr(cmd, sanitize_flag_arg_name(arg.name, l2_root)):
                out.append(arg.name)
                out.append(val)

    if l2_root.subcommands:
        subcmd = getattr(cmd, "cmd")
        subcmd_name = type(subcmd).__name__
        subcmdl2 = next(
            sub for sub in l2_root.subcommands if sanitize_name(sub.name) == subcmd_name
        )

        sub = make_command(subcmdl2, subcmd)
        out.extend(sub)

    return out


def find_kicad_cli() -> Path:
    """Figure out what to call for the pcbnew CLI."""

    def check(cmd) -> bool:
        try:
            version = check_output([cmd, "--version"]).decode("utf-8")
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.debug("Missed kicad-cli at %s", cmd)
            return False
        else:
            logger.debug("Found kicad-cli version: %s", version)
            return True

    if check("kicad-cli"):
        return Path("kicad-cli")

    if sys.platform.startswith("darwin"):
        base = Path("/Applications/KiCad/")
    elif sys.platform.startswith("win"):
        base = Path(os.getenv("ProgramFiles")) / "KiCad"
    else:
        raise NotImplementedError(f"Unsupported platform: {sys.platform}")

    bin_name = "kicad-cli"
    if sys.platform.startswith("win"):
        bin_name += ".exe"

    for cmd in base.glob(f"**/{bin_name}"):
        if check(cmd):
            return cmd

    raise FileNotFoundError("Could not find kicad-cli executable")


def run_command(command: list[str], check=False) -> str:
    assert command
    cli_path = find_kicad_cli()
    assert cli_path.name.replace(".exe", "") == command[0]
    logger.debug("Running command: %s", " ".join(command))

    result = subprocess.run([cli_path] + command[1:], capture_output=True, text=True)

    logger.debug("Command return code: %s", result.returncode)
    logger.debug("Command stdout: %s", result.stdout)
    logger.debug("Command stderr: %s", result.stderr)

    stdout = result.stdout
    if result.returncode != 0:
        # workaround: Some help commands return an error when no arguments are provided
        pattern = r"input: [0-9]+ argument\(s\) expected. 0 provided.\n"
        if "--help" in command and re.match(pattern, stdout):
            stdout = re.sub(pattern, "", stdout)
        else:
            raise subprocess.CalledProcessError(
                result.returncode, command, result.stdout, result.stderr
            )

    return stdout


def run_parser_command(l2_root: ParserL2.Command, cmd, check=False) -> str:
    command = make_command(l2_root, cmd)
    return run_command(command, check)
