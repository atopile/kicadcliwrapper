# This file is part of the faebryk project
# SPDX-License-Identifier: MIT


from dataclasses import dataclass
from subprocess import check_output

from kicadcliwrapper.generated.kicad_cli_l2 import kicad_cli_l2
from kicadcliwrapper.lib import run_command


@dataclass
class kicad_cli:
    """
    Args:
        a_version: prints version information and exits
        help: Shows help message and exits
    """

    cmd: "fp | pcb | sch | sym | version"
    # Arguments (Required)
    # Arguments (Optional)
    # Flags
    a_version: bool = False
    help: bool = False

    # Commands
    @dataclass
    class fp:
        """
        Args:
            help: Shows help message and exits
        """

        cmd: "export | upgrade"
        # Arguments (Required)
        # Arguments (Optional)
        # Flags
        help: bool = False

        # Commands
        @dataclass
        class export:
            """
            Args:
                help: Shows help message and exits
            """

            cmd: "svg"
            # Arguments (Required)
            # Arguments (Optional)
            # Flags
            help: bool = False

            # Commands
            @dataclass
            class svg:
                """
                Args:
                    INPUT_DIR: Input directory
                    output: Output directory [nargs=0..1] [default: ""]
                    layers: Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to footprint editor settings) [nargs=0..1] [default: ""]
                    footprint: Specific footprint to export within the library [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                """

                # Arguments (Required)
                INPUT_DIR: str
                # Arguments (Optional)
                output: str | None = None
                layers: str | None = None
                define_var: str | None = None
                theme: str | None = None
                footprint: str | None = None
                # Flags
                help: bool = False
                black_and_white: bool = False

        @dataclass
        class upgrade:
            """
            Args:
                INPUT_DIR: Input directory
                output: Output directory [nargs=0..1] [default: ""]
                help: Shows help message and exits
                force: Forces the footprint library to be resaved regardless of versioning
            """

            # Arguments (Required)
            INPUT_DIR: str
            # Arguments (Optional)
            output: str | None = None
            # Flags
            help: bool = False
            force: bool = False

    @dataclass
    class pcb:
        """
        Args:
            help: Shows help message and exits
        """

        cmd: "drc | export"
        # Arguments (Required)
        # Arguments (Optional)
        # Flags
        help: bool = False

        # Commands
        @dataclass
        class drc:
            """
            Args:
                INPUT_FILE: Input file
                output: Output file [nargs=0..1] [default: ""]
                define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                format: Output file format, options: json, report [nargs=0..1] [default: "report"]
                units: Report units; valid options: in, mm, mils [nargs=0..1] [default: "mm"]
                help: Shows help message and exits
                all_track_errors: Report all errors for each track
                schematic_parity: Test for parity between PCB and schematic
                severity_all: Report all DRC violations, this is equivalent to including all the other severity arguments
                severity_error: Report all DRC error level violations, this can be combined with the other severity arguments
                severity_warning: Report all DRC warning level violations, this can be combined with the other severity arguments
                severity_exclusions: Report all excluded DRC violations, this can be combined with the other severity arguments
                exit_code_violations: Return a nonzero exit code if DRC violations exist
            """

            # Arguments (Required)
            INPUT_FILE: str
            # Arguments (Optional)
            output: str | None = None
            define_var: str | None = None
            format: str | None = None
            units: str | None = None
            # Flags
            help: bool = False
            all_track_errors: bool = False
            schematic_parity: bool = False
            severity_all: bool = False
            severity_error: bool = False
            severity_warning: bool = False
            severity_exclusions: bool = False
            exit_code_violations: bool = False

        @dataclass
        class export:
            """
            Args:
                help: Shows help message and exits
            """

            cmd: "drill | dxf | gerber | gerbers | glb | ipc2581 | pdf | pos | step | svg | vrml"
            # Arguments (Required)
            # Arguments (Optional)
            # Flags
            help: bool = False

            # Commands
            @dataclass
            class drill:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    format: Valid options excellon, gerber. [nargs=0..1] [default: "excellon"]
                    drill_origin: Valid options are: absolute,plot [nargs=0..1] [default: "absolute"]
                    excellon_zeros_format: Valid options are: decimal,suppressleading,suppresstrailing,keep. [nargs=0..1] [default: "decimal"]
                    excellon_oval_format: Valid options are: route,alternate. [nargs=0..1] [default: "alternate"]
                    excellon_units: Output units, valid options:in,mm [nargs=0..1] [default: "mm"]
                    map_format: Valid options: pdf,gerberx2,ps,dxf,svg [nargs=0..1] [default: "pdf"]
                    gerber_precision: Precision of Gerber coordinates (5 or 6) [nargs=0..1] [default: 6]
                    help: Shows help message and exits
                    excellon_mirror_y: Mirror Y axis
                    excellon_min_header: Minimal header
                    excellon_separate_th: Generate independent files for NPTH and PTH holes
                    generate_map: Generate map / summary of drill hits
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                format: str | None = None
                drill_origin: str | None = None
                excellon_zeros_format: str | None = None
                excellon_oval_format: str | None = None
                excellon_units: str | None = None
                map_format: str | None = None
                gerber_precision: str | None = None
                # Flags
                help: bool = False
                excellon_mirror_y: bool = False
                excellon_min_header: bool = False
                excellon_separate_th: bool = False
                generate_map: bool = False

            @dataclass
            class dxf:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    layers: Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    output_units: Output units, valid options: mm, in [nargs=0..1] [default: "in"]
                    help: Shows help message and exits
                    exclude_refdes: Exclude the reference designator text
                    exclude_value: Exclude the value text
                    use_contours: Plot graphic items using their contours
                    include_border_title: Include the border and title block
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                layers: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                output_units: str | None = None
                # Flags
                help: bool = False
                exclude_refdes: bool = False
                exclude_value: bool = False
                use_contours: bool = False
                include_border_title: bool = False

            @dataclass
            class gerber:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    layers: Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    precision: Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]
                    help: Shows help message and exits
                    exclude_refdes: Exclude the reference designator text
                    exclude_value: Exclude the value text
                    include_border_title: Include the border and title block
                    no_x2: Do not use the extended X2 format
                    no_netlist: Do not generate netlist attributes
                    subtract_soldermask: Subtract soldermask from silkscreen
                    disable_aperture_macros: Disable aperture macros
                    use_drill_file_origin: Use drill/place file origin
                    no_protel_ext: Use KiCad Gerber file extension
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                layers: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                precision: str | None = None
                # Flags
                help: bool = False
                exclude_refdes: bool = False
                exclude_value: bool = False
                include_border_title: bool = False
                no_x2: bool = False
                no_netlist: bool = False
                subtract_soldermask: bool = False
                disable_aperture_macros: bool = False
                use_drill_file_origin: bool = False
                no_protel_ext: bool = False

            @dataclass
            class gerbers:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    layers: Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    precision: Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]
                    common_layers: Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    exclude_refdes: Exclude the reference designator text
                    exclude_value: Exclude the value text
                    include_border_title: Include the border and title block
                    no_x2: Do not use the extended X2 format
                    no_netlist: Do not generate netlist attributes
                    subtract_soldermask: Subtract soldermask from silkscreen
                    disable_aperture_macros: Disable aperture macros
                    use_drill_file_origin: Use drill/place file origin
                    no_protel_ext: Use KiCad Gerber file extension
                    board_plot_params: Use the Gerber plot settings already configured in the board file
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                layers: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                precision: str | None = None
                common_layers: str | None = None
                # Flags
                help: bool = False
                exclude_refdes: bool = False
                exclude_value: bool = False
                include_border_title: bool = False
                no_x2: bool = False
                no_netlist: bool = False
                subtract_soldermask: bool = False
                disable_aperture_macros: bool = False
                use_drill_file_origin: bool = False
                no_protel_ext: bool = False
                board_plot_params: bool = False

            @dataclass
            class glb:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    min_distance: Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]
                    user_origin: User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    force: Overwrite output file
                    grid_origin: Use Grid Origin for output origin
                    drill_origin: Use Drill Origin for output origin
                    no_unspecified: Exclude 3D models for components with 'Unspecified' footprint type
                    no_dnp: Exclude 3D models for components with 'Do not populate' attribute
                    subst_models: Substitute STEP or IGS models with the same name in place of VRML models
                    board_only: Only generate a board with no components
                    include_tracks: Export tracks
                    include_zones: Export zones
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                define_var: str | None = None
                min_distance: str | None = None
                user_origin: str | None = None
                # Flags
                help: bool = False
                force: bool = False
                grid_origin: bool = False
                drill_origin: bool = False
                no_unspecified: bool = False
                no_dnp: bool = False
                subst_models: bool = False
                board_only: bool = False
                include_tracks: bool = False
                include_zones: bool = False

            @dataclass
            class ipc2581:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    precision: Precision [nargs=0..1] [default: 3]
                    version: IPC2581 standard version [nargs=0..1] [default: "C"]
                    units: Units [nargs=0..1] [default: "mm"]
                    bom_col_int_id: Name of the part field to use for the Bill of Material Internal Id Column [nargs=0..1] [default: ""]
                    bom_col_mfg_pn: Name of the part field to use for the Bill of Material Manufacturer Part Number Column [nargs=0..1] [default: ""]
                    bom_col_mfg: Name of the part field to use for the Bill of Material Manufacturer Column [nargs=0..1] [default: ""]
                    bom_col_dist_pn: Name of the part field to use for the Bill of Material Distributor Part Number Column [nargs=0..1] [default: ""]
                    bom_col_dist: Name to insert into Bill of Material Distributor Column [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    compress: Compress the output
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                precision: str | None = None
                version: str | None = None
                units: str | None = None
                bom_col_int_id: str | None = None
                bom_col_mfg_pn: str | None = None
                bom_col_mfg: str | None = None
                bom_col_dist_pn: str | None = None
                bom_col_dist: str | None = None
                # Flags
                help: bool = False
                compress: bool = False

            @dataclass
            class pdf:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    layers: Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to PCB Editor settings) [nargs=0..1] [default: ""]
                    drill_shape_opt: Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]
                    help: Shows help message and exits
                    mirror: Mirror the board (useful for trying to show bottom layers)
                    exclude_refdes: Exclude the reference designator text
                    exclude_value: Exclude the value text
                    include_border_title: Include the border and title block
                    negative: Plot as negative (useful for directly etching from the export)
                    black_and_white: Black and white only
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                layers: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                theme: str | None = None
                drill_shape_opt: str | None = None
                # Flags
                help: bool = False
                mirror: bool = False
                exclude_refdes: bool = False
                exclude_value: bool = False
                include_border_title: bool = False
                negative: bool = False
                black_and_white: bool = False

            @dataclass
            class pos:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    side: Valid options: front,back,both. Gerber format only supports "front" or "back". [nargs=0..1] [default: "both"]
                    format: Valid options: ascii,csv,gerber [nargs=0..1] [default: "ascii"]
                    units: Output units; ascii or csv format only; valid options: in,mm [nargs=0..1] [default: "in"]
                    help: Shows help message and exits
                    bottom_negate_x: Use negative X coordinates for footprints on bottom layer (ascii or csv formats only)
                    use_drill_file_origin: Use drill/place file origin (ascii or csv only)
                    smd_only: Include only SMD footprints (ascii or csv only)
                    exclude_fp_th: Exclude all footprints with through-hole pads (ascii or csv only)
                    exclude_dnp: Exclude all footprints with the Do Not Populate flag set
                    gerber_board_edge: Include board edge layer (Gerber only)
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                side: str | None = None
                format: str | None = None
                units: str | None = None
                # Flags
                help: bool = False
                bottom_negate_x: bool = False
                use_drill_file_origin: bool = False
                smd_only: bool = False
                exclude_fp_th: bool = False
                exclude_dnp: bool = False
                gerber_board_edge: bool = False

            @dataclass
            class step:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    min_distance: Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]
                    user_origin: User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    force: Overwrite output file
                    grid_origin: Use Grid Origin for output origin
                    drill_origin: Use Drill Origin for output origin
                    no_unspecified: Exclude 3D models for components with 'Unspecified' footprint type
                    no_dnp: Exclude 3D models for components with 'Do not populate' attribute
                    subst_models: Substitute STEP or IGS models with the same name in place of VRML models
                    board_only: Only generate a board with no components
                    include_tracks: Export tracks
                    include_zones: Export zones
                    no_optimize_step: Do not optimize STEP file (enables writing parametric curves)
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                define_var: str | None = None
                min_distance: str | None = None
                user_origin: str | None = None
                # Flags
                help: bool = False
                force: bool = False
                grid_origin: bool = False
                drill_origin: bool = False
                no_unspecified: bool = False
                no_dnp: bool = False
                subst_models: bool = False
                board_only: bool = False
                include_tracks: bool = False
                include_zones: bool = False
                no_optimize_step: bool = False

            @dataclass
            class svg:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    layers: Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to PCB editor settings) [nargs=0..1] [default: ""]
                    page_size_mode: Set page sizing mode (0 = page with frame and title block, 1 = current page size, 2 = board area only) [nargs=0..1] [default: 0]
                    drill_shape_opt: Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]
                    help: Shows help message and exits
                    mirror: Mirror the board (useful for trying to show bottom layers)
                    negative: Plot as negative (useful for directly etching from the export)
                    black_and_white: Black and white only
                    exclude_drawing_sheet: No drawing sheet
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                layers: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                theme: str | None = None
                page_size_mode: str | None = None
                drill_shape_opt: str | None = None
                # Flags
                help: bool = False
                mirror: bool = False
                negative: bool = False
                black_and_white: bool = False
                exclude_drawing_sheet: bool = False

            @dataclass
            class vrml:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    user_origin: User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]
                    units: Output units; valid options: mm, m, in, tenths [nargs=0..1] [default: "in"]
                    models_dir: Name of folder to create and store 3d models in, if not specified or empty, the models will be embedded in main exported VRML file [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    force: Overwrite output file
                    models_relative: Used with --models-dir to output relative paths in the resulting file
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                define_var: str | None = None
                user_origin: str | None = None
                units: str | None = None
                models_dir: str | None = None
                # Flags
                help: bool = False
                force: bool = False
                models_relative: bool = False

    @dataclass
    class sch:
        """
        Args:
            help: Shows help message and exits
        """

        cmd: "erc | export"
        # Arguments (Required)
        # Arguments (Optional)
        # Flags
        help: bool = False

        # Commands
        @dataclass
        class erc:
            """
            Args:
                INPUT_FILE: Input file
                output: Output file [nargs=0..1] [default: ""]
                define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                format: Output file format, options: json, report [nargs=0..1] [default: "report"]
                units: Report units; valid options: in, mm, mils [nargs=0..1] [default: "mm"]
                help: Shows help message and exits
                severity_all: Report all ERC violations, this is equivalent to including all the other severity arguments
                severity_error: Report all ERC error level violations, this can be combined with the other severity arguments
                severity_warning: Report all ERC warning level violations, this can be combined with the other severity arguments
                severity_exclusions: Report all excluded ERC violations, this can be combined with the other severity arguments
                exit_code_violations: Return a nonzero exit code if ERC violations exist
            """

            # Arguments (Required)
            INPUT_FILE: str
            # Arguments (Optional)
            output: str | None = None
            define_var: str | None = None
            format: str | None = None
            units: str | None = None
            # Flags
            help: bool = False
            severity_all: bool = False
            severity_error: bool = False
            severity_warning: bool = False
            severity_exclusions: bool = False
            exit_code_violations: bool = False

        @dataclass
        class export:
            """
            Args:
                help: Shows help message and exits
            """

            cmd: "bom | dxf | hpgl | netlist | pdf | ps | python_bom | svg"
            # Arguments (Required)
            # Arguments (Optional)
            # Flags
            help: bool = False

            # Commands
            @dataclass
            class bom:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    preset: Use a named BOM preset setting from the schematic, e.g. "Grouped By Value". [nargs=0..1] [default: ""]
                    format_preset: Use a named BOM format preset setting from the schematic, e.g. CSV. [nargs=0..1] [default: ""]
                    fields: An ordered list of fields to export. See documentation for special substitutions. [nargs=0..1] [default: "Reference,Value,Footprint,${QUANTITY},${DNP}"]
                    labels: An ordered list of labels to apply the exported fields. [nargs=0..1] [default: "Refs,Value,Footprint,Qty,DNP"]
                    group_by: Fields to group references by when field values match. [nargs=0..1] [default: ""]
                    sort_field: Field name to sort by. [nargs=0..1] [default: "Reference"]
                    filter: Filter string to remove output lines. [nargs=0..1] [default: ""]
                    field_delimiter: Separator between output fields/columns. [nargs=0..1] [default: ","]
                    string_delimiter: Character to surround fields with. [nargs=0..1] [default: " " "]
                    ref_delimiter: Character to place between individual references. [nargs=0..1] [default: ","]
                    ref_range_delimiter: Character to place in ranges of references. Leave blank for no ranges. [nargs=0..1] [default: "-"]
                    help: Shows help message and exits
                    sort_asc: Sort ascending (true) or descending (false).
                    exclude_dnp: Exclude symbols marked Do-Not-Populate.
                    keep_tabs: Keep tab characters from input fields. Stripped by default.
                    keep_line_breaks: Keep line break characters from input fields. Stripped by default.
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                preset: str | None = None
                format_preset: str | None = None
                fields: str | None = None
                labels: str | None = None
                group_by: str | None = None
                sort_field: str | None = None
                filter: str | None = None
                field_delimiter: str | None = None
                string_delimiter: str | None = None
                ref_delimiter: str | None = None
                ref_range_delimiter: str | None = None
                # Flags
                help: bool = False
                sort_asc: bool = False
                exclude_dnp: bool = False
                keep_tabs: bool = False
                keep_line_breaks: bool = False

            @dataclass
            class dxf:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                    exclude_drawing_sheet: No drawing sheet
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                theme: str | None = None
                pages: str | None = None
                # Flags
                help: bool = False
                black_and_white: bool = False
                exclude_drawing_sheet: bool = False

            @dataclass
            class hpgl:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    pen_size: Pen size [mm] [nargs=0..1] [default: 0.5]
                    origin: Origin and scale: 0 bottom left, 1 centered, 2 page fit, 3 content fit [nargs=0..1] [default: 1]
                    help: Shows help message and exits
                    exclude_drawing_sheet: No drawing sheet
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                pages: str | None = None
                pen_size: str | None = None
                origin: str | None = None
                # Flags
                help: bool = False
                exclude_drawing_sheet: bool = False

            @dataclass
            class netlist:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    format: Netlist output format, valid options: kicadsexpr, kicadxml, cadstar, orcadpcb2, spice, spicemodel [nargs=0..1] [default: "kicadsexpr"]
                    help: Shows help message and exits
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                format: str | None = None
                # Flags
                help: bool = False

            @dataclass
            class pdf:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                    exclude_drawing_sheet: No drawing sheet
                    exclude_pdf_property_popups: Do not generate property popups in PDF
                    no_background_color: Avoid setting a background color (regardless of theme)
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                theme: str | None = None
                pages: str | None = None
                # Flags
                help: bool = False
                black_and_white: bool = False
                exclude_drawing_sheet: bool = False
                exclude_pdf_property_popups: bool = False
                no_background_color: bool = False

            @dataclass
            class ps:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                    exclude_drawing_sheet: No drawing sheet
                    no_background_color: Avoid setting a background color (regardless of theme)
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                theme: str | None = None
                pages: str | None = None
                # Flags
                help: bool = False
                black_and_white: bool = False
                exclude_drawing_sheet: bool = False
                no_background_color: bool = False

            @dataclass
            class python_bom:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                # Flags
                help: bool = False

            @dataclass
            class svg:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                    exclude_drawing_sheet: No drawing sheet
                    no_background_color: Avoid setting a background color (regardless of theme)
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                drawing_sheet: str | None = None
                define_var: str | None = None
                theme: str | None = None
                pages: str | None = None
                # Flags
                help: bool = False
                black_and_white: bool = False
                exclude_drawing_sheet: bool = False
                no_background_color: bool = False

    @dataclass
    class sym:
        """
        Args:
            help: Shows help message and exits
        """

        cmd: "export | upgrade"
        # Arguments (Required)
        # Arguments (Optional)
        # Flags
        help: bool = False

        # Commands
        @dataclass
        class export:
            """
            Args:
                help: Shows help message and exits
            """

            cmd: "svg"
            # Arguments (Required)
            # Arguments (Optional)
            # Flags
            help: bool = False

            # Commands
            @dataclass
            class svg:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    theme: Color theme to use (will default to symbol editor settings) [nargs=0..1] [default: ""]
                    symbol: Specific symbol to export within the library [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                    include_hidden_pins: Include hidden pins
                    include_hidden_fields: Include hidden fields
                """

                # Arguments (Required)
                INPUT_FILE: str
                # Arguments (Optional)
                output: str | None = None
                theme: str | None = None
                symbol: str | None = None
                # Flags
                help: bool = False
                black_and_white: bool = False
                include_hidden_pins: bool = False
                include_hidden_fields: bool = False

        @dataclass
        class upgrade:
            """
            Args:
                INPUT_FILE: Input file
                output: Output file [nargs=0..1] [default: ""]
                help: Shows help message and exits
                force: Forces the symbol library to be resaved regardless of versioning
            """

            # Arguments (Required)
            INPUT_FILE: str
            # Arguments (Optional)
            output: str | None = None
            # Flags
            help: bool = False
            force: bool = False

    @dataclass
    class version:
        """
        Args:
            format: version info format (plain, commit, about) [nargs=0..1] [default: "plain"]
            help: Shows help message and exits
        """

        # Arguments (Required)
        # Arguments (Optional)
        format: str | None = None
        # Flags
        help: bool = False

    def exec(self):
        return run_command(kicad_cli_l2, self)
