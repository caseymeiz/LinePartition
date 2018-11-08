import arcpy
import lpt
import ppt
import flpt
reload(lpt)
reload(ppt)
reload(flpt)
from lpt import Length
from ppt import Proportion
from flpt import FixedLength

class Toolbox(object):
	def __init__(self):
		"""Define the toolbox (the name of the toolbox is the name of the
		.pyt file)."""
		self.label = "Toolbox"
		self.alias = "partition"
		# List of tool classes associated with this toolbox
		self.tools = [Length, Proportion, FixedLength]


