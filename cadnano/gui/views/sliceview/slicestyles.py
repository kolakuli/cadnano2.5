from PyQt5.QtGui import QColor, QFont

from cadnano.gui.views.styles import *

# Slice Sizing
SLICE_HELIX_RADIUS = 15
SLICE_HELIX_STROKE_WIDTH = 0.5
SLICE_HELIX_HILIGHT_WIDTH = 0.5
SLICE_HELIX_MOD_HILIGHT_WIDTH = 1
HONEYCOMB_PART_MAXROWS = 10
HONEYCOMB_PART_MAXCOLS = 10
HONEYCOMB_PART_MAXSTEPS = 2
SQUARE_PART_MAXROWS = 50
SQUARE_PART_MAXCOLS = 50
SQUARE_PART_MAXSTEPS = 2

# Z values
# bottom
ZSLICEHELIX = 50
ZDESELECTOR = 60
ZPARTITEM = 200
# top

# Part apperance
OUT_OF_SLICE_FILL = "#fafafa"
DEFAULT_PEN_WIDTH = 1
DEFAULT_ALPHA = 2
SELECTED_COLOR = '#5a8bff'
SELECTED_PEN_WIDTH = 2
SELECTED_ALPHA = 0

SLICE_NUM_FONT = QFont(THE_FONT, 10, QFont.Bold)
USE_TEXT_COLOR = "#ffffff"
OUT_OF_SLICE_TEXT_COLOR = "#000000"
