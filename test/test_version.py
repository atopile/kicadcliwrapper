# This file is part of the faebryk project
# SPDX-License-Identifier: MIT_

import subprocess

from kicadcliwrapper.generated.kicad_cli import kicad_cli


def test_version():
    version = kicad_cli(kicad_cli.version()).exec()
    assert version == subprocess.check_output(["kicad-cli", "version"]).decode()


def test_version_advanced():
    version_id = kicad_cli(kicad_cli.version(format="about")).exec()
    assert (
        version_id
        == subprocess.check_output(
            ["kicad-cli", "version", "--format", "about"]
        ).decode()
    )
