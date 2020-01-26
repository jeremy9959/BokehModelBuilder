from sortedcollections import SortedDict
from bokeh.models.scales import LogScale, LinearScale
from bokeh.models.tools import (
    BoxEditTool,
    BoxSelectTool,
    BoxZoomTool,
    CrosshairTool,
    EditTool,
    FreehandDrawTool,
    HelpTool,
    HoverTool,
    LassoSelectTool,
    PanTool,
    PointDrawTool,
    PolyDrawTool,
    PolyEditTool,
    PolySelectTool,
    RangeTool,
    RedoTool,
    ResetTool,
    SaveTool,
    TapTool,
    WheelPanTool,
    WheelZoomTool,
    ZoomInTool,
    ZoomOutTool,
)

tool_name_list = [
    "BoxEdit",
    "BoxSelect",
    "BoxZoom",
    "Crosshair",
    "Edit",
    "FreehandDraw",
    "Help",
    "Hover",
    "LassoSelect",
    "Pan",
    "PointDraw",
    "PolyDraw",
    "PolyEdit",
    "PolySelect",
    "RangeTool",
    "RedoTool",
    "Reset",
    "Save",
    "Tap",
    "WheelPan",
    "WheelZoom",
    "ZoomIn",
    "ZoomOut",
]

tool_instances = [
    BoxEditTool(),
    BoxSelectTool(),
    BoxZoomTool(),
    CrosshairTool(),
    EditTool(),
    FreehandDrawTool(),
    HelpTool(),
    HoverTool(),
    LassoSelectTool(),
    PanTool(),
    PointDrawTool(),
    PolyDrawTool(),
    PolyEditTool(),
    PolySelectTool(),
    RangeTool(),
    RedoTool(),
    ResetTool(),
    SaveTool(),
    TapTool(),
    WheelPanTool(),
    WheelZoomTool(),
    ZoomInTool(),
    ZoomOutTool(),
]

Toolbar_Options = {
    "multi_choices": {"tools": (tool_name_list, tool_instances)},
    "choices": {
        "logo": (["normal", "grey", "none"], ["normal", "grey", None]),
        "autohide": (["false", "true"], [False, True]),
    },
    "floats": {},
    "colors": {},
    "ints": {},
}

Plot_Options = {
    "multi_choices": {},
    "choices": {
        "height_policy": (
            ["auto", "fixed", "fit", "min", "max"],
            ["auto", "fixed", "fit", "min", "max"],
        ),
        "width_policy": (
            ["auto", "fixed", "fit", "min", "max"],
            ["auto", "fixed", "fit", "min", "max"],
        ),
        "x_scale": (["Linear", "Log"], [LinearScale(), LogScale()]),
        "y_scale": (["Linear", "Log"], [LinearScale(), LogScale()]),
        "title_location": (
            ["above", "below", "left", "right"],
            ["above", "below", "left", "right"],
        ),
        "outline_line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "outline_line_join": (["miter", "round", "bevel"], ["miter", "round", "bevel"]),
        "sizing_mode": (
            [
                "stretch_both",
                "stretch_width",
                "stretch_height",
                "scale_width",
                "scale_height",
                "scale_both",
                "fixed",
            ],
            [
                "stretch_both",
                "stretch_width",
                "stretch_height",
                "scale_width",
                "scale_height",
                "scale_both",
                "fixed",
            ],
        ),
        "toolbar_location": (
            ["above", "below", "left", "right"],
            ["above", "below", "left", "right"],
        ),
    },
    "floats": {
        "background_fill_alpha": 1.0,
        "border_fill_alpha": 1.0,
        "outline_line_alpha": 1.0,
        "outline_line_width": 1.0,
    },
    "ints": {
        "frame_height": None,
        "frame_width": None,
        "min_border": 5,
        "min_border_bottom": None,
        "min_border_left": None,
        "min_border_right": None,
        "min_border_top": None,
        "outline_line_dash_offset": 0,
        "plot_height": 600,
        "plot_width": 600,
    },
    "colors": {
        "background": "#ffffff",
        "background_fill_color": "#ffffff",
        "border_fill_color": "#ffffff",
        "outline_line_color": "#e5e5e5",
    },
}

Grid_Options = {
    "multi_choices": {},
    "colors": {
        "minor_grid_line_color": "#FFFFFF",
        "band_fill_color": "#FFFFFF",
        "band_hatch_color": "#000000",
        "grid_line_color": "#e5e5e5",
    },
    "choices": {
        "band_hatch_pattern": (
            [
                "blank",
                ".",
                "o",
                "-",
                "|",
                "+",
                '"',
                ":",
                "@",
                "/",
                "\\",
                "x",
                ",",
                "`",
                "v",
                ">",
                "*",
            ],
            [
                "blank",
                ".",
                "o",
                "-",
                "|",
                "+",
                '"',
                ":",
                "@",
                "/",
                "\\",
                "x",
                ",",
                "`",
                "v",
                ">",
                "*",
            ],
        ),
        "grid_line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "grid_line_join": (["bevel", "miter", "round"], ["bevel", "miter", "round"]),
        "minor_grid_line_cap": (
            ["butt", "round", "square"],
            ["butt", "round", "square"],
        ),
        "minor_grid_line_join": (
            ["bevel", "miter", "round"],
            ["bevel", "miter", "round"],
        ),
        "level": (
            ["underlay", "image", "glyph", "annotation", "overlay"],
            ["underlay", "image", "glyph", "annotation", "overlay"],
        ),
    },
    "floats": {
        "grid_line_width": 1.0,
        "grid_line_alpha": 1.0,
        "minor_grid_line_width": 1.0,
        "band_fill_alpha": 0.0,
        "band_hatch_alpha": 1.0,
        "minor_grid_line_alpha": 1.0,
    },
    "ints": {
        "grid_line_dash_offset": 0,
        "minor_grid_line_dash_offset": 0,
        "band_hatch_scale": 12,
        "band_hatch_weight": 1,
        #        "dimension": 0,
        # set dimension in construction of grid to avoid confusion later
    },
}

Title_Options = {
    "colors": {
        "border_line_color": "#ffffff",
        "text_color": "#444444",
        "background_fill_color": "#ffffff",
    },
    "choices": {
        "border_line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "level": (
            ["underlay", "image", "glyph", "annotation", "overlay"],
            ["underlay", "image", "glyph", "annotation", "overlay"],
        ),
        "align": (["left", "right", "center"], ["left", "right", "center"]),
        "border_line_join": (["bevel", "miter", "round"], ["bevel", "miter", "round"]),
        "text_font_style": (
            ["bold", "normal", "italic", "bold italic"],
            ["bold", "normal", "italic", "bold italic"],
        ),
        "vertical_align": (["bottom", "top", "middle"], ["bottom", "top", "middle"]),
        "text_font_size": (
            ["10pt", "12pt", "16pt", "18pt", "24pt", "32pt"],
            ["10pt", "12pt", "16pt", "18pt", "24pt", "32pt"],
        ),
        "text_font": (
            ["helvetica", "times", "calibri"],
            ["helvetica", "times", "calibri"],
        ),
    },
    "floats": {
        "text_line_height": 1.0,
        "offset": 0.0,
        "border_line_alpha": 1.0,
        "background_fill_alpha": 1.0,
        "border_line_width": 1.0,
        "text_alpha": 1.0,
    },
    "strings": {"text": ""},
}

Axis_Options = {
    "choices": {
        "axis_label_text_baseline": (
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
        ),
        "major_label_orientation": (
            ["horizontal", "vertical"],
            ["horizontal", "vertical"],
        ),
        "major_tick_line_dash": (
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
        ),
        "axis_label_text_font_style": (
            ["normal", "italic", "bold", "bold italic"],
            ["normal", "italic", "bold", "bold italic"],
        ),
        "major_label_text_font_style": (
            ["normal", "italic", "bold", "bold italic"],
            ["normal", "italic", "bold", "bold italic"],
        ),
        "axis_line_join": (["miter", "round", "bevel"], ["miter", "round", "bevel"]),
        "axis_line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "axis_label_text_align": (
            ["left", "right", "center"],
            ["left", "right", "center"],
        ),
        "major_tick_line_cap": (
            ["butt", "round", "square"],
            ["butt", "round", "square"],
        ),
        "axis_line_dash": (
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
        ),
        "minor_tick_line_cap": (
            ["butt", "round", "square"],
            ["butt", "round", "square"],
        ),
        "minor_tick_line_dash": (
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
        ),
        "major_label_text_baseline": (
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
        ),
        "major_label_text_font_size": (
            ["10pt", "12pt", "16pt", "24pt", "32pt"],
            ["10pt", "12pt", "16pt", "24pt", "32pt"],
        ),
        "major_label_text_align": (
            ["left", "right", "center"],
            ["left", "right", "center"],
        ),
        "major_tick_line_join": (
            ["miter", "round", "bevel"],
            ["miter", "round", "bevel"],
        ),
        "level": (
            ["image", "underlay", "glyph", "annotation", "overlay"],
            ["image", "underlay", "glyph", "annotation", "overlay"],
        ),
        "minor_tick_line_join": (
            ["miter", "round", "bevel"],
            ["miter", "round", "bevel"],
        ),
        "axis_label_text_font_size": (
            ["10pt", "12pt", "16pt", "24pt", "32pt"],
            ["10pt", "12pt", "16pt", "24pt", "32pt"]
        ),
        "major_label_text_font": (["helvetica","times","calibri"],["helvetica","times","calibri"]),
        "axis_label_text_font":  (["helvetica","times","calibri"],["helvetica","times","calibri"]),
    },
    "strings": {
        "axis_label": "Label",
    },
    "ints": {
        "axis_line_dash_offset": 0,
        "major_label_standoff": 5,
        "minor_tick_out": 4,
        "axis_label_standoff": 5,
        "minor_tick_line_dash_offset": 0,
        "major_tick_in": 2,
        "major_tick_line_dash_offset": 0,
        "major_tick_out": 6,
        "minor_tick_in": 0,
    },
    "floats": {
        "major_tick_line_alpha": 1.0,
        "major_tick_line_width": 1,
        "axis_line_width": 1,
        "minor_tick_line_alpha": 1.0,
        "axis_label_text_line_height": 1.2,
        "major_label_text_alpha": 1.0,
        "major_label_text_line_height": 1.2,
        "axis_line_alpha": 1.0,
        "minor_tick_line_width": 1,
        "axis_label_text_alpha": 1.0,
    },
    "colors": {
        "major_label_text_color": "#444444",
        "axis_label_text_color": "#444444",
        "axis_line_color": "black",
        "major_tick_line_color": "black",
        "minor_tick_line_color": "black",
    },
}
