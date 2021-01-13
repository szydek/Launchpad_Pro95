import Live
from consts import * 
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.CompoundComponent import CompoundComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.Util import find_if
from itertools import imap
from NoteEditorComponent import NoteEditorComponent
from ScaleComponent import * 
from TrackControllerComponent import TrackControllerComponent
import time
import Settings

# quantization button colours. this must remain of length 4.
QUANTIZATION_MAP = [1, 0.5, 0.25, 0.125]  # 1/4 1/8 1/16 1/32
QUANTIZATION_NAMES = ["1/4", "1/8", "1/16", "1/32"]

STEPSEQ_MODE_NORMAL = 1
STEPSEQ_MODE_MULTINOTE = 2
STEPSEQ_MODE_SCALE_EDIT = 10

LONG_BUTTON_PRESS = 1.0

class SetCalcComponent(CompoundComponent):

	def __init__(self, control_surface = None, matrix = None, side_buttons = None, top_buttons = None):
		self._osd = None
		self._control_surface = control_surface
		super(SetCalcComponent, self).__init__()