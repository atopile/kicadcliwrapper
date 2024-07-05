# This file is part of the faebryk project
# SPDX-License-Identifier: MIT


import re
from dataclasses import dataclass


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
