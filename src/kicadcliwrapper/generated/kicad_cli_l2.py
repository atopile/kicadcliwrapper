# This file is part of the faebryk project
# SPDX-License-Identifier: MIT


from kicadcliwrapper.lib import ParserL2

kicad_cli_l2 = ParserL2.Command(
    name="kicad-cli",
    description="",
    args=[],
    flags=[
        ParserL2.Flag(
            name="--version",
            commands=["-v", "--version"],
            description="prints version information and exits",
            default=False,
        ),
        ParserL2.Flag(
            name="--help",
            commands=["-h", "--help"],
            description="Shows help message and exits",
            default=False,
        ),
    ],
    subcommands=[
        ParserL2.Command(
            name="fp",
            description="Footprint and Footprint Libraries",
            args=[],
            flags=[
                ParserL2.Flag(
                    name="--help",
                    commands=["-h", "--help"],
                    description="Shows help message and exits",
                    default=False,
                )
            ],
            subcommands=[
                ParserL2.Command(
                    name="export",
                    description="Export utilities (svg)",
                    args=[],
                    flags=[
                        ParserL2.Flag(
                            name="--help",
                            commands=["-h", "--help"],
                            description="Shows help message and exits",
                            default=False,
                        )
                    ],
                    subcommands=[
                        ParserL2.Command(
                            name="svg",
                            description="Exports the footprint or entire footprint library to SVG",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_DIR",
                                    description="Input directory",
                                    arg_description="INPUT_DIR",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output directory [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_DIR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--layers",
                                    description='Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                    arg_description="LAYER_LIST",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--theme",
                                    description='Color theme to use (will default to footprint editor settings) [nargs=0..1] [default: ""]',
                                    arg_description="VAR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--footprint",
                                    description='Specific footprint to export within the library [nargs=0..1] [default: ""]',
                                    arg_description="FOOTPRINT_NAME",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--black-and-white",
                                    commands=["--black-and-white"],
                                    description="Black and white only",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        )
                    ],
                ),
                ParserL2.Command(
                    name="upgrade",
                    description="Upgrades the footprint library to the current kicad version format",
                    args=[
                        ParserL2.Argument(
                            name="INPUT_DIR",
                            description="Input directory",
                            arg_description="INPUT_DIR",
                            required=True,
                        ),
                        ParserL2.Argument(
                            name="--output",
                            description='Output directory [nargs=0..1] [default: ""]',
                            arg_description="OUTPUT_DIR",
                            required=False,
                        ),
                    ],
                    flags=[
                        ParserL2.Flag(
                            name="--help",
                            commands=["-h", "--help"],
                            description="Shows help message and exits",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--force",
                            commands=["--force"],
                            description="Forces the footprint library to be resaved regardless of versioning",
                            default=False,
                        ),
                    ],
                    subcommands=[],
                ),
            ],
        ),
        ParserL2.Command(
            name="pcb",
            description="PCB",
            args=[],
            flags=[
                ParserL2.Flag(
                    name="--help",
                    commands=["-h", "--help"],
                    description="Shows help message and exits",
                    default=False,
                )
            ],
            subcommands=[
                ParserL2.Command(
                    name="drc",
                    description="Runs the Design Rules Check (DRC) on the PCB and creates a report",
                    args=[
                        ParserL2.Argument(
                            name="INPUT_FILE",
                            description="Input file",
                            arg_description="INPUT_FILE",
                            required=True,
                        ),
                        ParserL2.Argument(
                            name="--output",
                            description='Output file [nargs=0..1] [default: ""]',
                            arg_description="OUTPUT_FILE",
                            required=False,
                        ),
                        ParserL2.Argument(
                            name="--define-var",
                            description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                            arg_description="KEY=VALUE",
                            required=False,
                        ),
                        ParserL2.Argument(
                            name="--format",
                            description='Output file format, options: json, report [nargs=0..1] [default: "report"]',
                            arg_description="FORMAT",
                            required=False,
                        ),
                        ParserL2.Argument(
                            name="--units",
                            description='Report units; valid options: in, mm, mils [nargs=0..1] [default: "mm"]',
                            arg_description="UNITS",
                            required=False,
                        ),
                    ],
                    flags=[
                        ParserL2.Flag(
                            name="--help",
                            commands=["-h", "--help"],
                            description="Shows help message and exits",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--all-track-errors",
                            commands=["--all-track-errors"],
                            description="Report all errors for each track",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--schematic-parity",
                            commands=["--schematic-parity"],
                            description="Test for parity between PCB and schematic",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--severity-all",
                            commands=["--severity-all"],
                            description="Report all DRC violations, this is equivalent to including all the other severity arguments",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--severity-error",
                            commands=["--severity-error"],
                            description="Report all DRC error level violations, this can be combined with the other severity arguments",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--severity-warning",
                            commands=["--severity-warning"],
                            description="Report all DRC warning level violations, this can be combined with the other severity arguments",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--severity-exclusions",
                            commands=["--severity-exclusions"],
                            description="Report all excluded DRC violations, this can be combined with the other severity arguments",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--exit-code-violations",
                            commands=["--exit-code-violations"],
                            description="Return a nonzero exit code if DRC violations exist",
                            default=False,
                        ),
                    ],
                    subcommands=[],
                ),
                ParserL2.Command(
                    name="export",
                    description="Export utilities (Gerbers, drill, position files, etc)",
                    args=[],
                    flags=[
                        ParserL2.Flag(
                            name="--help",
                            commands=["-h", "--help"],
                            description="Shows help message and exits",
                            default=False,
                        )
                    ],
                    subcommands=[
                        ParserL2.Command(
                            name="drill",
                            description="Generate Drill Files",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output directory [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_DIR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--format",
                                    description='Valid options excellon, gerber. [nargs=0..1] [default: "excellon"]',
                                    arg_description="FORMAT",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drill-origin",
                                    description='Valid options are: absolute,plot [nargs=0..1] [default: "absolute"]',
                                    arg_description="DRILL_ORIGIN",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--excellon-zeros-format",
                                    description='Valid options are: decimal,suppressleading,suppresstrailing,keep. [nargs=0..1] [default: "decimal"]',
                                    arg_description="ZEROS_FORMAT",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--excellon-oval-format",
                                    description='Valid options are: route,alternate. [nargs=0..1] [default: "alternate"]',
                                    arg_description="OVAL_FORMAT",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--excellon-units",
                                    description='Output units, valid options:in,mm [nargs=0..1] [default: "mm"]',
                                    arg_description="UNITS",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--map-format",
                                    description='Valid options: pdf,gerberx2,ps,dxf,svg [nargs=0..1] [default: "pdf"]',
                                    arg_description="MAP_FORMAT",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--gerber-precision",
                                    description="Precision of Gerber coordinates (5 or 6) [nargs=0..1] [default: 6]",
                                    arg_description="VAR",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--excellon-mirror-y",
                                    commands=["--excellon-mirror-y"],
                                    description="Mirror Y axis",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--excellon-min-header",
                                    commands=["--excellon-min-header"],
                                    description="Minimal header",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--excellon-separate-th",
                                    commands=["--excellon-separate-th"],
                                    description="Generate independent files for NPTH and PTH holes",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--generate-map",
                                    commands=["--generate-map"],
                                    description="Generate map / summary of drill hits",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="dxf",
                            description="Generate a DXF from a list of layers",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--layers",
                                    description='Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                    arg_description="LAYER_LIST",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--output-units",
                                    description='Output units, valid options: mm, in [nargs=0..1] [default: "in"]',
                                    arg_description="UNITS",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-refdes",
                                    commands=["--erd", "--exclude-refdes"],
                                    description="Exclude the reference designator text",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-value",
                                    commands=["--ev", "--exclude-value"],
                                    description="Exclude the value text",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--use-contours",
                                    commands=["--uc", "--use-contours"],
                                    description="Plot graphic items using their contours",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-border-title",
                                    commands=["--ibt", "--include-border-title"],
                                    description="Include the border and title block",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="gerber",
                            description="Plot given layers to a single Gerber file",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--layers",
                                    description='Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                    arg_description="LAYER_LIST",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--precision",
                                    description="Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]",
                                    arg_description="PRECISION",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-refdes",
                                    commands=["--erd", "--exclude-refdes"],
                                    description="Exclude the reference designator text",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-value",
                                    commands=["--ev", "--exclude-value"],
                                    description="Exclude the value text",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-border-title",
                                    commands=["--ibt", "--include-border-title"],
                                    description="Include the border and title block",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-x2",
                                    commands=["--no-x2"],
                                    description="Do not use the extended X2 format",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-netlist",
                                    commands=["--no-netlist"],
                                    description="Do not generate netlist attributes",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--subtract-soldermask",
                                    commands=["--subtract-soldermask"],
                                    description="Subtract soldermask from silkscreen",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--disable-aperture-macros",
                                    commands=["--disable-aperture-macros"],
                                    description="Disable aperture macros",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--use-drill-file-origin",
                                    commands=["--use-drill-file-origin"],
                                    description="Use drill/place file origin",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-protel-ext",
                                    commands=["--no-protel-ext"],
                                    description="Use KiCad Gerber file extension",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="gerbers",
                            description="Plot multiple Gerbers for a PCB, including the ability to use stored board plot settings",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--layers",
                                    description='Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                    arg_description="LAYER_LIST",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--precision",
                                    description="Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]",
                                    arg_description="PRECISION",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--common-layers",
                                    description='Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                    arg_description="COMMON_LAYER_LIST",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-refdes",
                                    commands=["--erd", "--exclude-refdes"],
                                    description="Exclude the reference designator text",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-value",
                                    commands=["--ev", "--exclude-value"],
                                    description="Exclude the value text",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-border-title",
                                    commands=["--ibt", "--include-border-title"],
                                    description="Include the border and title block",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-x2",
                                    commands=["--no-x2"],
                                    description="Do not use the extended X2 format",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-netlist",
                                    commands=["--no-netlist"],
                                    description="Do not generate netlist attributes",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--subtract-soldermask",
                                    commands=["--subtract-soldermask"],
                                    description="Subtract soldermask from silkscreen",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--disable-aperture-macros",
                                    commands=["--disable-aperture-macros"],
                                    description="Disable aperture macros",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--use-drill-file-origin",
                                    commands=["--use-drill-file-origin"],
                                    description="Use drill/place file origin",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-protel-ext",
                                    commands=["--no-protel-ext"],
                                    description="Use KiCad Gerber file extension",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--board-plot-params",
                                    commands=["--board-plot-params"],
                                    description="Use the Gerber plot settings already configured in the board file",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="glb",
                            description="Export GLB (binary GLTF)",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--min-distance",
                                    description='Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]',
                                    arg_description="MIN_DIST",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--user-origin",
                                    description='User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                    arg_description="VAR",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--force",
                                    commands=["-f", "--force"],
                                    description="Overwrite output file",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--grid-origin",
                                    commands=["--grid-origin"],
                                    description="Use Grid Origin for output origin",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--drill-origin",
                                    commands=["--drill-origin"],
                                    description="Use Drill Origin for output origin",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-unspecified",
                                    commands=["--no-unspecified"],
                                    description="Exclude 3D models for components with 'Unspecified' footprint type",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-dnp",
                                    commands=["--no-dnp"],
                                    description="Exclude 3D models for components with 'Do not populate' attribute",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--subst-models",
                                    commands=["--subst-models"],
                                    description="Substitute STEP or IGS models with the same name in place of VRML models",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--board-only",
                                    commands=["--board-only"],
                                    description="Only generate a board with no components",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-tracks",
                                    commands=["--include-tracks"],
                                    description="Export tracks",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-zones",
                                    commands=["--include-zones"],
                                    description="Export zones",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="ipc2581",
                            description="Export the PCB in IPC2581 format",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--precision",
                                    description="Precision [nargs=0..1] [default: 3]",
                                    arg_description="PRECISION",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--version",
                                    description='IPC2581 standard version [nargs=0..1] [default: "C"]',
                                    arg_description="VAR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--units",
                                    description='Units [nargs=0..1] [default: "mm"]',
                                    arg_description="VAR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--bom-col-int-id",
                                    description='Name of the part field to use for the Bill of Material Internal Id Column [nargs=0..1] [default: ""]',
                                    arg_description="FIELD_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--bom-col-mfg-pn",
                                    description='Name of the part field to use for the Bill of Material Manufacturer Part Number Column [nargs=0..1] [default: ""]',
                                    arg_description="FIELD_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--bom-col-mfg",
                                    description='Name of the part field to use for the Bill of Material Manufacturer Column [nargs=0..1] [default: ""]',
                                    arg_description="FIELD_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--bom-col-dist-pn",
                                    description='Name of the part field to use for the Bill of Material Distributor Part Number Column [nargs=0..1] [default: ""]',
                                    arg_description="FIELD_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--bom-col-dist",
                                    description='Name to insert into Bill of Material Distributor Column [nargs=0..1] [default: ""]',
                                    arg_description="FIELD_NAME",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--compress",
                                    commands=["--compress"],
                                    description="Compress the output",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="pdf",
                            description="Generate PDF from a list of layers",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--layers",
                                    description='Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                    arg_description="LAYER_LIST",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--theme",
                                    description='Color theme to use (will default to PCB Editor settings) [nargs=0..1] [default: ""]',
                                    arg_description="THEME_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drill-shape-opt",
                                    description="Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]",
                                    arg_description="VAR",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--mirror",
                                    commands=["-m", "--mirror"],
                                    description="Mirror the board (useful for trying to show bottom layers)",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-refdes",
                                    commands=["--erd", "--exclude-refdes"],
                                    description="Exclude the reference designator text",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-value",
                                    commands=["--ev", "--exclude-value"],
                                    description="Exclude the value text",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-border-title",
                                    commands=["--ibt", "--include-border-title"],
                                    description="Include the border and title block",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--negative",
                                    commands=["-n", "--negative"],
                                    description="Plot as negative (useful for directly etching from the export)",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--black-and-white",
                                    commands=["--black-and-white"],
                                    description="Black and white only",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="pos",
                            description="Generate Position File",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--side",
                                    description='Valid options: front,back,both. Gerber format only supports "both". [nargs=0..1] [default: "both"]',
                                    arg_description="VAR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--format",
                                    description='Valid options: ascii,csv,gerber [nargs=0..1] [default: "ascii"]',
                                    arg_description="FORMAT",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--units",
                                    description='Output units; ascii or csv format only; valid options: in,mm [nargs=0..1] [default: "in"]',
                                    arg_description="UNITS",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--bottom-negate-x",
                                    commands=["--bottom-negate-x"],
                                    description="Use negative X coordinates for footprints on bottom layer (ascii or csv formats only)",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--use-drill-file-origin",
                                    commands=["--use-drill-file-origin"],
                                    description="Use drill/place file origin (ascii or csv only)",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--smd-only",
                                    commands=["--smd-only"],
                                    description="Include only SMD footprints (ascii or csv only)",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-fp-th",
                                    commands=["--exclude-fp-th"],
                                    description="Exclude all footprints with through-hole pads (ascii or csv only)",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-dnp",
                                    commands=["--exclude-dnp"],
                                    description="Exclude all footprints with the Do Not Populate flag set",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--gerber-board-edge",
                                    commands=["--gerber-board-edge"],
                                    description="Include board edge layer (Gerber only)",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="step",
                            description="Export STEP",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--min-distance",
                                    description='Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]',
                                    arg_description="MIN_DIST",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--user-origin",
                                    description='User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                    arg_description="VAR",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--force",
                                    commands=["-f", "--force"],
                                    description="Overwrite output file",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--grid-origin",
                                    commands=["--grid-origin"],
                                    description="Use Grid Origin for output origin",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--drill-origin",
                                    commands=["--drill-origin"],
                                    description="Use Drill Origin for output origin",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-unspecified",
                                    commands=["--no-unspecified"],
                                    description="Exclude 3D models for components with 'Unspecified' footprint type",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-dnp",
                                    commands=["--no-dnp"],
                                    description="Exclude 3D models for components with 'Do not populate' attribute",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--subst-models",
                                    commands=["--subst-models"],
                                    description="Substitute STEP or IGS models with the same name in place of VRML models",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--board-only",
                                    commands=["--board-only"],
                                    description="Only generate a board with no components",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-tracks",
                                    commands=["--include-tracks"],
                                    description="Export tracks",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-zones",
                                    commands=["--include-zones"],
                                    description="Export zones",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-optimize-step",
                                    commands=["--no-optimize-step"],
                                    description="Do not optimize STEP file (enables writing parametric curves)",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="svg",
                            description="Generate SVG outputs of a given layer list",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--layers",
                                    description='Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                    arg_description="LAYER_LIST",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--theme",
                                    description='Color theme to use (will default to PCB editor settings) [nargs=0..1] [default: ""]',
                                    arg_description="THEME_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--page-size-mode",
                                    description="Set page sizing mode (0 = page with frame and title block, 1 = current page size, 2 = board area only) [nargs=0..1] [default: 0]",
                                    arg_description="MODE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drill-shape-opt",
                                    description="Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]",
                                    arg_description="SHAPE_OPTION",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--mirror",
                                    commands=["-m", "--mirror"],
                                    description="Mirror the board (useful for trying to show bottom layers)",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--negative",
                                    commands=["-n", "--negative"],
                                    description="Plot as negative (useful for directly etching from the export)",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--black-and-white",
                                    commands=["--black-and-white"],
                                    description="Black and white only",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-drawing-sheet",
                                    commands=["--exclude-drawing-sheet"],
                                    description="No drawing sheet",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="vrml",
                            description="Export VRML",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--user-origin",
                                    description='User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                    arg_description="VAR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--units",
                                    description='Output units; valid options: mm, m, in, tenths [nargs=0..1] [default: "in"]',
                                    arg_description="VAR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--models-dir",
                                    description='Name of folder to create and store 3d models in, if not specified or empty, the models will be embedded in main exported VRML file [nargs=0..1] [default: ""]',
                                    arg_description="VAR",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--force",
                                    commands=["-f", "--force"],
                                    description="Overwrite output file",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--models-relative",
                                    commands=["--models-relative"],
                                    description="Used with --models-dir to output relative paths in the resulting file",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                    ],
                ),
            ],
        ),
        ParserL2.Command(
            name="sch",
            description="Schematics",
            args=[],
            flags=[
                ParserL2.Flag(
                    name="--help",
                    commands=["-h", "--help"],
                    description="Shows help message and exits",
                    default=False,
                )
            ],
            subcommands=[
                ParserL2.Command(
                    name="erc",
                    description="Runs the Electrical Rules Check (ERC) on the schematic and creates a report",
                    args=[
                        ParserL2.Argument(
                            name="INPUT_FILE",
                            description="Input file",
                            arg_description="INPUT_FILE",
                            required=True,
                        ),
                        ParserL2.Argument(
                            name="--output",
                            description='Output file [nargs=0..1] [default: ""]',
                            arg_description="OUTPUT_FILE",
                            required=False,
                        ),
                        ParserL2.Argument(
                            name="--define-var",
                            description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                            arg_description="KEY=VALUE",
                            required=False,
                        ),
                        ParserL2.Argument(
                            name="--format",
                            description='Output file format, options: json, report [nargs=0..1] [default: "report"]',
                            arg_description="VAR",
                            required=False,
                        ),
                        ParserL2.Argument(
                            name="--units",
                            description='Report units; valid options: in, mm, mils [nargs=0..1] [default: "mm"]',
                            arg_description="VAR",
                            required=False,
                        ),
                    ],
                    flags=[
                        ParserL2.Flag(
                            name="--help",
                            commands=["-h", "--help"],
                            description="Shows help message and exits",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--severity-all",
                            commands=["--severity-all"],
                            description="Report all ERC violations, this is equivalent to including all the other severity arguments",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--severity-error",
                            commands=["--severity-error"],
                            description="Report all ERC error level violations, this can be combined with the other severity arguments",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--severity-warning",
                            commands=["--severity-warning"],
                            description="Report all ERC warning level violations, this can be combined with the other severity arguments",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--severity-exclusions",
                            commands=["--severity-exclusions"],
                            description="Report all excluded ERC violations, this can be combined with the other severity arguments",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--exit-code-violations",
                            commands=["--exit-code-violations"],
                            description="Return a nonzero exit code if ERC violations exist",
                            default=False,
                        ),
                    ],
                    subcommands=[],
                ),
                ParserL2.Command(
                    name="export",
                    description="Export utilities (netlist, pdf, bom, etc)",
                    args=[],
                    flags=[
                        ParserL2.Flag(
                            name="--help",
                            commands=["-h", "--help"],
                            description="Shows help message and exits",
                            default=False,
                        )
                    ],
                    subcommands=[
                        ParserL2.Command(
                            name="bom",
                            description="Generate a Bill of Materials (BOM)",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--preset",
                                    description='Use a named BOM preset setting from the schematic, e.g. "Grouped By Value". [nargs=0..1] [default: ""]',
                                    arg_description="PRESET",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--format-preset",
                                    description='Use a named BOM format preset setting from the schematic, e.g. CSV. [nargs=0..1] [default: ""]',
                                    arg_description="FMT_PRESET",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--fields",
                                    description='An ordered list of fields to export. See documentation for special substitutions. [nargs=0..1] [default: "Reference,Value,Footprint,${QUANTITY},${DNP}"]',
                                    arg_description="FIELDS",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--labels",
                                    description='An ordered list of labels to apply the exported fields. [nargs=0..1] [default: "Refs,Value,Footprint,Qty,DNP"]',
                                    arg_description="LABELS",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--group-by",
                                    description='Fields to group references by when field values match. [nargs=0..1] [default: ""]',
                                    arg_description="GROUP_BY",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--sort-field",
                                    description='Field name to sort by. [nargs=0..1] [default: "Reference"]',
                                    arg_description="SORT_BY",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--filter",
                                    description='Filter string to remove output lines. [nargs=0..1] [default: ""]',
                                    arg_description="FILTER",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--field-delimiter",
                                    description='Separator between output fields/columns. [nargs=0..1] [default: ","]',
                                    arg_description="FIELD_DELIM",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--string-delimiter",
                                    description='Character to surround fields with. [nargs=0..1] [default: """]',
                                    arg_description="STR_DELIM",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--ref-delimiter",
                                    description='Character to place between individual references. [nargs=0..1] [default: ","]',
                                    arg_description="REF_DELIM",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--ref-range-delimiter",
                                    description='Character to place in ranges of references. Leave blank for no ranges. [nargs=0..1] [default: "-"]',
                                    arg_description="REF_RANGE_DELIM",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--sort-asc",
                                    commands=["--sort-asc"],
                                    description="Sort ascending (true) or descending (false).",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-dnp",
                                    commands=["--exclude-dnp"],
                                    description="Exclude symbols marked Do-Not-Populate.",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--keep-tabs",
                                    commands=["--keep-tabs"],
                                    description="Keep tab characters from input fields. Stripped by default.",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--keep-line-breaks",
                                    commands=["--keep-line-breaks"],
                                    description="Keep line break characters from input fields. Stripped by default.",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="dxf",
                            description="Export DXF",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output directory [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_DIR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--theme",
                                    description='Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]',
                                    arg_description="THEME_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--pages",
                                    description='List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                    arg_description="PAGE_LIST",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--black-and-white",
                                    commands=["-b", "--black-and-white"],
                                    description="Black and white only",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-drawing-sheet",
                                    commands=["-e", "--exclude-drawing-sheet"],
                                    description="No drawing sheet",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="hpgl",
                            description="Export HPGL",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output directory [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_DIR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--pages",
                                    description='List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                    arg_description="PAGE_LIST",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--pen-size",
                                    description="Pen size [mm] [nargs=0..1] [default: 0.5]",
                                    arg_description="PEN_SIZE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--origin",
                                    description="Origin and scale: 0 bottom left, 1 centered, 2 page fit, 3 content fit [nargs=0..1] [default: 1]",
                                    arg_description="ORIGIN",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-drawing-sheet",
                                    commands=["-e", "--exclude-drawing-sheet"],
                                    description="No drawing sheet",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="netlist",
                            description="Export a netlist",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--format",
                                    description='Netlist output format, valid options: kicadsexpr, kicadxml, cadstar, orcadpcb2, spice, spicemodel [nargs=0..1] [default: "kicadsexpr"]',
                                    arg_description="FORMAT",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                )
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="pdf",
                            description="Export PDF",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--theme",
                                    description='Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]',
                                    arg_description="THEME_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--pages",
                                    description='List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                    arg_description="PAGE_LIST",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--black-and-white",
                                    commands=["-b", "--black-and-white"],
                                    description="Black and white only",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-drawing-sheet",
                                    commands=["-e", "--exclude-drawing-sheet"],
                                    description="No drawing sheet",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-pdf-property-popups",
                                    commands=["--exclude-pdf-property-popups"],
                                    description="Do not generate property popups in PDF",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-background-color",
                                    commands=["-n", "--no-background-color"],
                                    description="Avoid setting a background color (regardless of theme)",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="ps",
                            description="Export PS",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output directory [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_DIR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--theme",
                                    description='Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]',
                                    arg_description="THEME_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--pages",
                                    description='List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                    arg_description="PAGE_LIST",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--black-and-white",
                                    commands=["-b", "--black-and-white"],
                                    description="Black and white only",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-drawing-sheet",
                                    commands=["-e", "--exclude-drawing-sheet"],
                                    description="No drawing sheet",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-background-color",
                                    commands=["-n", "--no-background-color"],
                                    description="Avoid setting a background color (regardless of theme)",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="python-bom",
                            description="Export the legacy BOM XML format used in the schematic editor with Python scripts",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output file [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_FILE",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                )
                            ],
                            subcommands=[],
                        ),
                        ParserL2.Command(
                            name="svg",
                            description="Export SVG",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output directory [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_DIR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--drawing-sheet",
                                    description='Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                    arg_description="SHEET_PATH",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--define-var",
                                    description="Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                    arg_description="KEY=VALUE",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--theme",
                                    description='Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]',
                                    arg_description="THEME_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--pages",
                                    description='List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                    arg_description="PAGE_LIST",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--black-and-white",
                                    commands=["-b", "--black-and-white"],
                                    description="Black and white only",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--exclude-drawing-sheet",
                                    commands=["-e", "--exclude-drawing-sheet"],
                                    description="No drawing sheet",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--no-background-color",
                                    commands=["-n", "--no-background-color"],
                                    description="Avoid setting a background color (regardless of theme)",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        ),
                    ],
                ),
            ],
        ),
        ParserL2.Command(
            name="sym",
            description="Symbol and Symbol Libraries",
            args=[],
            flags=[
                ParserL2.Flag(
                    name="--help",
                    commands=["-h", "--help"],
                    description="Shows help message and exits",
                    default=False,
                )
            ],
            subcommands=[
                ParserL2.Command(
                    name="export",
                    description="Export utilities (svg)",
                    args=[],
                    flags=[
                        ParserL2.Flag(
                            name="--help",
                            commands=["-h", "--help"],
                            description="Shows help message and exits",
                            default=False,
                        )
                    ],
                    subcommands=[
                        ParserL2.Command(
                            name="svg",
                            description="Exports the symbol or entire symbol library to SVG",
                            args=[
                                ParserL2.Argument(
                                    name="INPUT_FILE",
                                    description="Input file",
                                    arg_description="INPUT_FILE",
                                    required=True,
                                ),
                                ParserL2.Argument(
                                    name="--output",
                                    description='Output directory [nargs=0..1] [default: ""]',
                                    arg_description="OUTPUT_DIR",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--theme",
                                    description='Color theme to use (will default to symbol editor settings) [nargs=0..1] [default: ""]',
                                    arg_description="THEME_NAME",
                                    required=False,
                                ),
                                ParserL2.Argument(
                                    name="--symbol",
                                    description='Specific symbol to export within the library [nargs=0..1] [default: ""]',
                                    arg_description="SYMBOL",
                                    required=False,
                                ),
                            ],
                            flags=[
                                ParserL2.Flag(
                                    name="--help",
                                    commands=["-h", "--help"],
                                    description="Shows help message and exits",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--black-and-white",
                                    commands=["--black-and-white"],
                                    description="Black and white only",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-hidden-pins",
                                    commands=["--include-hidden-pins"],
                                    description="Include hidden pins",
                                    default=False,
                                ),
                                ParserL2.Flag(
                                    name="--include-hidden-fields",
                                    commands=["--include-hidden-fields"],
                                    description="Include hidden fields",
                                    default=False,
                                ),
                            ],
                            subcommands=[],
                        )
                    ],
                ),
                ParserL2.Command(
                    name="upgrade",
                    description="Upgrades the symbol library to the current kicad version format",
                    args=[
                        ParserL2.Argument(
                            name="INPUT_FILE",
                            description="Input file",
                            arg_description="INPUT_FILE",
                            required=True,
                        ),
                        ParserL2.Argument(
                            name="--output",
                            description='Output file [nargs=0..1] [default: ""]',
                            arg_description="OUTPUT_FILE",
                            required=False,
                        ),
                    ],
                    flags=[
                        ParserL2.Flag(
                            name="--help",
                            commands=["-h", "--help"],
                            description="Shows help message and exits",
                            default=False,
                        ),
                        ParserL2.Flag(
                            name="--force",
                            commands=["--force"],
                            description="Forces the symbol library to be resaved regardless of versioning",
                            default=False,
                        ),
                    ],
                    subcommands=[],
                ),
            ],
        ),
        ParserL2.Command(
            name="version",
            description="",
            args=[
                ParserL2.Argument(
                    name="--format",
                    description='version info format (plain, commit, about) [nargs=0..1] [default: "plain"]',
                    arg_description="VAR",
                    required=False,
                )
            ],
            flags=[
                ParserL2.Flag(
                    name="--help",
                    commands=["-h", "--help"],
                    description="Shows help message and exits",
                    default=False,
                )
            ],
            subcommands=[],
        ),
    ],
)
