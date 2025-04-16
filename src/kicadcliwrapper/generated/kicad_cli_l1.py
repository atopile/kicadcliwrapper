# This file is part of the faebryk project
# SPDX-License-Identifier: MIT


from kicadcliwrapper.lib import ParserL1

ParserL1.Command(
    command="kicad-cli",
    sections=[
        ParserL1.Section(
            name="Usage",
            lines=[
                "Usage: kicad-cli [--version] [--help] {fp,jobset,pcb,sch,sym,version}"
            ],
        ),
        ParserL1.Section(
            name="Optional arguments",
            lines=[
                "Optional arguments:",
                "-v, --version  prints version information and exits",
                "-h, --help     Shows help message and exits",
            ],
        ),
        ParserL1.Section(
            name="Subcommands",
            lines=[
                "Subcommands:",
                "fp            Footprint and Footprint Libraries",
                "jobset        Jobset",
                "pcb           PCB",
                "sch           Schematics",
                "sym           Symbol and Symbol Libraries",
                "version       Reports the version info in various formats",
            ],
        ),
    ],
    subcommands=[
        ParserL1.Command(
            command="fp",
            sections=[
                ParserL1.Section(
                    name="Usage", lines=["Usage: fp [--help] {export,upgrade}"]
                ),
                ParserL1.Section(
                    name="Footprint and Footprint Libraries",
                    lines=["Footprint and Footprint Libraries"],
                ),
                ParserL1.Section(
                    name="Optional arguments",
                    lines=[
                        "Optional arguments:",
                        "-h, --help  Shows help message and exits",
                    ],
                ),
                ParserL1.Section(
                    name="Subcommands",
                    lines=[
                        "Subcommands:",
                        "export     Export utilities (svg)",
                        "upgrade    Upgrades the footprint library to the current kicad version format",
                    ],
                ),
            ],
            subcommands=[
                ParserL1.Command(
                    command="export",
                    sections=[
                        ParserL1.Section(
                            name="Usage", lines=["Usage: export [--help] {svg}"]
                        ),
                        ParserL1.Section(
                            name="Export utilities (svg)",
                            lines=["Export utilities (svg)"],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help  Shows help message and exits",
                            ],
                        ),
                        ParserL1.Section(
                            name="Subcommands",
                            lines=[
                                "Subcommands:",
                                "svg        Exports the footprint or entire footprint library to SVG",
                            ],
                        ),
                    ],
                    subcommands=[
                        ParserL1.Command(
                            command="svg",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: svg [--help] [--output OUTPUT_DIR] [--layers LAYER_LIST] [--define-var KEY=VALUE] [--theme VAR] [--footprint FOOTPRINT_NAME] [--sketch-pads-on-fab-layers] [--hide-DNP-footprints-on-fab-layers] [--sketch-DNP-footprints-on-fab-layers] [--crossout-DNP-footprints-on-fab-layers] [--black-and-white] INPUT_DIR"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Exports the footprint or entire footprint library to SVG",
                                    lines=[
                                        "Exports the footprint or entire footprint library to SVG"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_DIR                                        Input directory",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                                       Shows help message and exits",
                                        '-o, --output                                     Output directory [nargs=0..1] [default: ""]',
                                        '-l, --layers                                     Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        "-D, --define-var                                 Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        '-t, --theme                                      Color theme to use (will default to footprint editor settings) [nargs=0..1] [default: ""]',
                                        '--fp, --footprint                                Specific footprint to export within the library [nargs=0..1] [default: ""]',
                                        "--sp, --sketch-pads-on-fab-layers                Draw pad outlines and their numbers on front and back fab layers",
                                        "--hdnp, --hide-DNP-footprints-on-fab-layers      Don't plot text & graphics of DNP footprints on fab layers",
                                        "--sdnp, --sketch-DNP-footprints-on-fab-layers    Plot graphics of DNP footprints in sketch mode on fab layers",
                                        "--cdnp, --crossout-DNP-footprints-on-fab-layers  Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators",
                                        "--black-and-white                                Black and white only",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        )
                    ],
                ),
                ParserL1.Command(
                    command="upgrade",
                    sections=[
                        ParserL1.Section(
                            name="Usage",
                            lines=[
                                "Usage: upgrade [--help] [--output OUTPUT_DIR] [--force] INPUT_DIR"
                            ],
                        ),
                        ParserL1.Section(
                            name="Upgrades the footprint library to the current kicad version format",
                            lines=[
                                "Upgrades the footprint library to the current kicad version format"
                            ],
                        ),
                        ParserL1.Section(
                            name="Positional arguments",
                            lines=[
                                "Positional arguments:",
                                "INPUT_DIR     Input directory",
                            ],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help    Shows help message and exits",
                                '-o, --output  Output directory [nargs=0..1] [default: ""]',
                                "--force       Forces the footprint library to be resaved regardless of versioning",
                            ],
                        ),
                    ],
                    subcommands=[],
                ),
            ],
        ),
        ParserL1.Command(
            command="jobset",
            sections=[
                ParserL1.Section(name="Usage", lines=["Usage: jobset [--help] {run}"]),
                ParserL1.Section(name="Jobset", lines=["Jobset"]),
                ParserL1.Section(
                    name="Optional arguments",
                    lines=[
                        "Optional arguments:",
                        "-h, --help  Shows help message and exits",
                    ],
                ),
                ParserL1.Section(
                    name="Subcommands",
                    lines=["Subcommands:", "run        Runs a jobset file"],
                ),
            ],
            subcommands=[
                ParserL1.Command(
                    command="run",
                    sections=[
                        ParserL1.Section(
                            name="Usage",
                            lines=[
                                "Usage: run [--help] [--stop-on-error] [--file JOB_FILE] [--output OUTPUT] INPUT_FILE"
                            ],
                        ),
                        ParserL1.Section(
                            name="Runs a jobset file", lines=["Runs a jobset file"]
                        ),
                        ParserL1.Section(
                            name="Positional arguments",
                            lines=[
                                "Positional arguments:",
                                "INPUT_FILE       Input file",
                            ],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help       Shows help message and exits",
                                "--stop-on-error  Stops processing jobs as they are executed sequentially on the first failure of a job",
                                '-f, --file       Jobset file to be run [nargs=0..1] [default: ""]',
                                '--output         Jobset file output to generate, leave blank for all outputs defined in the jobset [nargs=0..1] [default: ""]',
                            ],
                        ),
                    ],
                    subcommands=[],
                )
            ],
        ),
        ParserL1.Command(
            command="pcb",
            sections=[
                ParserL1.Section(
                    name="Usage", lines=["Usage: pcb [--help] {drc,export,render}"]
                ),
                ParserL1.Section(name="PCB", lines=["PCB"]),
                ParserL1.Section(
                    name="Optional arguments",
                    lines=[
                        "Optional arguments:",
                        "-h, --help  Shows help message and exits",
                    ],
                ),
                ParserL1.Section(
                    name="Subcommands",
                    lines=[
                        "Subcommands:",
                        "drc        Runs the Design Rules Check (DRC) on the PCB and creates a report",
                        "export     Export utilities (Gerbers, drill, position files, etc)",
                        "render     Renders the PCB in 3D view to PNG or JPEG image",
                    ],
                ),
            ],
            subcommands=[
                ParserL1.Command(
                    command="drc",
                    sections=[
                        ParserL1.Section(
                            name="Usage",
                            lines=[
                                "Usage: drc [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--format FORMAT] [--all-track-errors] [--schematic-parity] [--units UNITS] [--severity-all] [--severity-error] [--severity-warning] [--severity-exclusions] [--exit-code-violations] INPUT_FILE"
                            ],
                        ),
                        ParserL1.Section(
                            name="Runs the Design Rules Check (DRC) on the PCB and creates a report",
                            lines=[
                                "Runs the Design Rules Check (DRC) on the PCB and creates a report"
                            ],
                        ),
                        ParserL1.Section(
                            name="Positional arguments",
                            lines=[
                                "Positional arguments:",
                                "INPUT_FILE              Input file",
                            ],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help              Shows help message and exits",
                                '-o, --output            Output file [nargs=0..1] [default: ""]',
                                "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                '--format                Output file format, options: json, report [nargs=0..1] [default: "report"]',
                                "--all-track-errors      Report all errors for each track",
                                "--schematic-parity      Test for parity between PCB and schematic",
                                '--units                 Report units; valid options: in, mm, mils [nargs=0..1] [default: "mm"]',
                                "--severity-all          Report all DRC violations, this is equivalent to including all the other severity arguments",
                                "--severity-error        Report all DRC error level violations, this can be combined with the other severity arguments",
                                "--severity-warning      Report all DRC warning level violations, this can be combined with the other severity arguments",
                                "--severity-exclusions   Report all excluded DRC violations, this can be combined with the other severity arguments",
                                "--exit-code-violations  Return a nonzero exit code if DRC violations exist",
                            ],
                        ),
                    ],
                    subcommands=[],
                ),
                ParserL1.Command(
                    command="export",
                    sections=[
                        ParserL1.Section(
                            name="Usage",
                            lines=[
                                "Usage: export [--help] {brep,drill,dxf,gencad,gerber,gerbers,glb,ipc2581,ipcd356,odb,pdf,ply,pos,step,stl,svg,vrml,xao}"
                            ],
                        ),
                        ParserL1.Section(
                            name="Export utilities (Gerbers, drill, position files, etc)",
                            lines=[
                                "Export utilities (Gerbers, drill, position files, etc)"
                            ],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help  Shows help message and exits",
                            ],
                        ),
                        ParserL1.Section(
                            name="Subcommands",
                            lines=[
                                "Subcommands:",
                                "brep       Export BREP",
                                "drill      Generate Drill Files",
                                "dxf        Generate a DXF from a list of layers",
                                "gencad     Generate Gencad from a list of layers",
                                "gerber     Plot given layers to a single Gerber file",
                                "gerbers    Plot multiple Gerbers for a PCB, including the ability to use stored board plot settings",
                                "glb        Export GLB (binary GLTF)",
                                "ipc2581    Export the PCB in IPC-2581 format",
                                "ipcd356    Generate IPC-D-356 netlist file",
                                "odb        Export the PCB in ODB++ format",
                                "pdf        Generate PDF from a list of layers",
                                "ply        Export PLY",
                                "pos        Generate Position File",
                                "step       Export STEP",
                                "stl        Export STL",
                                "svg        Generate SVG outputs of a given layer list",
                                "vrml       Export VRML",
                                "xao        Export XAO",
                            ],
                        ),
                    ],
                    subcommands=[
                        ParserL1.Command(
                            command="brep",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: brep [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--force] [--no-unspecified] [--no-dnp] [--grid-origin] [--drill-origin] [--subst-models] [--board-only] [--cut-vias-in-body] [--no-board-body] [--no-components] [--component-filter VAR] [--include-tracks] [--include-pads] [--include-zones] [--include-inner-copper] [--include-silkscreen] [--include-soldermask] [--fuse-shapes] [--fill-all-vias] [--min-distance MIN_DIST] [--net-filter VAR] [--user-origin VAR] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export BREP", lines=["Export BREP"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE              Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help              Shows help message and exits",
                                        '-o, --output            Output file [nargs=0..1] [default: ""]',
                                        "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-f, --force             Overwrite output file",
                                        "--no-unspecified        Exclude 3D models for components with 'Unspecified' footprint type",
                                        "--no-dnp                Exclude 3D models for components with 'Do not populate' attribute",
                                        "--grid-origin           Use Grid Origin for output origin",
                                        "--drill-origin          Use Drill Origin for output origin",
                                        "--subst-models          Substitute STEP or IGS models with the same name in place of VRML models",
                                        "--board-only            Only generate a board with no components",
                                        "--cut-vias-in-body      Cut via holes in board body even if conductor layers are not exported.",
                                        "--no-board-body         Exclude board body",
                                        "--no-components         Exclude 3D models for components",
                                        '--component-filter      Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]',
                                        "--include-tracks        Export tracks and vias",
                                        "--include-pads          Export pads",
                                        "--include-zones         Export zones",
                                        "--include-inner-copper  Export elements on inner copper layers",
                                        "--include-silkscreen    Export silkscreen graphics as a set of flat faces",
                                        "--include-soldermask    Export soldermask layers as a set of flat faces",
                                        "--fuse-shapes           Fuse overlapping geometry together",
                                        "--fill-all-vias         Don't cut via holes in conductor layers.",
                                        '--min-distance          Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]',
                                        '--net-filter            Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]',
                                        '--user-origin           User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="drill",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: drill [--help] [--output OUTPUT_DIR] [--format FORMAT] [--drill-origin DRILL_ORIGIN] [--excellon-zeros-format ZEROS_FORMAT] [--excellon-oval-format OVAL_FORMAT] [--excellon-units UNITS] [--excellon-mirror-y] [--excellon-min-header] [--excellon-separate-th] [--generate-map] [--map-format MAP_FORMAT] [--gerber-precision VAR] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Generate Drill Files",
                                    lines=["Generate Drill Files"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE               Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help               Shows help message and exits",
                                        '-o, --output             Output directory [nargs=0..1] [default: ""]',
                                        '--format                 Valid options excellon, gerber. [nargs=0..1] [default: "excellon"]',
                                        '--drill-origin           Valid options are: absolute,plot [nargs=0..1] [default: "absolute"]',
                                        '--excellon-zeros-format  Valid options are: decimal,suppressleading,suppresstrailing,keep. [nargs=0..1] [default: "decimal"]',
                                        '--excellon-oval-format   Valid options are: route,alternate. [nargs=0..1] [default: "alternate"]',
                                        '-u, --excellon-units     Output units, valid options:in,mm [nargs=0..1] [default: "mm"]',
                                        "--excellon-mirror-y      Mirror Y axis",
                                        "--excellon-min-header    Minimal header",
                                        "--excellon-separate-th   Generate independent files for NPTH and PTH holes",
                                        "--generate-map           Generate map / summary of drill hits",
                                        '--map-format             Valid options: pdf,gerberx2,ps,dxf,svg [nargs=0..1] [default: "pdf"]',
                                        "--gerber-precision       Precision of Gerber coordinates (5 or 6) [nargs=0..1] [default: 6]",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="dxf",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: dxf [--help] [--output OUTPUT_FILE] [--layers LAYER_LIST] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--exclude-refdes] [--exclude-value] [--sketch-pads-on-fab-layers] [--hide-DNP-footprints-on-fab-layers] [--sketch-DNP-footprints-on-fab-layers] [--crossout-DNP-footprints-on-fab-layers] [--subtract-soldermask] [--use-contours] [--use-drill-origin] [--include-border-title] [--output-units UNITS] [--drill-shape-opt VAR] [--common-layers COMMON_LAYER_LIST] [--mode-single] [--mode-multi] [--plot-invisible-text] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Generate a DXF from a list of layers",
                                    lines=["Generate a DXF from a list of layers"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                                       Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                                       Shows help message and exits",
                                        '-o, --output                                     Output file [nargs=0..1] [default: ""]',
                                        '-l, --layers                                     Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        '--drawing-sheet                                  Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var                                 Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "--erd, --exclude-refdes                          Exclude the reference designator text",
                                        "--ev, --exclude-value                            Exclude the value text",
                                        "--sp, --sketch-pads-on-fab-layers                Draw pad outlines and their numbers on front and back fab layers",
                                        "--hdnp, --hide-DNP-footprints-on-fab-layers      Don't plot text & graphics of DNP footprints on fab layers",
                                        "--sdnp, --sketch-DNP-footprints-on-fab-layers    Plot graphics of DNP footprints in sketch mode on fab layers",
                                        "--cdnp, --crossout-DNP-footprints-on-fab-layers  Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators",
                                        "--subtract-soldermask                            Subtract soldermask from silkscreen",
                                        "--uc, --use-contours                             Plot graphic items using their contours",
                                        "--udo, --use-drill-origin                        Plot using the drill/place file origin",
                                        "--ibt, --include-border-title                    Include the border and title block",
                                        '--ou, --output-units                             Output units, valid options: mm, in [nargs=0..1] [default: "in"]',
                                        "--drill-shape-opt                                Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]",
                                        '--cl, --common-layers                            Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        "--mode-single                                    Generates a single file with the output arg path acting as the complete directory and filename path. COMMON_LAYER_LIST does not function in this mode. Instead LAYER_LIST controls all layers plotted.",
                                        "--mode-multi                                     Generates one or more files with behavior similar to the KiCad GUI plotting. The given output path specifies a directory in which files may be output.",
                                        "--plot-invisible-text                            Deprecated.  Has no effect.",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="gencad",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: gencad [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--flip-bottom-pads] [--unique-pins] [--unique-footprints] [--use-drill-origin] [--store-origin-coord] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Generate Gencad from a list of layers",
                                    lines=["Generate Gencad from a list of layers"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE              Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help              Shows help message and exits",
                                        '-o, --output            Output file [nargs=0..1] [default: ""]',
                                        "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-f, --flip-bottom-pads  Flip bottom footprint padstacks",
                                        "--unique-pins          Generate unique pin names",
                                        "--unique-footprints    Generate a new shape for each footprint instance (do not reuse shapes)",
                                        "--use-drill-origin     Use drill/place file origin as origin",
                                        "--store-origin-coord   Save the origin coordinates in the file",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="gerber",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: gerber [--help] [--output OUTPUT_FILE] [--layers LAYER_LIST] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--exclude-refdes] [--exclude-value] [--include-border-title] [--sketch-pads-on-fab-layers] [--hide-DNP-footprints-on-fab-layers] [--sketch-DNP-footprints-on-fab-layers] [--crossout-DNP-footprints-on-fab-layers] [--no-x2] [--no-netlist] [--subtract-soldermask] [--disable-aperture-macros] [--use-drill-file-origin] [--common-layers COMMON_LAYER_LIST] [--precision PRECISION] [--no-protel-ext] [--plot-invisible-text] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Plot given layers to a single Gerber file",
                                    lines=["Plot given layers to a single Gerber file"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                                       Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                                       Shows help message and exits",
                                        '-o, --output                                     Output file [nargs=0..1] [default: ""]',
                                        '-l, --layers                                     Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        '--drawing-sheet                                  Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var                                 Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "--erd, --exclude-refdes                          Exclude the reference designator text",
                                        "--ev, --exclude-value                            Exclude the value text",
                                        "--ibt, --include-border-title                    Include the border and title block",
                                        "--sp, --sketch-pads-on-fab-layers                Draw pad outlines and their numbers on front and back fab layers",
                                        "--hdnp, --hide-DNP-footprints-on-fab-layers      Don't plot text & graphics of DNP footprints on fab layers",
                                        "--sdnp, --sketch-DNP-footprints-on-fab-layers    Plot graphics of DNP footprints in sketch mode on fab layers",
                                        "--cdnp, --crossout-DNP-footprints-on-fab-layers  Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators",
                                        "--no-x2                                          Do not use the extended X2 format",
                                        "--no-netlist                                     Do not generate netlist attributes",
                                        "--subtract-soldermask                            Subtract soldermask from silkscreen",
                                        "--disable-aperture-macros                        Disable aperture macros",
                                        "--use-drill-file-origin                          Use drill/place file origin",
                                        '--cl, --common-layers                            Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        "--precision                                      Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]",
                                        "--no-protel-ext                                  Use KiCad Gerber file extension",
                                        "--plot-invisible-text                            Deprecated.  Has no effect.",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="gerbers",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: gerbers [--help] [--output OUTPUT_FILE] [--layers LAYER_LIST] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--exclude-refdes] [--exclude-value] [--include-border-title] [--sketch-pads-on-fab-layers] [--hide-DNP-footprints-on-fab-layers] [--sketch-DNP-footprints-on-fab-layers] [--crossout-DNP-footprints-on-fab-layers] [--no-x2] [--no-netlist] [--subtract-soldermask] [--disable-aperture-macros] [--use-drill-file-origin] [--common-layers COMMON_LAYER_LIST] [--precision PRECISION] [--no-protel-ext] [--plot-invisible-text] [--common-layers COMMON_LAYER_LIST] [--board-plot-params] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Plot multiple Gerbers for a PCB, including the ability to use stored board plot settings",
                                    lines=[
                                        "Plot multiple Gerbers for a PCB, including the ability to use stored board plot settings"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                                       Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                                       Shows help message and exits",
                                        '-o, --output                                     Output file [nargs=0..1] [default: ""]',
                                        '-l, --layers                                     Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        '--drawing-sheet                                  Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var                                 Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "--erd, --exclude-refdes                          Exclude the reference designator text",
                                        "--ev, --exclude-value                            Exclude the value text",
                                        "--ibt, --include-border-title                    Include the border and title block",
                                        "--sp, --sketch-pads-on-fab-layers                Draw pad outlines and their numbers on front and back fab layers",
                                        "--hdnp, --hide-DNP-footprints-on-fab-layers      Don't plot text & graphics of DNP footprints on fab layers",
                                        "--sdnp, --sketch-DNP-footprints-on-fab-layers    Plot graphics of DNP footprints in sketch mode on fab layers",
                                        "--cdnp, --crossout-DNP-footprints-on-fab-layers  Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators",
                                        "--no-x2                                          Do not use the extended X2 format",
                                        "--no-netlist                                     Do not generate netlist attributes",
                                        "--subtract-soldermask                            Subtract soldermask from silkscreen",
                                        "--disable-aperture-macros                        Disable aperture macros",
                                        "--use-drill-file-origin                          Use drill/place file origin",
                                        '--cl, --common-layers                            Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        "--precision                                      Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]",
                                        "--no-protel-ext                                  Use KiCad Gerber file extension",
                                        "--plot-invisible-text                            Deprecated.  Has no effect.",
                                        '--cl, --common-layers                            Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        "--board-plot-params                              Use the Gerber plot settings already configured in the board file",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="glb",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: glb [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--force] [--no-unspecified] [--no-dnp] [--grid-origin] [--drill-origin] [--subst-models] [--board-only] [--cut-vias-in-body] [--no-board-body] [--no-components] [--component-filter VAR] [--include-tracks] [--include-pads] [--include-zones] [--include-inner-copper] [--include-silkscreen] [--include-soldermask] [--fuse-shapes] [--fill-all-vias] [--min-distance MIN_DIST] [--net-filter VAR] [--user-origin VAR] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export GLB (binary GLTF)",
                                    lines=["Export GLB (binary GLTF)"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE              Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help              Shows help message and exits",
                                        '-o, --output            Output file [nargs=0..1] [default: ""]',
                                        "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-f, --force             Overwrite output file",
                                        "--no-unspecified        Exclude 3D models for components with 'Unspecified' footprint type",
                                        "--no-dnp                Exclude 3D models for components with 'Do not populate' attribute",
                                        "--grid-origin           Use Grid Origin for output origin",
                                        "--drill-origin          Use Drill Origin for output origin",
                                        "--subst-models          Substitute STEP or IGS models with the same name in place of VRML models",
                                        "--board-only            Only generate a board with no components",
                                        "--cut-vias-in-body      Cut via holes in board body even if conductor layers are not exported.",
                                        "--no-board-body         Exclude board body",
                                        "--no-components         Exclude 3D models for components",
                                        '--component-filter      Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]',
                                        "--include-tracks        Export tracks and vias",
                                        "--include-pads          Export pads",
                                        "--include-zones         Export zones",
                                        "--include-inner-copper  Export elements on inner copper layers",
                                        "--include-silkscreen    Export silkscreen graphics as a set of flat faces",
                                        "--include-soldermask    Export soldermask layers as a set of flat faces",
                                        "--fuse-shapes           Fuse overlapping geometry together",
                                        "--fill-all-vias         Don't cut via holes in conductor layers.",
                                        '--min-distance          Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]',
                                        '--net-filter            Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]',
                                        '--user-origin           User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="ipc2581",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: ipc2581 [--help] [--output OUTPUT_FILE] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--precision PRECISION] [--compress] [--version VAR] [--units VAR] [--bom-col-int-id FIELD_NAME] [--bom-col-mfg-pn FIELD_NAME] [--bom-col-mfg FIELD_NAME] [--bom-col-dist-pn FIELD_NAME] [--bom-col-dist FIELD_NAME] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export the PCB in IPC-2581 format",
                                    lines=["Export the PCB in IPC-2581 format"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE         Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help         Shows help message and exits",
                                        '-o, --output       Output file [nargs=0..1] [default: ""]',
                                        '--drawing-sheet    Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var   Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "--precision        Precision [nargs=0..1] [default: 6]",
                                        "--compress         Compress the output",
                                        '--version          IPC-2581 standard version [nargs=0..1] [default: "C"]',
                                        '--units            Units [nargs=0..1] [default: "mm"]',
                                        '--bom-col-int-id   Name of the part field to use for the Bill of Material Internal Id Column [nargs=0..1] [default: ""]',
                                        '--bom-col-mfg-pn   Name of the part field to use for the Bill of Material Manufacturer Part Number Column [nargs=0..1] [default: ""]',
                                        '--bom-col-mfg      Name of the part field to use for the Bill of Material Manufacturer Column [nargs=0..1] [default: ""]',
                                        '--bom-col-dist-pn  Name of the part field to use for the Bill of Material Distributor Part Number Column [nargs=0..1] [default: ""]',
                                        '--bom-col-dist     Name to insert into Bill of Material Distributor Column [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="ipcd356",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: ipcd356 [--help] [--output OUTPUT_FILE] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Generate IPC-D-356 netlist file",
                                    lines=["Generate IPC-D-356 netlist file"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE    Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help    Shows help message and exits",
                                        '-o, --output  Output file [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="odb",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: odb [--help] [--output OUTPUT_FILE] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--precision PRECISION] [--compression VAR] [--units VAR] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export the PCB in ODB++ format",
                                    lines=["Export the PCB in ODB++ format"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE        Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help        Shows help message and exits",
                                        '-o, --output      Output file [nargs=0..1] [default: ""]',
                                        '--drawing-sheet   Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var  Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "--precision       Precision [nargs=0..1] [default: 2]",
                                        '--compression     Compression mode [nargs=0..1] [default: "zip"]',
                                        '--units           Units [nargs=0..1] [default: "mm"]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="pdf",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: pdf [--help] [--output OUTPUT_FILE] [--layers LAYER_LIST] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--mirror] [--exclude-refdes] [--exclude-value] [--include-border-title] [--subtract-soldermask] [--sketch-pads-on-fab-layers] [--hide-DNP-footprints-on-fab-layers] [--sketch-DNP-footprints-on-fab-layers] [--crossout-DNP-footprints-on-fab-layers] [--negative] [--black-and-white] [--theme THEME_NAME] [--drill-shape-opt VAR] [--common-layers COMMON_LAYER_LIST] [--plot-invisible-text] [--mode-single] [--mode-separate] [--mode-multipage] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Generate PDF from a list of layers",
                                    lines=["Generate PDF from a list of layers"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                                       Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                                       Shows help message and exits",
                                        '-o, --output                                     Output file [nargs=0..1] [default: ""]',
                                        '-l, --layers                                     Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        '--drawing-sheet                                  Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var                                 Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-m, --mirror                                     Mirror the board (useful for trying to show bottom layers)",
                                        "--erd, --exclude-refdes                          Exclude the reference designator text",
                                        "--ev, --exclude-value                            Exclude the value text",
                                        "--ibt, --include-border-title                    Include the border and title block",
                                        "--subtract-soldermask                            Subtract soldermask from silkscreen",
                                        "--sp, --sketch-pads-on-fab-layers                Draw pad outlines and their numbers on front and back fab layers",
                                        "--hdnp, --hide-DNP-footprints-on-fab-layers      Don't plot text & graphics of DNP footprints on fab layers",
                                        "--sdnp, --sketch-DNP-footprints-on-fab-layers    Plot graphics of DNP footprints in sketch mode on fab layers",
                                        "--cdnp, --crossout-DNP-footprints-on-fab-layers  Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators",
                                        "-n, --negative                                   Plot as negative (useful for directly etching from the export)",
                                        "--black-and-white                                Black and white only",
                                        '-t, --theme                                      Color theme to use (will default to PCB Editor settings) [nargs=0..1] [default: ""]',
                                        "--drill-shape-opt                                Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]",
                                        '--cl, --common-layers                            Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        "--plot-invisible-text                            Deprecated.  Has no effect.",
                                        "--mode-single                                    Generates a single file with the output arg path acting as the complete directory and filename path. COMMON_LAYER_LIST does not function in this mode. Instead LAYER_LIST controls all layers plotted.",
                                        "--mode-separate                                  Plot the layers to individual PDF files",
                                        "--mode-multipage                                 Plot the layers to a single PDF file with multiple pages",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="ply",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: ply [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--force] [--no-unspecified] [--no-dnp] [--grid-origin] [--drill-origin] [--subst-models] [--board-only] [--cut-vias-in-body] [--no-board-body] [--no-components] [--component-filter VAR] [--include-tracks] [--include-pads] [--include-zones] [--include-inner-copper] [--include-silkscreen] [--include-soldermask] [--fuse-shapes] [--fill-all-vias] [--min-distance MIN_DIST] [--net-filter VAR] [--user-origin VAR] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export PLY", lines=["Export PLY"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE              Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help              Shows help message and exits",
                                        '-o, --output            Output file [nargs=0..1] [default: ""]',
                                        "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-f, --force             Overwrite output file",
                                        "--no-unspecified        Exclude 3D models for components with 'Unspecified' footprint type",
                                        "--no-dnp                Exclude 3D models for components with 'Do not populate' attribute",
                                        "--grid-origin           Use Grid Origin for output origin",
                                        "--drill-origin          Use Drill Origin for output origin",
                                        "--subst-models          Substitute STEP or IGS models with the same name in place of VRML models",
                                        "--board-only            Only generate a board with no components",
                                        "--cut-vias-in-body      Cut via holes in board body even if conductor layers are not exported.",
                                        "--no-board-body         Exclude board body",
                                        "--no-components         Exclude 3D models for components",
                                        '--component-filter      Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]',
                                        "--include-tracks        Export tracks and vias",
                                        "--include-pads          Export pads",
                                        "--include-zones         Export zones",
                                        "--include-inner-copper  Export elements on inner copper layers",
                                        "--include-silkscreen    Export silkscreen graphics as a set of flat faces",
                                        "--include-soldermask    Export soldermask layers as a set of flat faces",
                                        "--fuse-shapes           Fuse overlapping geometry together",
                                        "--fill-all-vias         Don't cut via holes in conductor layers.",
                                        '--min-distance          Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]',
                                        '--net-filter            Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]',
                                        '--user-origin           User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="pos",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: pos [--help] [--output OUTPUT_FILE] [--side VAR] [--format FORMAT] [--units UNITS] [--bottom-negate-x] [--use-drill-file-origin] [--smd-only] [--exclude-fp-th] [--exclude-dnp] [--gerber-board-edge] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Generate Position File",
                                    lines=["Generate Position File"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE               Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help               Shows help message and exits",
                                        '-o, --output             Output file [nargs=0..1] [default: ""]',
                                        '--side                   Valid options: front,back,both. Gerber format only supports "front" or "back". [nargs=0..1] [default: "both"]',
                                        '--format                 Valid options: ascii,csv,gerber [nargs=0..1] [default: "ascii"]',
                                        '--units                  Output units; ascii or csv format only; valid options: in,mm [nargs=0..1] [default: "in"]',
                                        "--bottom-negate-x        Use negative X coordinates for footprints on bottom layer (ascii or csv formats only)",
                                        "--use-drill-file-origin  Use drill/place file origin (ascii or csv only)",
                                        "--smd-only               Include only SMD footprints (ascii or csv only)",
                                        "--exclude-fp-th          Exclude all footprints with through-hole pads (ascii or csv only)",
                                        "--exclude-dnp            Exclude all footprints with the Do Not Populate flag set",
                                        "--gerber-board-edge      Include board edge layer (Gerber only)",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="step",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: step [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--force] [--no-unspecified] [--no-dnp] [--grid-origin] [--drill-origin] [--subst-models] [--board-only] [--cut-vias-in-body] [--no-board-body] [--no-components] [--component-filter VAR] [--include-tracks] [--include-pads] [--include-zones] [--include-inner-copper] [--include-silkscreen] [--include-soldermask] [--fuse-shapes] [--fill-all-vias] [--min-distance MIN_DIST] [--net-filter VAR] [--no-optimize-step] [--user-origin VAR] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export STEP", lines=["Export STEP"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE              Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help              Shows help message and exits",
                                        '-o, --output            Output file [nargs=0..1] [default: ""]',
                                        "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-f, --force             Overwrite output file",
                                        "--no-unspecified        Exclude 3D models for components with 'Unspecified' footprint type",
                                        "--no-dnp                Exclude 3D models for components with 'Do not populate' attribute",
                                        "--grid-origin           Use Grid Origin for output origin",
                                        "--drill-origin          Use Drill Origin for output origin",
                                        "--subst-models          Substitute STEP or IGS models with the same name in place of VRML models",
                                        "--board-only            Only generate a board with no components",
                                        "--cut-vias-in-body      Cut via holes in board body even if conductor layers are not exported.",
                                        "--no-board-body         Exclude board body",
                                        "--no-components         Exclude 3D models for components",
                                        '--component-filter      Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]',
                                        "--include-tracks        Export tracks and vias",
                                        "--include-pads          Export pads",
                                        "--include-zones         Export zones",
                                        "--include-inner-copper  Export elements on inner copper layers",
                                        "--include-silkscreen    Export silkscreen graphics as a set of flat faces",
                                        "--include-soldermask    Export soldermask layers as a set of flat faces",
                                        "--fuse-shapes           Fuse overlapping geometry together",
                                        "--fill-all-vias         Don't cut via holes in conductor layers.",
                                        '--min-distance          Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]',
                                        '--net-filter            Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]',
                                        "--no-optimize-step      Do not optimize STEP file (enables writing parametric curves)",
                                        '--user-origin           User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="stl",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: stl [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--force] [--no-unspecified] [--no-dnp] [--grid-origin] [--drill-origin] [--subst-models] [--board-only] [--cut-vias-in-body] [--no-board-body] [--no-components] [--component-filter VAR] [--include-tracks] [--include-pads] [--include-zones] [--include-inner-copper] [--include-silkscreen] [--include-soldermask] [--fuse-shapes] [--fill-all-vias] [--min-distance MIN_DIST] [--net-filter VAR] [--user-origin VAR] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export STL", lines=["Export STL"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE              Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help              Shows help message and exits",
                                        '-o, --output            Output file [nargs=0..1] [default: ""]',
                                        "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-f, --force             Overwrite output file",
                                        "--no-unspecified        Exclude 3D models for components with 'Unspecified' footprint type",
                                        "--no-dnp                Exclude 3D models for components with 'Do not populate' attribute",
                                        "--grid-origin           Use Grid Origin for output origin",
                                        "--drill-origin          Use Drill Origin for output origin",
                                        "--subst-models          Substitute STEP or IGS models with the same name in place of VRML models",
                                        "--board-only            Only generate a board with no components",
                                        "--cut-vias-in-body      Cut via holes in board body even if conductor layers are not exported.",
                                        "--no-board-body         Exclude board body",
                                        "--no-components         Exclude 3D models for components",
                                        '--component-filter      Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]',
                                        "--include-tracks        Export tracks and vias",
                                        "--include-pads          Export pads",
                                        "--include-zones         Export zones",
                                        "--include-inner-copper  Export elements on inner copper layers",
                                        "--include-silkscreen    Export silkscreen graphics as a set of flat faces",
                                        "--include-soldermask    Export soldermask layers as a set of flat faces",
                                        "--fuse-shapes           Fuse overlapping geometry together",
                                        "--fill-all-vias         Don't cut via holes in conductor layers.",
                                        '--min-distance          Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]',
                                        '--net-filter            Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]',
                                        '--user-origin           User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="svg",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: svg [--help] [--output OUTPUT_FILE] [--layers LAYER_LIST] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--subtract-soldermask] [--mirror] [--theme THEME_NAME] [--negative] [--black-and-white] [--sketch-pads-on-fab-layers] [--hide-DNP-footprints-on-fab-layers] [--sketch-DNP-footprints-on-fab-layers] [--crossout-DNP-footprints-on-fab-layers] [--page-size-mode MODE] [--fit-page-to-board] [--exclude-drawing-sheet] [--drill-shape-opt SHAPE_OPTION] [--common-layers COMMON_LAYER_LIST] [--mode-single] [--mode-multi] [--plot-invisible-text] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Generate SVG outputs of a given layer list",
                                    lines=[
                                        "Generate SVG outputs of a given layer list"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                                       Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                                       Shows help message and exits",
                                        '-o, --output                                     Output file [nargs=0..1] [default: ""]',
                                        '-l, --layers                                     Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        '--drawing-sheet                                  Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var                                 Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "--subtract-soldermask                            Subtract soldermask from silkscreen",
                                        "-m, --mirror                                     Mirror the board (useful for trying to show bottom layers)",
                                        '-t, --theme                                      Color theme to use (will default to PCB editor settings) [nargs=0..1] [default: ""]',
                                        "-n, --negative                                   Plot as negative (useful for directly etching from the export)",
                                        "--black-and-white                                Black and white only",
                                        "--sp, --sketch-pads-on-fab-layers                Draw pad outlines and their numbers on front and back fab layers",
                                        "--hdnp, --hide-DNP-footprints-on-fab-layers      Don't plot text & graphics of DNP footprints on fab layers",
                                        "--sdnp, --sketch-DNP-footprints-on-fab-layers    Plot graphics of DNP footprints in sketch mode on fab layers",
                                        "--cdnp, --crossout-DNP-footprints-on-fab-layers  Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators",
                                        "--page-size-mode                                 Set page sizing mode (0 = page with frame and title block, 1 = current page size, 2 = board area only) [nargs=0..1] [default: 0]",
                                        "--fit-page-to-board                              Fit the page to the board",
                                        "--exclude-drawing-sheet                          No drawing sheet",
                                        "--drill-shape-opt                                Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]",
                                        '--cl, --common-layers                            Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]',
                                        "--mode-single                                    Generates a single file with the output arg path acting as the complete directory and filename path. COMMON_LAYER_LIST does not function in this mode. Instead LAYER_LIST controls all layers plotted.",
                                        "--mode-multi                                     Generates one or more files with behavior similar to the KiCad GUI plotting. The given output path specifies a directory in which files may be output.",
                                        "--plot-invisible-text                            Deprecated.  Has no effect.",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="vrml",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: vrml [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--force] [--no-unspecified] [--no-dnp] [--user-origin VAR] [--units VAR] [--models-dir VAR] [--models-relative] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export VRML", lines=["Export VRML"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE         Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help         Shows help message and exits",
                                        '-o, --output       Output file [nargs=0..1] [default: ""]',
                                        "-D, --define-var   Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-f, --force        Overwrite output file",
                                        "--no-unspecified   Exclude 3D models for components with 'Unspecified' footprint type",
                                        "--no-dnp           Exclude 3D models for components with 'Do not populate' attribute",
                                        '--user-origin      User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                        '--units            Output units; valid options: mm, m, in, tenths [nargs=0..1] [default: "in"]',
                                        '--models-dir       Name of folder to create and store 3d models in, if not specified or empty, the models will be embedded in main exported VRML file [nargs=0..1] [default: ""]',
                                        "--models-relative  Used with --models-dir to output relative paths in the resulting file",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="xao",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: xao [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--force] [--no-unspecified] [--no-dnp] [--grid-origin] [--drill-origin] [--subst-models] [--board-only] [--cut-vias-in-body] [--no-board-body] [--no-components] [--component-filter VAR] [--include-tracks] [--include-pads] [--include-zones] [--include-inner-copper] [--include-silkscreen] [--include-soldermask] [--fuse-shapes] [--fill-all-vias] [--min-distance MIN_DIST] [--net-filter VAR] [--user-origin VAR] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export XAO", lines=["Export XAO"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE              Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help              Shows help message and exits",
                                        '-o, --output            Output file [nargs=0..1] [default: ""]',
                                        "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-f, --force             Overwrite output file",
                                        "--no-unspecified        Exclude 3D models for components with 'Unspecified' footprint type",
                                        "--no-dnp                Exclude 3D models for components with 'Do not populate' attribute",
                                        "--grid-origin           Use Grid Origin for output origin",
                                        "--drill-origin          Use Drill Origin for output origin",
                                        "--subst-models          Substitute STEP or IGS models with the same name in place of VRML models",
                                        "--board-only            Only generate a board with no components",
                                        "--cut-vias-in-body      Cut via holes in board body even if conductor layers are not exported.",
                                        "--no-board-body         Exclude board body",
                                        "--no-components         Exclude 3D models for components",
                                        '--component-filter      Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]',
                                        "--include-tracks        Export tracks and vias",
                                        "--include-pads          Export pads",
                                        "--include-zones         Export zones",
                                        "--include-inner-copper  Export elements on inner copper layers",
                                        "--include-silkscreen    Export silkscreen graphics as a set of flat faces",
                                        "--include-soldermask    Export soldermask layers as a set of flat faces",
                                        "--fuse-shapes           Fuse overlapping geometry together",
                                        "--fill-all-vias         Don't cut via holes in conductor layers.",
                                        '--min-distance          Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]',
                                        '--net-filter            Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]',
                                        '--user-origin           User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                    ],
                ),
                ParserL1.Command(
                    command="render",
                    sections=[
                        ParserL1.Section(
                            name="Usage",
                            lines=[
                                "Usage: render [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--width WIDTH] [--height HEIGHT] [--side SIDE] [--background BG] [--quality QUALITY] [--preset PRESET] [--floor] [--perspective] [--zoom ZOOM] [--pan VECTOR] [--pivot PIVOT] [--rotate ANGLES] [--light-top COLOR] [--light-bottom COLOR] [--light-side COLOR] [--light-camera COLOR] [--light-side-elevation ANGLE] INPUT_FILE"
                            ],
                        ),
                        ParserL1.Section(
                            name="Renders the PCB in 3D view to PNG or JPEG image",
                            lines=["Renders the PCB in 3D view to PNG or JPEG image"],
                        ),
                        ParserL1.Section(
                            name="Positional arguments",
                            lines=[
                                "Positional arguments:",
                                "INPUT_FILE              Input file",
                            ],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help              Shows help message and exits",
                                '-o, --output            Output file [nargs=0..1] [default: ""]',
                                "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                "-w, --width             Image width [nargs=0..1] [default: 1600]",
                                "-h, --height            Image height [nargs=0..1] [default: 900]",
                                '--side                  Render from side. Options: top, bottom, left, right, front, back [nargs=0..1] [default: "top"]',
                                '--background            Image background. Options: default, transparent, opaque. Default: transparent for PNG, opaque for JPEG [nargs=0..1] [default: ""]',
                                '--quality               Render quality. Options: basic, high, user [nargs=0..1] [default: "basic"]',
                                '--preset                Color preset. Options: follow_pcb_editor, follow_plot_settings, legacy_preset_flag, ... [nargs=0..1] [default: "follow_plot_settings"]',
                                "--floor                 Enables floor, shadows and post-processing, even if disabled in quality preset",
                                "--perspective           Use perspective projection instead of orthogonal",
                                "--zoom                  Camera zoom [nargs=0..1] [default: 1]",
                                "--pan                   Pan camera, format 'X,Y,Z' e.g.: '3,0,0' [nargs=0..1] [default: \"\"]",
                                "--pivot                 Set pivot point relative to the board center in centimeters, format 'X,Y,Z' e.g.: '-10,2,0' [nargs=0..1] [default: \"\"]",
                                "--rotate                Rotate board, format 'X,Y,Z' e.g.: '-45,0,45' for isometric view [nargs=0..1] [default: \"\"]",
                                "--light-top             Top light intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: \"\"]",
                                "--light-bottom          Bottom light intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: \"\"]",
                                "--light-side            Side lights intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: \"\"]",
                                "--light-camera          Camera light intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: \"\"]",
                                "--light-side-elevation  Side lights elevation angle in degrees, range: 0-90 [nargs=0..1] [default: 60]",
                            ],
                        ),
                    ],
                    subcommands=[],
                ),
            ],
        ),
        ParserL1.Command(
            command="sch",
            sections=[
                ParserL1.Section(
                    name="Usage", lines=["Usage: sch [--help] {erc,export}"]
                ),
                ParserL1.Section(name="Schematics", lines=["Schematics"]),
                ParserL1.Section(
                    name="Optional arguments",
                    lines=[
                        "Optional arguments:",
                        "-h, --help  Shows help message and exits",
                    ],
                ),
                ParserL1.Section(
                    name="Subcommands",
                    lines=[
                        "Subcommands:",
                        "erc        Runs the Electrical Rules Check (ERC) on the schematic and creates a report",
                        "export     Export utilities (netlist, pdf, bom, etc)",
                    ],
                ),
            ],
            subcommands=[
                ParserL1.Command(
                    command="erc",
                    sections=[
                        ParserL1.Section(
                            name="Usage",
                            lines=[
                                "Usage: erc [--help] [--output OUTPUT_FILE] [--define-var KEY=VALUE] [--format VAR] [--units VAR] [--severity-all] [--severity-error] [--severity-warning] [--severity-exclusions] [--exit-code-violations] INPUT_FILE"
                            ],
                        ),
                        ParserL1.Section(
                            name="Runs the Electrical Rules Check (ERC) on the schematic and creates a report",
                            lines=[
                                "Runs the Electrical Rules Check (ERC) on the schematic and creates a report"
                            ],
                        ),
                        ParserL1.Section(
                            name="Positional arguments",
                            lines=[
                                "Positional arguments:",
                                "INPUT_FILE              Input file",
                            ],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help              Shows help message and exits",
                                '-o, --output            Output file [nargs=0..1] [default: ""]',
                                "-D, --define-var        Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                '--format                Output file format, options: json, report [nargs=0..1] [default: "report"]',
                                '--units                 Report units; valid options: in, mm, mils [nargs=0..1] [default: "mm"]',
                                "--severity-all          Report all ERC violations, this is equivalent to including all the other severity arguments",
                                "--severity-error        Report all ERC error level violations, this can be combined with the other severity arguments",
                                "--severity-warning      Report all ERC warning level violations, this can be combined with the other severity arguments",
                                "--severity-exclusions   Report all excluded ERC violations, this can be combined with the other severity arguments",
                                "--exit-code-violations  Return a nonzero exit code if ERC violations exist",
                            ],
                        ),
                    ],
                    subcommands=[],
                ),
                ParserL1.Command(
                    command="export",
                    sections=[
                        ParserL1.Section(
                            name="Usage",
                            lines=[
                                "Usage: export [--help] {bom,dxf,hpgl,netlist,pdf,ps,python-bom,svg}"
                            ],
                        ),
                        ParserL1.Section(
                            name="Export utilities (netlist, pdf, bom, etc)",
                            lines=["Export utilities (netlist, pdf, bom, etc)"],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help  Shows help message and exits",
                            ],
                        ),
                        ParserL1.Section(
                            name="Subcommands",
                            lines=[
                                "Subcommands:",
                                "bom        Generate a Bill of Materials (BOM)",
                                "dxf        Export DXF",
                                "hpgl       Export HPGL",
                                "netlist    Export a netlist",
                                "pdf        Export PDF",
                                "ps         Export PS",
                                "python-bom Export the legacy BOM XML format used in the schematic editor with Python scripts",
                                "svg        Export SVG",
                            ],
                        ),
                    ],
                    subcommands=[
                        ParserL1.Command(
                            command="bom",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: bom [--help] [--output OUTPUT_FILE] [--preset PRESET] [--format-preset FMT_PRESET] [--fields FIELDS] [--labels LABELS] [--group-by GROUP_BY] [--sort-field SORT_BY] [--sort-asc] [--filter FILTER] [--exclude-dnp] [--include-excluded-from-bom] [--field-delimiter FIELD_DELIM] [--string-delimiter STR_DELIM] [--ref-delimiter REF_DELIM] [--ref-range-delimiter REF_RANGE_DELIM] [--keep-tabs] [--keep-line-breaks] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Generate a Bill of Materials (BOM)",
                                    lines=["Generate a Bill of Materials (BOM)"],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                   Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                   Shows help message and exits",
                                        '-o, --output                 Output file [nargs=0..1] [default: ""]',
                                        '--preset                     Use a named BOM preset setting from the schematic, e.g. "Grouped By Value". [nargs=0..1] [default: ""]',
                                        '--format-preset              Use a named BOM format preset setting from the schematic, e.g. CSV. [nargs=0..1] [default: ""]',
                                        '--fields                     An ordered list of fields to export. See documentation for special substitutions. [nargs=0..1] [default: "Reference,Value,Footprint,${QUANTITY},${DNP}"]',
                                        '--labels                     An ordered list of labels to apply the exported fields. [nargs=0..1] [default: "Refs,Value,Footprint,Qty,DNP"]',
                                        '--group-by                   Fields to group references by when field values match. [nargs=0..1] [default: ""]',
                                        '--sort-field                 Field name to sort by. [nargs=0..1] [default: "Reference"]',
                                        "--sort-asc                   Sort ascending (true) or descending (false).",
                                        '--filter                     Filter string to remove output lines. [nargs=0..1] [default: ""]',
                                        "--exclude-dnp                Exclude symbols marked Do-Not-Populate.",
                                        "--include-excluded-from-bom  Include symbols marked 'Exclude from BOM'.",
                                        '--field-delimiter            Separator between output fields/columns. [nargs=0..1] [default: ","]',
                                        '--string-delimiter           Character to surround fields with. [nargs=0..1] [default: """]',
                                        '--ref-delimiter              Character to place between individual references. [nargs=0..1] [default: ","]',
                                        '--ref-range-delimiter        Character to place in ranges of references. Leave blank for no ranges. [nargs=0..1] [default: "-"]',
                                        "--keep-tabs                  Keep tab characters from input fields. Stripped by default.",
                                        "--keep-line-breaks           Keep line break characters from input fields. Stripped by default.",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="dxf",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: dxf [--help] [--output OUTPUT_DIR] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--theme THEME_NAME] [--black-and-white] [--exclude-drawing-sheet] [--default-font VAR] [--pages PAGE_LIST] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export DXF", lines=["Export DXF"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                   Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                   Shows help message and exits",
                                        '-o, --output                 Output directory [nargs=0..1] [default: ""]',
                                        '--drawing-sheet              Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var             Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        '-t, --theme                  Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]',
                                        "-b, --black-and-white        Black and white only",
                                        "-e, --exclude-drawing-sheet  No drawing sheet",
                                        '--default-font               Default font name [nargs=0..1] [default: "KiCad Font"]',
                                        '--pages                      List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="hpgl",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: hpgl [--help] [--output OUTPUT_DIR] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--exclude-drawing-sheet] [--default-font VAR] [--pages PAGE_LIST] [--pen-size PEN_SIZE] [--origin ORIGIN] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export HPGL", lines=["Export HPGL"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                   Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                   Shows help message and exits",
                                        '-o, --output                 Output directory [nargs=0..1] [default: ""]',
                                        '--drawing-sheet              Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var             Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        "-e, --exclude-drawing-sheet  No drawing sheet",
                                        '--default-font               Default font name [nargs=0..1] [default: "KiCad Font"]',
                                        '--pages                      List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                        "-p, --pen-size               Pen size [mm] [nargs=0..1] [default: 0.5]",
                                        "-r, --origin                 Origin and scale: 0 bottom left, 1 centered, 2 page fit, 3 content fit [nargs=0..1] [default: 1]",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="netlist",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: netlist [--help] [--output OUTPUT_FILE] [--format FORMAT] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export a netlist", lines=["Export a netlist"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE    Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help    Shows help message and exits",
                                        '-o, --output  Output file [nargs=0..1] [default: ""]',
                                        '--format      Netlist output format, valid options: kicadsexpr, kicadxml, cadstar, orcadpcb2, spice, spicemodel, pads, allegro [nargs=0..1] [default: "kicadsexpr"]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="pdf",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: pdf [--help] [--output OUTPUT_FILE] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--theme THEME_NAME] [--black-and-white] [--exclude-drawing-sheet] [--default-font VAR] [--exclude-pdf-property-popups] [--exclude-pdf-hierarchical-links] [--exclude-pdf-metadata] [--no-background-color] [--pages PAGE_LIST] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export PDF", lines=["Export PDF"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                        Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                        Shows help message and exits",
                                        '-o, --output                      Output file [nargs=0..1] [default: ""]',
                                        '--drawing-sheet                   Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var                  Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        '-t, --theme                       Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]',
                                        "-b, --black-and-white             Black and white only",
                                        "-e, --exclude-drawing-sheet       No drawing sheet",
                                        '--default-font                    Default font name [nargs=0..1] [default: "KiCad Font"]',
                                        "--exclude-pdf-property-popups     Do not generate property popups in PDF",
                                        "--exclude-pdf-hierarchical-links  Do not generate clickable links for hierarchical elements in PDF",
                                        "--exclude-pdf-metadata            Do not generate PDF metadata from AUTHOR and SUBJECT variables",
                                        "-n, --no-background-color         Avoid setting a background color (regardless of theme)",
                                        '--pages                           List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="ps",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: ps [--help] [--output OUTPUT_DIR] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--theme THEME_NAME] [--black-and-white] [--exclude-drawing-sheet] [--default-font VAR] [--no-background-color] [--pages PAGE_LIST] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(name="Export PS", lines=["Export PS"]),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                   Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                   Shows help message and exits",
                                        '-o, --output                 Output directory [nargs=0..1] [default: ""]',
                                        '--drawing-sheet              Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var             Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        '-t, --theme                  Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]',
                                        "-b, --black-and-white        Black and white only",
                                        "-e, --exclude-drawing-sheet  No drawing sheet",
                                        '--default-font               Default font name [nargs=0..1] [default: "KiCad Font"]',
                                        "-n, --no-background-color    Avoid setting a background color (regardless of theme)",
                                        '--pages                      List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="python-bom",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: python-bom [--help] [--output OUTPUT_FILE] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export the legacy BOM XML format used in the schematic editor with Python scripts",
                                    lines=[
                                        "Export the legacy BOM XML format used in the schematic editor with Python scripts"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE    Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help    Shows help message and exits",
                                        '-o, --output  Output file [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                        ParserL1.Command(
                            command="svg",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: svg [--help] [--output OUTPUT_DIR] [--drawing-sheet SHEET_PATH] [--define-var KEY=VALUE] [--theme THEME_NAME] [--black-and-white] [--exclude-drawing-sheet] [--default-font VAR] [--no-background-color] [--pages PAGE_LIST] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Export SVG", lines=["Export SVG"]
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE                   Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help                   Shows help message and exits",
                                        '-o, --output                 Output directory [nargs=0..1] [default: ""]',
                                        '--drawing-sheet              Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]',
                                        "-D, --define-var             Overrides or adds project variables, can be used multiple times to declare multiple variables.",
                                        "Use in the format of '--define-var key=value' or '-D key=value' [nargs=0..1] [default: {}]",
                                        '-t, --theme                  Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]',
                                        "-b, --black-and-white        Black and white only",
                                        "-e, --exclude-drawing-sheet  No drawing sheet",
                                        '--default-font               Default font name [nargs=0..1] [default: "KiCad Font"]',
                                        "-n, --no-background-color    Avoid setting a background color (regardless of theme)",
                                        '--pages                      List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]',
                                    ],
                                ),
                            ],
                            subcommands=[],
                        ),
                    ],
                ),
            ],
        ),
        ParserL1.Command(
            command="sym",
            sections=[
                ParserL1.Section(
                    name="Usage", lines=["Usage: sym [--help] {export,upgrade}"]
                ),
                ParserL1.Section(
                    name="Symbol and Symbol Libraries",
                    lines=["Symbol and Symbol Libraries"],
                ),
                ParserL1.Section(
                    name="Optional arguments",
                    lines=[
                        "Optional arguments:",
                        "-h, --help  Shows help message and exits",
                    ],
                ),
                ParserL1.Section(
                    name="Subcommands",
                    lines=[
                        "Subcommands:",
                        "export     Export utilities (svg)",
                        "upgrade    Upgrades the symbol library to the current kicad version format",
                    ],
                ),
            ],
            subcommands=[
                ParserL1.Command(
                    command="export",
                    sections=[
                        ParserL1.Section(
                            name="Usage", lines=["Usage: export [--help] {svg}"]
                        ),
                        ParserL1.Section(
                            name="Export utilities (svg)",
                            lines=["Export utilities (svg)"],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help  Shows help message and exits",
                            ],
                        ),
                        ParserL1.Section(
                            name="Subcommands",
                            lines=[
                                "Subcommands:",
                                "svg        Exports the symbol or entire symbol library to SVG",
                            ],
                        ),
                    ],
                    subcommands=[
                        ParserL1.Command(
                            command="svg",
                            sections=[
                                ParserL1.Section(
                                    name="Usage",
                                    lines=[
                                        "Usage: svg [--help] [--output OUTPUT_DIR] [--theme THEME_NAME] [--symbol SYMBOL] [--black-and-white] [--include-hidden-pins] [--include-hidden-fields] INPUT_FILE"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Exports the symbol or entire symbol library to SVG",
                                    lines=[
                                        "Exports the symbol or entire symbol library to SVG"
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Positional arguments",
                                    lines=[
                                        "Positional arguments:",
                                        "INPUT_FILE               Input file",
                                    ],
                                ),
                                ParserL1.Section(
                                    name="Optional arguments",
                                    lines=[
                                        "Optional arguments:",
                                        "-h, --help               Shows help message and exits",
                                        '-o, --output             Output directory [nargs=0..1] [default: ""]',
                                        '-t, --theme              Color theme to use (will default to symbol editor settings) [nargs=0..1] [default: ""]',
                                        '-s, --symbol             Specific symbol to export within the library [nargs=0..1] [default: ""]',
                                        "--black-and-white        Black and white only",
                                        "--include-hidden-pins    Include hidden pins",
                                        "--include-hidden-fields  Include hidden fields",
                                    ],
                                ),
                            ],
                            subcommands=[],
                        )
                    ],
                ),
                ParserL1.Command(
                    command="upgrade",
                    sections=[
                        ParserL1.Section(
                            name="Usage",
                            lines=[
                                "Usage: upgrade [--help] [--output OUTPUT_FILE] [--force] INPUT_FILE"
                            ],
                        ),
                        ParserL1.Section(
                            name="Upgrades the symbol library to the current kicad version format",
                            lines=[
                                "Upgrades the symbol library to the current kicad version format"
                            ],
                        ),
                        ParserL1.Section(
                            name="Positional arguments",
                            lines=["Positional arguments:", "INPUT_FILE    Input file"],
                        ),
                        ParserL1.Section(
                            name="Optional arguments",
                            lines=[
                                "Optional arguments:",
                                "-h, --help    Shows help message and exits",
                                '-o, --output  Output file [nargs=0..1] [default: ""]',
                                "--force       Forces the symbol library to be resaved regardless of versioning",
                            ],
                        ),
                    ],
                    subcommands=[],
                ),
            ],
        ),
        ParserL1.Command(
            command="version",
            sections=[
                ParserL1.Section(
                    name="Usage", lines=["Usage: version [--help] [--format VAR]"]
                ),
                ParserL1.Section(
                    name="Reports the version info in various formats",
                    lines=["Reports the version info in various formats"],
                ),
                ParserL1.Section(
                    name="Optional arguments",
                    lines=[
                        "Optional arguments:",
                        "-h, --help  Shows help message and exits",
                        '--format    version info format (plain, commit, about) [nargs=0..1] [default: "plain"]',
                    ],
                ),
            ],
            subcommands=[],
        ),
    ],
)
