import arcpy
import lpt
import ppt
reload(lpt)
reload(ppt)
from lpt import Length
from ppt import Proportion

class Toolbox(object):
	def __init__(self):
		"""Define the toolbox (the name of the toolbox is the name of the
		.pyt file)."""
		self.label = "Toolbox"
		self.alias = ""
		# List of tool classes associated with this toolbox
		self.tools = [Length, Proportion]


