# This file is part of the faebryk project
# SPDX-License-Identifier: MIT


from dataclasses import dataclass

from kicadcliwrapper.generated.kicad_cli_l2 import kicad_cli_l2
from kicadcliwrapper.lib import run_parser_command


@dataclass
class kicad_cli:
    """
    Args:
        a_version: prints version information and exits
        help: Shows help message and exits
    """

    cmd: "fp | jobset | pcb | sch | sym | version"
    # Arguments (Required)
    # Arguments (Optional)
    # Flags
    a_version: bool = False
    """prints version information and exits"""
    help: bool = False
    """Shows help message and exits"""

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
        """Shows help message and exits"""

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
            """Shows help message and exits"""

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
                    sketch_pads_on_fab_layers: Draw pad outlines and their numbers on front and back fab layers
                    hide_DNP_footprints_on_fab_layers: Don't plot text & graphics of DNP footprints on fab layers
                    sketch_DNP_footprints_on_fab_layers: Plot graphics of DNP footprints in sketch mode on fab layers
                    crossout_DNP_footprints_on_fab_layers: Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators
                    black_and_white: Black and white only
                """

                # Arguments (Required)
                INPUT_DIR: str
                """Input directory"""
                # Arguments (Optional)
                output: str | None = None
                """Output directory [nargs=0..1] [default: ""]"""
                layers: str | None = None
                """Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                theme: str | None = None
                """Color theme to use (will default to footprint editor settings) [nargs=0..1] [default: ""]"""
                footprint: str | None = None
                """Specific footprint to export within the library [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                sketch_pads_on_fab_layers: bool = False
                """Draw pad outlines and their numbers on front and back fab layers"""
                hide_DNP_footprints_on_fab_layers: bool = False
                """Don't plot text & graphics of DNP footprints on fab layers"""
                sketch_DNP_footprints_on_fab_layers: bool = False
                """Plot graphics of DNP footprints in sketch mode on fab layers"""
                crossout_DNP_footprints_on_fab_layers: bool = False
                """Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators"""
                black_and_white: bool = False
                """Black and white only"""

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
            """Input directory"""
            # Arguments (Optional)
            output: str | None = None
            """Output directory [nargs=0..1] [default: ""]"""
            # Flags
            help: bool = False
            """Shows help message and exits"""
            force: bool = False
            """Forces the footprint library to be resaved regardless of versioning"""

    @dataclass
    class jobset:
        """
        Args:
            help: Shows help message and exits
        """

        cmd: "run"
        # Arguments (Required)
        # Arguments (Optional)
        # Flags
        help: bool = False
        """Shows help message and exits"""

        # Commands
        @dataclass
        class run:
            """
            Args:
                INPUT_FILE: Input file
                file: Jobset file to be run [nargs=0..1] [default: ""]
                output: Jobset file output to generate, leave blank for all outputs defined in the jobset [nargs=0..1] [default: ""]
                help: Shows help message and exits
                stop_on_error: Stops processing jobs as they are executed sequentially on the first failure of a job
            """

            # Arguments (Required)
            INPUT_FILE: str
            """Input file"""
            # Arguments (Optional)
            file: str | None = None
            """Jobset file to be run [nargs=0..1] [default: ""]"""
            output: str | None = None
            """Jobset file output to generate, leave blank for all outputs defined in the jobset [nargs=0..1] [default: ""]"""
            # Flags
            help: bool = False
            """Shows help message and exits"""
            stop_on_error: bool = False
            """Stops processing jobs as they are executed sequentially on the first failure of a job"""

    @dataclass
    class pcb:
        """
        Args:
            help: Shows help message and exits
        """

        cmd: "drc | export | render"
        # Arguments (Required)
        # Arguments (Optional)
        # Flags
        help: bool = False
        """Shows help message and exits"""

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
            """Input file"""
            # Arguments (Optional)
            output: str | None = None
            """Output file [nargs=0..1] [default: ""]"""
            define_var: str | None = None
            """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
            format: str | None = None
            """Output file format, options: json, report [nargs=0..1] [default: "report"]"""
            units: str | None = None
            """Report units; valid options: in, mm, mils [nargs=0..1] [default: "mm"]"""
            # Flags
            help: bool = False
            """Shows help message and exits"""
            all_track_errors: bool = False
            """Report all errors for each track"""
            schematic_parity: bool = False
            """Test for parity between PCB and schematic"""
            severity_all: bool = False
            """Report all DRC violations, this is equivalent to including all the other severity arguments"""
            severity_error: bool = False
            """Report all DRC error level violations, this can be combined with the other severity arguments"""
            severity_warning: bool = False
            """Report all DRC warning level violations, this can be combined with the other severity arguments"""
            severity_exclusions: bool = False
            """Report all excluded DRC violations, this can be combined with the other severity arguments"""
            exit_code_violations: bool = False
            """Return a nonzero exit code if DRC violations exist"""

        @dataclass
        class export:
            """
            Args:
                help: Shows help message and exits
            """

            cmd: "brep | drill | dxf | gencad | gerber | gerbers | glb | ipc2581 | ipcd356 | odb | pdf | ply | pos | step | stl | svg | vrml | xao"
            # Arguments (Required)
            # Arguments (Optional)
            # Flags
            help: bool = False
            """Shows help message and exits"""

            # Commands
            @dataclass
            class brep:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    component_filter: Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]
                    min_distance: Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]
                    net_filter: Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]
                    user_origin: User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    force: Overwrite output file
                    no_unspecified: Exclude 3D models for components with 'Unspecified' footprint type
                    no_dnp: Exclude 3D models for components with 'Do not populate' attribute
                    grid_origin: Use Grid Origin for output origin
                    drill_origin: Use Drill Origin for output origin
                    subst_models: Substitute STEP or IGS models with the same name in place of VRML models
                    board_only: Only generate a board with no components
                    cut_vias_in_body: Cut via holes in board body even if conductor layers are not exported.
                    no_board_body: Exclude board body
                    no_components: Exclude 3D models for components
                    include_tracks: Export tracks and vias
                    include_pads: Export pads
                    include_zones: Export zones
                    include_inner_copper: Export elements on inner copper layers
                    include_silkscreen: Export silkscreen graphics as a set of flat faces
                    include_soldermask: Export soldermask layers as a set of flat faces
                    fuse_shapes: Fuse overlapping geometry together
                    fill_all_vias: Don't cut via holes in conductor layers.
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                component_filter: str | None = None
                """Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]"""
                min_distance: str | None = None
                """Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]"""
                net_filter: str | None = None
                """Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]"""
                user_origin: str | None = None
                """User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                force: bool = False
                """Overwrite output file"""
                no_unspecified: bool = False
                """Exclude 3D models for components with 'Unspecified' footprint type"""
                no_dnp: bool = False
                """Exclude 3D models for components with 'Do not populate' attribute"""
                grid_origin: bool = False
                """Use Grid Origin for output origin"""
                drill_origin: bool = False
                """Use Drill Origin for output origin"""
                subst_models: bool = False
                """Substitute STEP or IGS models with the same name in place of VRML models"""
                board_only: bool = False
                """Only generate a board with no components"""
                cut_vias_in_body: bool = False
                """Cut via holes in board body even if conductor layers are not exported."""
                no_board_body: bool = False
                """Exclude board body"""
                no_components: bool = False
                """Exclude 3D models for components"""
                include_tracks: bool = False
                """Export tracks and vias"""
                include_pads: bool = False
                """Export pads"""
                include_zones: bool = False
                """Export zones"""
                include_inner_copper: bool = False
                """Export elements on inner copper layers"""
                include_silkscreen: bool = False
                """Export silkscreen graphics as a set of flat faces"""
                include_soldermask: bool = False
                """Export soldermask layers as a set of flat faces"""
                fuse_shapes: bool = False
                """Fuse overlapping geometry together"""
                fill_all_vias: bool = False
                """Don't cut via holes in conductor layers."""

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
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output directory [nargs=0..1] [default: ""]"""
                format: str | None = None
                """Valid options excellon, gerber. [nargs=0..1] [default: "excellon"]"""
                drill_origin: str | None = None
                """Valid options are: absolute,plot [nargs=0..1] [default: "absolute"]"""
                excellon_zeros_format: str | None = None
                """Valid options are: decimal,suppressleading,suppresstrailing,keep. [nargs=0..1] [default: "decimal"]"""
                excellon_oval_format: str | None = None
                """Valid options are: route,alternate. [nargs=0..1] [default: "alternate"]"""
                excellon_units: str | None = None
                """Output units, valid options:in,mm [nargs=0..1] [default: "mm"]"""
                map_format: str | None = None
                """Valid options: pdf,gerberx2,ps,dxf,svg [nargs=0..1] [default: "pdf"]"""
                gerber_precision: str | None = None
                """Precision of Gerber coordinates (5 or 6) [nargs=0..1] [default: 6]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                excellon_mirror_y: bool = False
                """Mirror Y axis"""
                excellon_min_header: bool = False
                """Minimal header"""
                excellon_separate_th: bool = False
                """Generate independent files for NPTH and PTH holes"""
                generate_map: bool = False
                """Generate map / summary of drill hits"""

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
                    drill_shape_opt: Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]
                    common_layers: Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    exclude_refdes: Exclude the reference designator text
                    exclude_value: Exclude the value text
                    sketch_pads_on_fab_layers: Draw pad outlines and their numbers on front and back fab layers
                    hide_DNP_footprints_on_fab_layers: Don't plot text & graphics of DNP footprints on fab layers
                    sketch_DNP_footprints_on_fab_layers: Plot graphics of DNP footprints in sketch mode on fab layers
                    crossout_DNP_footprints_on_fab_layers: Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators
                    subtract_soldermask: Subtract soldermask from silkscreen
                    use_contours: Plot graphic items using their contours
                    use_drill_origin: Plot using the drill/place file origin
                    include_border_title: Include the border and title block
                    mode_single: Generates a single file with the output arg path acting as the complete directory and filename path. COMMON_LAYER_LIST does not function in this mode. Instead LAYER_LIST controls all layers plotted.
                    mode_multi: Generates one or more files with behavior similar to the KiCad GUI plotting. The given output path specifies a directory in which files may be output.
                    plot_invisible_text: Deprecated.  Has no effect.
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                layers: str | None = None
                """Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                output_units: str | None = None
                """Output units, valid options: mm, in [nargs=0..1] [default: "in"]"""
                drill_shape_opt: str | None = None
                """Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]"""
                common_layers: str | None = None
                """Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                exclude_refdes: bool = False
                """Exclude the reference designator text"""
                exclude_value: bool = False
                """Exclude the value text"""
                sketch_pads_on_fab_layers: bool = False
                """Draw pad outlines and their numbers on front and back fab layers"""
                hide_DNP_footprints_on_fab_layers: bool = False
                """Don't plot text & graphics of DNP footprints on fab layers"""
                sketch_DNP_footprints_on_fab_layers: bool = False
                """Plot graphics of DNP footprints in sketch mode on fab layers"""
                crossout_DNP_footprints_on_fab_layers: bool = False
                """Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators"""
                subtract_soldermask: bool = False
                """Subtract soldermask from silkscreen"""
                use_contours: bool = False
                """Plot graphic items using their contours"""
                use_drill_origin: bool = False
                """Plot using the drill/place file origin"""
                include_border_title: bool = False
                """Include the border and title block"""
                mode_single: bool = False
                """Generates a single file with the output arg path acting as the complete directory and filename path. COMMON_LAYER_LIST does not function in this mode. Instead LAYER_LIST controls all layers plotted."""
                mode_multi: bool = False
                """Generates one or more files with behavior similar to the KiCad GUI plotting. The given output path specifies a directory in which files may be output."""
                plot_invisible_text: bool = False
                """Deprecated.  Has no effect."""

            @dataclass
            class gencad:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    help: Shows help message and exits
                    flip_bottom_pads: Flip bottom footprint padstacks
                    unique_pins: Generate unique pin names
                    unique_footprints: Generate a new shape for each footprint instance (do not reuse shapes)
                    use_drill_origin: Use drill/place file origin as origin
                    store_origin_coord: Save the origin coordinates in the file
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                flip_bottom_pads: bool = False
                """Flip bottom footprint padstacks"""
                unique_pins: bool = False
                """Generate unique pin names"""
                unique_footprints: bool = False
                """Generate a new shape for each footprint instance (do not reuse shapes)"""
                use_drill_origin: bool = False
                """Use drill/place file origin as origin"""
                store_origin_coord: bool = False
                """Save the origin coordinates in the file"""

            @dataclass
            class gerber:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    layers: Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    common_layers: Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    precision: Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]
                    help: Shows help message and exits
                    exclude_refdes: Exclude the reference designator text
                    exclude_value: Exclude the value text
                    include_border_title: Include the border and title block
                    sketch_pads_on_fab_layers: Draw pad outlines and their numbers on front and back fab layers
                    hide_DNP_footprints_on_fab_layers: Don't plot text & graphics of DNP footprints on fab layers
                    sketch_DNP_footprints_on_fab_layers: Plot graphics of DNP footprints in sketch mode on fab layers
                    crossout_DNP_footprints_on_fab_layers: Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators
                    no_x2: Do not use the extended X2 format
                    no_netlist: Do not generate netlist attributes
                    subtract_soldermask: Subtract soldermask from silkscreen
                    disable_aperture_macros: Disable aperture macros
                    use_drill_file_origin: Use drill/place file origin
                    no_protel_ext: Use KiCad Gerber file extension
                    plot_invisible_text: Deprecated.  Has no effect.
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                layers: str | None = None
                """Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                common_layers: str | None = None
                """Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                precision: str | None = None
                """Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                exclude_refdes: bool = False
                """Exclude the reference designator text"""
                exclude_value: bool = False
                """Exclude the value text"""
                include_border_title: bool = False
                """Include the border and title block"""
                sketch_pads_on_fab_layers: bool = False
                """Draw pad outlines and their numbers on front and back fab layers"""
                hide_DNP_footprints_on_fab_layers: bool = False
                """Don't plot text & graphics of DNP footprints on fab layers"""
                sketch_DNP_footprints_on_fab_layers: bool = False
                """Plot graphics of DNP footprints in sketch mode on fab layers"""
                crossout_DNP_footprints_on_fab_layers: bool = False
                """Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators"""
                no_x2: bool = False
                """Do not use the extended X2 format"""
                no_netlist: bool = False
                """Do not generate netlist attributes"""
                subtract_soldermask: bool = False
                """Subtract soldermask from silkscreen"""
                disable_aperture_macros: bool = False
                """Disable aperture macros"""
                use_drill_file_origin: bool = False
                """Use drill/place file origin"""
                no_protel_ext: bool = False
                """Use KiCad Gerber file extension"""
                plot_invisible_text: bool = False
                """Deprecated.  Has no effect."""

            @dataclass
            class gerbers:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    layers: Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    common_layers: Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    precision: Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]
                    common_layers: Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    exclude_refdes: Exclude the reference designator text
                    exclude_value: Exclude the value text
                    include_border_title: Include the border and title block
                    sketch_pads_on_fab_layers: Draw pad outlines and their numbers on front and back fab layers
                    hide_DNP_footprints_on_fab_layers: Don't plot text & graphics of DNP footprints on fab layers
                    sketch_DNP_footprints_on_fab_layers: Plot graphics of DNP footprints in sketch mode on fab layers
                    crossout_DNP_footprints_on_fab_layers: Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators
                    no_x2: Do not use the extended X2 format
                    no_netlist: Do not generate netlist attributes
                    subtract_soldermask: Subtract soldermask from silkscreen
                    disable_aperture_macros: Disable aperture macros
                    use_drill_file_origin: Use drill/place file origin
                    no_protel_ext: Use KiCad Gerber file extension
                    plot_invisible_text: Deprecated.  Has no effect.
                    board_plot_params: Use the Gerber plot settings already configured in the board file
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                layers: str | None = None
                """Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                common_layers: str | None = None
                """Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                precision: str | None = None
                """Precision of Gerber coordinates, valid options: 5 or 6 [nargs=0..1] [default: 6]"""
                common_layers: str | None = None
                """Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                exclude_refdes: bool = False
                """Exclude the reference designator text"""
                exclude_value: bool = False
                """Exclude the value text"""
                include_border_title: bool = False
                """Include the border and title block"""
                sketch_pads_on_fab_layers: bool = False
                """Draw pad outlines and their numbers on front and back fab layers"""
                hide_DNP_footprints_on_fab_layers: bool = False
                """Don't plot text & graphics of DNP footprints on fab layers"""
                sketch_DNP_footprints_on_fab_layers: bool = False
                """Plot graphics of DNP footprints in sketch mode on fab layers"""
                crossout_DNP_footprints_on_fab_layers: bool = False
                """Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators"""
                no_x2: bool = False
                """Do not use the extended X2 format"""
                no_netlist: bool = False
                """Do not generate netlist attributes"""
                subtract_soldermask: bool = False
                """Subtract soldermask from silkscreen"""
                disable_aperture_macros: bool = False
                """Disable aperture macros"""
                use_drill_file_origin: bool = False
                """Use drill/place file origin"""
                no_protel_ext: bool = False
                """Use KiCad Gerber file extension"""
                plot_invisible_text: bool = False
                """Deprecated.  Has no effect."""
                board_plot_params: bool = False
                """Use the Gerber plot settings already configured in the board file"""

            @dataclass
            class glb:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    component_filter: Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]
                    min_distance: Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]
                    net_filter: Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]
                    user_origin: User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    force: Overwrite output file
                    no_unspecified: Exclude 3D models for components with 'Unspecified' footprint type
                    no_dnp: Exclude 3D models for components with 'Do not populate' attribute
                    grid_origin: Use Grid Origin for output origin
                    drill_origin: Use Drill Origin for output origin
                    subst_models: Substitute STEP or IGS models with the same name in place of VRML models
                    board_only: Only generate a board with no components
                    cut_vias_in_body: Cut via holes in board body even if conductor layers are not exported.
                    no_board_body: Exclude board body
                    no_components: Exclude 3D models for components
                    include_tracks: Export tracks and vias
                    include_pads: Export pads
                    include_zones: Export zones
                    include_inner_copper: Export elements on inner copper layers
                    include_silkscreen: Export silkscreen graphics as a set of flat faces
                    include_soldermask: Export soldermask layers as a set of flat faces
                    fuse_shapes: Fuse overlapping geometry together
                    fill_all_vias: Don't cut via holes in conductor layers.
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                component_filter: str | None = None
                """Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]"""
                min_distance: str | None = None
                """Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]"""
                net_filter: str | None = None
                """Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]"""
                user_origin: str | None = None
                """User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                force: bool = False
                """Overwrite output file"""
                no_unspecified: bool = False
                """Exclude 3D models for components with 'Unspecified' footprint type"""
                no_dnp: bool = False
                """Exclude 3D models for components with 'Do not populate' attribute"""
                grid_origin: bool = False
                """Use Grid Origin for output origin"""
                drill_origin: bool = False
                """Use Drill Origin for output origin"""
                subst_models: bool = False
                """Substitute STEP or IGS models with the same name in place of VRML models"""
                board_only: bool = False
                """Only generate a board with no components"""
                cut_vias_in_body: bool = False
                """Cut via holes in board body even if conductor layers are not exported."""
                no_board_body: bool = False
                """Exclude board body"""
                no_components: bool = False
                """Exclude 3D models for components"""
                include_tracks: bool = False
                """Export tracks and vias"""
                include_pads: bool = False
                """Export pads"""
                include_zones: bool = False
                """Export zones"""
                include_inner_copper: bool = False
                """Export elements on inner copper layers"""
                include_silkscreen: bool = False
                """Export silkscreen graphics as a set of flat faces"""
                include_soldermask: bool = False
                """Export soldermask layers as a set of flat faces"""
                fuse_shapes: bool = False
                """Fuse overlapping geometry together"""
                fill_all_vias: bool = False
                """Don't cut via holes in conductor layers."""

            @dataclass
            class ipc2581:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    precision: Precision [nargs=0..1] [default: 6]
                    version: IPC-2581 standard version [nargs=0..1] [default: "C"]
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
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                precision: str | None = None
                """Precision [nargs=0..1] [default: 6]"""
                version: str | None = None
                """IPC-2581 standard version [nargs=0..1] [default: "C"]"""
                units: str | None = None
                """Units [nargs=0..1] [default: "mm"]"""
                bom_col_int_id: str | None = None
                """Name of the part field to use for the Bill of Material Internal Id Column [nargs=0..1] [default: ""]"""
                bom_col_mfg_pn: str | None = None
                """Name of the part field to use for the Bill of Material Manufacturer Part Number Column [nargs=0..1] [default: ""]"""
                bom_col_mfg: str | None = None
                """Name of the part field to use for the Bill of Material Manufacturer Column [nargs=0..1] [default: ""]"""
                bom_col_dist_pn: str | None = None
                """Name of the part field to use for the Bill of Material Distributor Part Number Column [nargs=0..1] [default: ""]"""
                bom_col_dist: str | None = None
                """Name to insert into Bill of Material Distributor Column [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                compress: bool = False
                """Compress the output"""

            @dataclass
            class ipcd356:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""

            @dataclass
            class odb:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    precision: Precision [nargs=0..1] [default: 2]
                    compression: Compression mode [nargs=0..1] [default: "zip"]
                    units: Units [nargs=0..1] [default: "mm"]
                    help: Shows help message and exits
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                precision: str | None = None
                """Precision [nargs=0..1] [default: 2]"""
                compression: str | None = None
                """Compression mode [nargs=0..1] [default: "zip"]"""
                units: str | None = None
                """Units [nargs=0..1] [default: "mm"]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""

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
                    common_layers: Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    mirror: Mirror the board (useful for trying to show bottom layers)
                    exclude_refdes: Exclude the reference designator text
                    exclude_value: Exclude the value text
                    include_border_title: Include the border and title block
                    subtract_soldermask: Subtract soldermask from silkscreen
                    sketch_pads_on_fab_layers: Draw pad outlines and their numbers on front and back fab layers
                    hide_DNP_footprints_on_fab_layers: Don't plot text & graphics of DNP footprints on fab layers
                    sketch_DNP_footprints_on_fab_layers: Plot graphics of DNP footprints in sketch mode on fab layers
                    crossout_DNP_footprints_on_fab_layers: Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators
                    negative: Plot as negative (useful for directly etching from the export)
                    black_and_white: Black and white only
                    plot_invisible_text: Deprecated.  Has no effect.
                    mode_single: Generates a single file with the output arg path acting as the complete directory and filename path. COMMON_LAYER_LIST does not function in this mode. Instead LAYER_LIST controls all layers plotted.
                    mode_separate: Plot the layers to individual PDF files
                    mode_multipage: Plot the layers to a single PDF file with multiple pages
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                layers: str | None = None
                """Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                theme: str | None = None
                """Color theme to use (will default to PCB Editor settings) [nargs=0..1] [default: ""]"""
                drill_shape_opt: str | None = None
                """Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]"""
                common_layers: str | None = None
                """Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                mirror: bool = False
                """Mirror the board (useful for trying to show bottom layers)"""
                exclude_refdes: bool = False
                """Exclude the reference designator text"""
                exclude_value: bool = False
                """Exclude the value text"""
                include_border_title: bool = False
                """Include the border and title block"""
                subtract_soldermask: bool = False
                """Subtract soldermask from silkscreen"""
                sketch_pads_on_fab_layers: bool = False
                """Draw pad outlines and their numbers on front and back fab layers"""
                hide_DNP_footprints_on_fab_layers: bool = False
                """Don't plot text & graphics of DNP footprints on fab layers"""
                sketch_DNP_footprints_on_fab_layers: bool = False
                """Plot graphics of DNP footprints in sketch mode on fab layers"""
                crossout_DNP_footprints_on_fab_layers: bool = False
                """Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators"""
                negative: bool = False
                """Plot as negative (useful for directly etching from the export)"""
                black_and_white: bool = False
                """Black and white only"""
                plot_invisible_text: bool = False
                """Deprecated.  Has no effect."""
                mode_single: bool = False
                """Generates a single file with the output arg path acting as the complete directory and filename path. COMMON_LAYER_LIST does not function in this mode. Instead LAYER_LIST controls all layers plotted."""
                mode_separate: bool = False
                """Plot the layers to individual PDF files"""
                mode_multipage: bool = False
                """Plot the layers to a single PDF file with multiple pages"""

            @dataclass
            class ply:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    component_filter: Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]
                    min_distance: Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]
                    net_filter: Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]
                    user_origin: User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    force: Overwrite output file
                    no_unspecified: Exclude 3D models for components with 'Unspecified' footprint type
                    no_dnp: Exclude 3D models for components with 'Do not populate' attribute
                    grid_origin: Use Grid Origin for output origin
                    drill_origin: Use Drill Origin for output origin
                    subst_models: Substitute STEP or IGS models with the same name in place of VRML models
                    board_only: Only generate a board with no components
                    cut_vias_in_body: Cut via holes in board body even if conductor layers are not exported.
                    no_board_body: Exclude board body
                    no_components: Exclude 3D models for components
                    include_tracks: Export tracks and vias
                    include_pads: Export pads
                    include_zones: Export zones
                    include_inner_copper: Export elements on inner copper layers
                    include_silkscreen: Export silkscreen graphics as a set of flat faces
                    include_soldermask: Export soldermask layers as a set of flat faces
                    fuse_shapes: Fuse overlapping geometry together
                    fill_all_vias: Don't cut via holes in conductor layers.
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                component_filter: str | None = None
                """Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]"""
                min_distance: str | None = None
                """Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]"""
                net_filter: str | None = None
                """Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]"""
                user_origin: str | None = None
                """User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                force: bool = False
                """Overwrite output file"""
                no_unspecified: bool = False
                """Exclude 3D models for components with 'Unspecified' footprint type"""
                no_dnp: bool = False
                """Exclude 3D models for components with 'Do not populate' attribute"""
                grid_origin: bool = False
                """Use Grid Origin for output origin"""
                drill_origin: bool = False
                """Use Drill Origin for output origin"""
                subst_models: bool = False
                """Substitute STEP or IGS models with the same name in place of VRML models"""
                board_only: bool = False
                """Only generate a board with no components"""
                cut_vias_in_body: bool = False
                """Cut via holes in board body even if conductor layers are not exported."""
                no_board_body: bool = False
                """Exclude board body"""
                no_components: bool = False
                """Exclude 3D models for components"""
                include_tracks: bool = False
                """Export tracks and vias"""
                include_pads: bool = False
                """Export pads"""
                include_zones: bool = False
                """Export zones"""
                include_inner_copper: bool = False
                """Export elements on inner copper layers"""
                include_silkscreen: bool = False
                """Export silkscreen graphics as a set of flat faces"""
                include_soldermask: bool = False
                """Export soldermask layers as a set of flat faces"""
                fuse_shapes: bool = False
                """Fuse overlapping geometry together"""
                fill_all_vias: bool = False
                """Don't cut via holes in conductor layers."""

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
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                side: str | None = None
                """Valid options: front,back,both. Gerber format only supports "front" or "back". [nargs=0..1] [default: "both"]"""
                format: str | None = None
                """Valid options: ascii,csv,gerber [nargs=0..1] [default: "ascii"]"""
                units: str | None = None
                """Output units; ascii or csv format only; valid options: in,mm [nargs=0..1] [default: "in"]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                bottom_negate_x: bool = False
                """Use negative X coordinates for footprints on bottom layer (ascii or csv formats only)"""
                use_drill_file_origin: bool = False
                """Use drill/place file origin (ascii or csv only)"""
                smd_only: bool = False
                """Include only SMD footprints (ascii or csv only)"""
                exclude_fp_th: bool = False
                """Exclude all footprints with through-hole pads (ascii or csv only)"""
                exclude_dnp: bool = False
                """Exclude all footprints with the Do Not Populate flag set"""
                gerber_board_edge: bool = False
                """Include board edge layer (Gerber only)"""

            @dataclass
            class step:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    component_filter: Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]
                    min_distance: Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]
                    net_filter: Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]
                    user_origin: User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    force: Overwrite output file
                    no_unspecified: Exclude 3D models for components with 'Unspecified' footprint type
                    no_dnp: Exclude 3D models for components with 'Do not populate' attribute
                    grid_origin: Use Grid Origin for output origin
                    drill_origin: Use Drill Origin for output origin
                    subst_models: Substitute STEP or IGS models with the same name in place of VRML models
                    board_only: Only generate a board with no components
                    cut_vias_in_body: Cut via holes in board body even if conductor layers are not exported.
                    no_board_body: Exclude board body
                    no_components: Exclude 3D models for components
                    include_tracks: Export tracks and vias
                    include_pads: Export pads
                    include_zones: Export zones
                    include_inner_copper: Export elements on inner copper layers
                    include_silkscreen: Export silkscreen graphics as a set of flat faces
                    include_soldermask: Export soldermask layers as a set of flat faces
                    fuse_shapes: Fuse overlapping geometry together
                    fill_all_vias: Don't cut via holes in conductor layers.
                    no_optimize_step: Do not optimize STEP file (enables writing parametric curves)
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                component_filter: str | None = None
                """Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]"""
                min_distance: str | None = None
                """Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]"""
                net_filter: str | None = None
                """Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]"""
                user_origin: str | None = None
                """User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                force: bool = False
                """Overwrite output file"""
                no_unspecified: bool = False
                """Exclude 3D models for components with 'Unspecified' footprint type"""
                no_dnp: bool = False
                """Exclude 3D models for components with 'Do not populate' attribute"""
                grid_origin: bool = False
                """Use Grid Origin for output origin"""
                drill_origin: bool = False
                """Use Drill Origin for output origin"""
                subst_models: bool = False
                """Substitute STEP or IGS models with the same name in place of VRML models"""
                board_only: bool = False
                """Only generate a board with no components"""
                cut_vias_in_body: bool = False
                """Cut via holes in board body even if conductor layers are not exported."""
                no_board_body: bool = False
                """Exclude board body"""
                no_components: bool = False
                """Exclude 3D models for components"""
                include_tracks: bool = False
                """Export tracks and vias"""
                include_pads: bool = False
                """Export pads"""
                include_zones: bool = False
                """Export zones"""
                include_inner_copper: bool = False
                """Export elements on inner copper layers"""
                include_silkscreen: bool = False
                """Export silkscreen graphics as a set of flat faces"""
                include_soldermask: bool = False
                """Export soldermask layers as a set of flat faces"""
                fuse_shapes: bool = False
                """Fuse overlapping geometry together"""
                fill_all_vias: bool = False
                """Don't cut via holes in conductor layers."""
                no_optimize_step: bool = False
                """Do not optimize STEP file (enables writing parametric curves)"""

            @dataclass
            class stl:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    component_filter: Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]
                    min_distance: Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]
                    net_filter: Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]
                    user_origin: User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    force: Overwrite output file
                    no_unspecified: Exclude 3D models for components with 'Unspecified' footprint type
                    no_dnp: Exclude 3D models for components with 'Do not populate' attribute
                    grid_origin: Use Grid Origin for output origin
                    drill_origin: Use Drill Origin for output origin
                    subst_models: Substitute STEP or IGS models with the same name in place of VRML models
                    board_only: Only generate a board with no components
                    cut_vias_in_body: Cut via holes in board body even if conductor layers are not exported.
                    no_board_body: Exclude board body
                    no_components: Exclude 3D models for components
                    include_tracks: Export tracks and vias
                    include_pads: Export pads
                    include_zones: Export zones
                    include_inner_copper: Export elements on inner copper layers
                    include_silkscreen: Export silkscreen graphics as a set of flat faces
                    include_soldermask: Export soldermask layers as a set of flat faces
                    fuse_shapes: Fuse overlapping geometry together
                    fill_all_vias: Don't cut via holes in conductor layers.
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                component_filter: str | None = None
                """Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]"""
                min_distance: str | None = None
                """Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]"""
                net_filter: str | None = None
                """Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]"""
                user_origin: str | None = None
                """User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                force: bool = False
                """Overwrite output file"""
                no_unspecified: bool = False
                """Exclude 3D models for components with 'Unspecified' footprint type"""
                no_dnp: bool = False
                """Exclude 3D models for components with 'Do not populate' attribute"""
                grid_origin: bool = False
                """Use Grid Origin for output origin"""
                drill_origin: bool = False
                """Use Drill Origin for output origin"""
                subst_models: bool = False
                """Substitute STEP or IGS models with the same name in place of VRML models"""
                board_only: bool = False
                """Only generate a board with no components"""
                cut_vias_in_body: bool = False
                """Cut via holes in board body even if conductor layers are not exported."""
                no_board_body: bool = False
                """Exclude board body"""
                no_components: bool = False
                """Exclude 3D models for components"""
                include_tracks: bool = False
                """Export tracks and vias"""
                include_pads: bool = False
                """Export pads"""
                include_zones: bool = False
                """Export zones"""
                include_inner_copper: bool = False
                """Export elements on inner copper layers"""
                include_silkscreen: bool = False
                """Export silkscreen graphics as a set of flat faces"""
                include_soldermask: bool = False
                """Export soldermask layers as a set of flat faces"""
                fuse_shapes: bool = False
                """Fuse overlapping geometry together"""
                fill_all_vias: bool = False
                """Don't cut via holes in conductor layers."""

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
                    common_layers: Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    subtract_soldermask: Subtract soldermask from silkscreen
                    mirror: Mirror the board (useful for trying to show bottom layers)
                    negative: Plot as negative (useful for directly etching from the export)
                    black_and_white: Black and white only
                    sketch_pads_on_fab_layers: Draw pad outlines and their numbers on front and back fab layers
                    hide_DNP_footprints_on_fab_layers: Don't plot text & graphics of DNP footprints on fab layers
                    sketch_DNP_footprints_on_fab_layers: Plot graphics of DNP footprints in sketch mode on fab layers
                    crossout_DNP_footprints_on_fab_layers: Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators
                    fit_page_to_board: Fit the page to the board
                    exclude_drawing_sheet: No drawing sheet
                    mode_single: Generates a single file with the output arg path acting as the complete directory and filename path. COMMON_LAYER_LIST does not function in this mode. Instead LAYER_LIST controls all layers plotted.
                    mode_multi: Generates one or more files with behavior similar to the KiCad GUI plotting. The given output path specifies a directory in which files may be output.
                    plot_invisible_text: Deprecated.  Has no effect.
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                layers: str | None = None
                """Comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                theme: str | None = None
                """Color theme to use (will default to PCB editor settings) [nargs=0..1] [default: ""]"""
                page_size_mode: str | None = None
                """Set page sizing mode (0 = page with frame and title block, 1 = current page size, 2 = board area only) [nargs=0..1] [default: 0]"""
                drill_shape_opt: str | None = None
                """Set pad/via drill shape option (0 = no shape, 1 = small shape, 2 = actual shape) [nargs=0..1] [default: 2]"""
                common_layers: str | None = None
                """Layers to include on each plot, comma separated list of untranslated layer names to include such as F.Cu,B.Cu [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                subtract_soldermask: bool = False
                """Subtract soldermask from silkscreen"""
                mirror: bool = False
                """Mirror the board (useful for trying to show bottom layers)"""
                negative: bool = False
                """Plot as negative (useful for directly etching from the export)"""
                black_and_white: bool = False
                """Black and white only"""
                sketch_pads_on_fab_layers: bool = False
                """Draw pad outlines and their numbers on front and back fab layers"""
                hide_DNP_footprints_on_fab_layers: bool = False
                """Don't plot text & graphics of DNP footprints on fab layers"""
                sketch_DNP_footprints_on_fab_layers: bool = False
                """Plot graphics of DNP footprints in sketch mode on fab layers"""
                crossout_DNP_footprints_on_fab_layers: bool = False
                """Plot an 'X' over the courtyard of DNP footprints on fab layers, and strikeout their reference designators"""
                fit_page_to_board: bool = False
                """Fit the page to the board"""
                exclude_drawing_sheet: bool = False
                """No drawing sheet"""
                mode_single: bool = False
                """Generates a single file with the output arg path acting as the complete directory and filename path. COMMON_LAYER_LIST does not function in this mode. Instead LAYER_LIST controls all layers plotted."""
                mode_multi: bool = False
                """Generates one or more files with behavior similar to the KiCad GUI plotting. The given output path specifies a directory in which files may be output."""
                plot_invisible_text: bool = False
                """Deprecated.  Has no effect."""

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
                    no_unspecified: Exclude 3D models for components with 'Unspecified' footprint type
                    no_dnp: Exclude 3D models for components with 'Do not populate' attribute
                    models_relative: Used with --models-dir to output relative paths in the resulting file
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                user_origin: str | None = None
                """User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]"""
                units: str | None = None
                """Output units; valid options: mm, m, in, tenths [nargs=0..1] [default: "in"]"""
                models_dir: str | None = None
                """Name of folder to create and store 3d models in, if not specified or empty, the models will be embedded in main exported VRML file [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                force: bool = False
                """Overwrite output file"""
                no_unspecified: bool = False
                """Exclude 3D models for components with 'Unspecified' footprint type"""
                no_dnp: bool = False
                """Exclude 3D models for components with 'Do not populate' attribute"""
                models_relative: bool = False
                """Used with --models-dir to output relative paths in the resulting file"""

            @dataclass
            class xao:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    component_filter: Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]
                    min_distance: Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]
                    net_filter: Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]
                    user_origin: User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    force: Overwrite output file
                    no_unspecified: Exclude 3D models for components with 'Unspecified' footprint type
                    no_dnp: Exclude 3D models for components with 'Do not populate' attribute
                    grid_origin: Use Grid Origin for output origin
                    drill_origin: Use Drill Origin for output origin
                    subst_models: Substitute STEP or IGS models with the same name in place of VRML models
                    board_only: Only generate a board with no components
                    cut_vias_in_body: Cut via holes in board body even if conductor layers are not exported.
                    no_board_body: Exclude board body
                    no_components: Exclude 3D models for components
                    include_tracks: Export tracks and vias
                    include_pads: Export pads
                    include_zones: Export zones
                    include_inner_copper: Export elements on inner copper layers
                    include_silkscreen: Export silkscreen graphics as a set of flat faces
                    include_soldermask: Export soldermask layers as a set of flat faces
                    fuse_shapes: Fuse overlapping geometry together
                    fill_all_vias: Don't cut via holes in conductor layers.
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                component_filter: str | None = None
                """Only include component 3D models matching this list of reference designators (comma-separated, wildcards supported) [nargs=0..1] [default: ""]"""
                min_distance: str | None = None
                """Minimum distance between points to treat them as separate ones [nargs=0..1] [default: "0.01mm"]"""
                net_filter: str | None = None
                """Only include copper items belonging to nets matching this wildcard [nargs=0..1] [default: ""]"""
                user_origin: str | None = None
                """User-specified output origin ex. 1x1in, 1x1inch, 25.4x25.4mm (default unit mm) [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                force: bool = False
                """Overwrite output file"""
                no_unspecified: bool = False
                """Exclude 3D models for components with 'Unspecified' footprint type"""
                no_dnp: bool = False
                """Exclude 3D models for components with 'Do not populate' attribute"""
                grid_origin: bool = False
                """Use Grid Origin for output origin"""
                drill_origin: bool = False
                """Use Drill Origin for output origin"""
                subst_models: bool = False
                """Substitute STEP or IGS models with the same name in place of VRML models"""
                board_only: bool = False
                """Only generate a board with no components"""
                cut_vias_in_body: bool = False
                """Cut via holes in board body even if conductor layers are not exported."""
                no_board_body: bool = False
                """Exclude board body"""
                no_components: bool = False
                """Exclude 3D models for components"""
                include_tracks: bool = False
                """Export tracks and vias"""
                include_pads: bool = False
                """Export pads"""
                include_zones: bool = False
                """Export zones"""
                include_inner_copper: bool = False
                """Export elements on inner copper layers"""
                include_silkscreen: bool = False
                """Export silkscreen graphics as a set of flat faces"""
                include_soldermask: bool = False
                """Export soldermask layers as a set of flat faces"""
                fuse_shapes: bool = False
                """Fuse overlapping geometry together"""
                fill_all_vias: bool = False
                """Don't cut via holes in conductor layers."""

        @dataclass
        class render:
            """
            Args:
                INPUT_FILE: Input file
                output: Output file [nargs=0..1] [default: ""]
                define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                width: Image width [nargs=0..1] [default: 1600]
                height: Image height [nargs=0..1] [default: 900]
                side: Render from side. Options: top, bottom, left, right, front, back [nargs=0..1] [default: "top"]
                background: Image background. Options: default, transparent, opaque. Default: transparent for PNG, opaque for JPEG [nargs=0..1] [default: ""]
                quality: Render quality. Options: basic, high, user [nargs=0..1] [default: "basic"]
                preset: Color preset. Options: follow_pcb_editor, follow_plot_settings, legacy_preset_flag, ... [nargs=0..1] [default: "follow_plot_settings"]
                zoom: Camera zoom [nargs=0..1] [default: 1]
                pan: Pan camera, format 'X,Y,Z' e.g.: '3,0,0' [nargs=0..1] [default: ""]
                pivot: Set pivot point relative to the board center in centimeters, format 'X,Y,Z' e.g.: '-10,2,0' [nargs=0..1] [default: ""]
                rotate: Rotate board, format 'X,Y,Z' e.g.: '-45,0,45' for isometric view [nargs=0..1] [default: ""]
                light_top: Top light intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: ""]
                light_bottom: Bottom light intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: ""]
                light_side: Side lights intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: ""]
                light_camera: Camera light intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: ""]
                light_side_elevation: Side lights elevation angle in degrees, range: 0-90 [nargs=0..1] [default: 60]
                help: Shows help message and exits
                floor: Enables floor, shadows and post-processing, even if disabled in quality preset
                perspective: Use perspective projection instead of orthogonal
            """

            # Arguments (Required)
            INPUT_FILE: str
            """Input file"""
            # Arguments (Optional)
            output: str | None = None
            """Output file [nargs=0..1] [default: ""]"""
            define_var: str | None = None
            """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
            width: str | None = None
            """Image width [nargs=0..1] [default: 1600]"""
            height: str | None = None
            """Image height [nargs=0..1] [default: 900]"""
            side: str | None = None
            """Render from side. Options: top, bottom, left, right, front, back [nargs=0..1] [default: "top"]"""
            background: str | None = None
            """Image background. Options: default, transparent, opaque. Default: transparent for PNG, opaque for JPEG [nargs=0..1] [default: ""]"""
            quality: str | None = None
            """Render quality. Options: basic, high, user [nargs=0..1] [default: "basic"]"""
            preset: str | None = None
            """Color preset. Options: follow_pcb_editor, follow_plot_settings, legacy_preset_flag, ... [nargs=0..1] [default: "follow_plot_settings"]"""
            zoom: str | None = None
            """Camera zoom [nargs=0..1] [default: 1]"""
            pan: str | None = None
            """Pan camera, format 'X,Y,Z' e.g.: '3,0,0' [nargs=0..1] [default: ""]"""
            pivot: str | None = None
            """Set pivot point relative to the board center in centimeters, format 'X,Y,Z' e.g.: '-10,2,0' [nargs=0..1] [default: ""]"""
            rotate: str | None = None
            """Rotate board, format 'X,Y,Z' e.g.: '-45,0,45' for isometric view [nargs=0..1] [default: ""]"""
            light_top: str | None = None
            """Top light intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: ""]"""
            light_bottom: str | None = None
            """Bottom light intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: ""]"""
            light_side: str | None = None
            """Side lights intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: ""]"""
            light_camera: str | None = None
            """Camera light intensity, format 'R,G,B' or a single number, range: 0-1 [nargs=0..1] [default: ""]"""
            light_side_elevation: str | None = None
            """Side lights elevation angle in degrees, range: 0-90 [nargs=0..1] [default: 60]"""
            # Flags
            help: bool = False
            """Shows help message and exits"""
            floor: bool = False
            """Enables floor, shadows and post-processing, even if disabled in quality preset"""
            perspective: bool = False
            """Use perspective projection instead of orthogonal"""

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
        """Shows help message and exits"""

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
            """Input file"""
            # Arguments (Optional)
            output: str | None = None
            """Output file [nargs=0..1] [default: ""]"""
            define_var: str | None = None
            """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
            format: str | None = None
            """Output file format, options: json, report [nargs=0..1] [default: "report"]"""
            units: str | None = None
            """Report units; valid options: in, mm, mils [nargs=0..1] [default: "mm"]"""
            # Flags
            help: bool = False
            """Shows help message and exits"""
            severity_all: bool = False
            """Report all ERC violations, this is equivalent to including all the other severity arguments"""
            severity_error: bool = False
            """Report all ERC error level violations, this can be combined with the other severity arguments"""
            severity_warning: bool = False
            """Report all ERC warning level violations, this can be combined with the other severity arguments"""
            severity_exclusions: bool = False
            """Report all excluded ERC violations, this can be combined with the other severity arguments"""
            exit_code_violations: bool = False
            """Return a nonzero exit code if ERC violations exist"""

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
            """Shows help message and exits"""

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
                    include_excluded_from_bom: Include symbols marked 'Exclude from BOM'.
                    keep_tabs: Keep tab characters from input fields. Stripped by default.
                    keep_line_breaks: Keep line break characters from input fields. Stripped by default.
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                preset: str | None = None
                """Use a named BOM preset setting from the schematic, e.g. "Grouped By Value". [nargs=0..1] [default: ""]"""
                format_preset: str | None = None
                """Use a named BOM format preset setting from the schematic, e.g. CSV. [nargs=0..1] [default: ""]"""
                fields: str | None = None
                """An ordered list of fields to export. See documentation for special substitutions. [nargs=0..1] [default: "Reference,Value,Footprint,${QUANTITY},${DNP}"]"""
                labels: str | None = None
                """An ordered list of labels to apply the exported fields. [nargs=0..1] [default: "Refs,Value,Footprint,Qty,DNP"]"""
                group_by: str | None = None
                """Fields to group references by when field values match. [nargs=0..1] [default: ""]"""
                sort_field: str | None = None
                """Field name to sort by. [nargs=0..1] [default: "Reference"]"""
                filter: str | None = None
                """Filter string to remove output lines. [nargs=0..1] [default: ""]"""
                field_delimiter: str | None = None
                """Separator between output fields/columns. [nargs=0..1] [default: ","]"""
                string_delimiter: str | None = None
                """Character to surround fields with. [nargs=0..1] [default: " " "]"""
                ref_delimiter: str | None = None
                """Character to place between individual references. [nargs=0..1] [default: ","]"""
                ref_range_delimiter: str | None = None
                """Character to place in ranges of references. Leave blank for no ranges. [nargs=0..1] [default: "-"]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                sort_asc: bool = False
                """Sort ascending (true) or descending (false)."""
                exclude_dnp: bool = False
                """Exclude symbols marked Do-Not-Populate."""
                include_excluded_from_bom: bool = False
                """Include symbols marked 'Exclude from BOM'."""
                keep_tabs: bool = False
                """Keep tab characters from input fields. Stripped by default."""
                keep_line_breaks: bool = False
                """Keep line break characters from input fields. Stripped by default."""

            @dataclass
            class dxf:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]
                    default_font: Default font name [nargs=0..1] [default: "KiCad Font"]
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                    exclude_drawing_sheet: No drawing sheet
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output directory [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                theme: str | None = None
                """Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]"""
                default_font: str | None = None
                """Default font name [nargs=0..1] [default: "KiCad Font"]"""
                pages: str | None = None
                """List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                black_and_white: bool = False
                """Black and white only"""
                exclude_drawing_sheet: bool = False
                """No drawing sheet"""

            @dataclass
            class hpgl:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    default_font: Default font name [nargs=0..1] [default: "KiCad Font"]
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    pen_size: Pen size [mm] [nargs=0..1] [default: 0.5]
                    origin: Origin and scale: 0 bottom left, 1 centered, 2 page fit, 3 content fit [nargs=0..1] [default: 1]
                    help: Shows help message and exits
                    exclude_drawing_sheet: No drawing sheet
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output directory [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                default_font: str | None = None
                """Default font name [nargs=0..1] [default: "KiCad Font"]"""
                pages: str | None = None
                """List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]"""
                pen_size: str | None = None
                """Pen size [mm] [nargs=0..1] [default: 0.5]"""
                origin: str | None = None
                """Origin and scale: 0 bottom left, 1 centered, 2 page fit, 3 content fit [nargs=0..1] [default: 1]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                exclude_drawing_sheet: bool = False
                """No drawing sheet"""

            @dataclass
            class netlist:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    format: Netlist output format, valid options: kicadsexpr, kicadxml, cadstar, orcadpcb2, spice, spicemodel, pads, allegro [nargs=0..1] [default: "kicadsexpr"]
                    help: Shows help message and exits
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                format: str | None = None
                """Netlist output format, valid options: kicadsexpr, kicadxml, cadstar, orcadpcb2, spice, spicemodel, pads, allegro [nargs=0..1] [default: "kicadsexpr"]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""

            @dataclass
            class pdf:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output file [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]
                    default_font: Default font name [nargs=0..1] [default: "KiCad Font"]
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                    exclude_drawing_sheet: No drawing sheet
                    exclude_pdf_property_popups: Do not generate property popups in PDF
                    exclude_pdf_hierarchical_links: Do not generate clickable links for hierarchical elements in PDF
                    exclude_pdf_metadata: Do not generate PDF metadata from AUTHOR and SUBJECT variables
                    no_background_color: Avoid setting a background color (regardless of theme)
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                theme: str | None = None
                """Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]"""
                default_font: str | None = None
                """Default font name [nargs=0..1] [default: "KiCad Font"]"""
                pages: str | None = None
                """List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                black_and_white: bool = False
                """Black and white only"""
                exclude_drawing_sheet: bool = False
                """No drawing sheet"""
                exclude_pdf_property_popups: bool = False
                """Do not generate property popups in PDF"""
                exclude_pdf_hierarchical_links: bool = False
                """Do not generate clickable links for hierarchical elements in PDF"""
                exclude_pdf_metadata: bool = False
                """Do not generate PDF metadata from AUTHOR and SUBJECT variables"""
                no_background_color: bool = False
                """Avoid setting a background color (regardless of theme)"""

            @dataclass
            class ps:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]
                    default_font: Default font name [nargs=0..1] [default: "KiCad Font"]
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                    exclude_drawing_sheet: No drawing sheet
                    no_background_color: Avoid setting a background color (regardless of theme)
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output directory [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                theme: str | None = None
                """Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]"""
                default_font: str | None = None
                """Default font name [nargs=0..1] [default: "KiCad Font"]"""
                pages: str | None = None
                """List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                black_and_white: bool = False
                """Black and white only"""
                exclude_drawing_sheet: bool = False
                """No drawing sheet"""
                no_background_color: bool = False
                """Avoid setting a background color (regardless of theme)"""

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
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output file [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""

            @dataclass
            class svg:
                """
                Args:
                    INPUT_FILE: Input file
                    output: Output directory [nargs=0..1] [default: ""]
                    drawing_sheet: Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]
                    define_var: Overrides or adds project variables, can be used multiple times to declare multiple variables.
                    theme: Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]
                    default_font: Default font name [nargs=0..1] [default: "KiCad Font"]
                    pages: List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]
                    help: Shows help message and exits
                    black_and_white: Black and white only
                    exclude_drawing_sheet: No drawing sheet
                    no_background_color: Avoid setting a background color (regardless of theme)
                """

                # Arguments (Required)
                INPUT_FILE: str
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output directory [nargs=0..1] [default: ""]"""
                drawing_sheet: str | None = None
                """Path to drawing sheet, this overrides any existing project defined sheet when used [nargs=0..1] [default: ""]"""
                define_var: str | None = None
                """Overrides or adds project variables, can be used multiple times to declare multiple variables."""
                theme: str | None = None
                """Color theme to use (will default to schematic settings) [nargs=0..1] [default: ""]"""
                default_font: str | None = None
                """Default font name [nargs=0..1] [default: "KiCad Font"]"""
                pages: str | None = None
                """List of page numbers separated by comma to print, blank or unspecified is equivalent to all pages [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                black_and_white: bool = False
                """Black and white only"""
                exclude_drawing_sheet: bool = False
                """No drawing sheet"""
                no_background_color: bool = False
                """Avoid setting a background color (regardless of theme)"""

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
        """Shows help message and exits"""

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
            """Shows help message and exits"""

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
                """Input file"""
                # Arguments (Optional)
                output: str | None = None
                """Output directory [nargs=0..1] [default: ""]"""
                theme: str | None = None
                """Color theme to use (will default to symbol editor settings) [nargs=0..1] [default: ""]"""
                symbol: str | None = None
                """Specific symbol to export within the library [nargs=0..1] [default: ""]"""
                # Flags
                help: bool = False
                """Shows help message and exits"""
                black_and_white: bool = False
                """Black and white only"""
                include_hidden_pins: bool = False
                """Include hidden pins"""
                include_hidden_fields: bool = False
                """Include hidden fields"""

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
            """Input file"""
            # Arguments (Optional)
            output: str | None = None
            """Output file [nargs=0..1] [default: ""]"""
            # Flags
            help: bool = False
            """Shows help message and exits"""
            force: bool = False
            """Forces the symbol library to be resaved regardless of versioning"""

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
        """version info format (plain, commit, about) [nargs=0..1] [default: "plain"]"""
        # Flags
        help: bool = False
        """Shows help message and exits"""

    def exec(self, check=False):
        return run_parser_command(l2_root=kicad_cli_l2, cmd=self, check=check)
