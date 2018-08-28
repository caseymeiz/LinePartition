import arcpy
import os 

class Toolbox(object):
	def __init__(self):
		"""Define the toolbox (the name of the toolbox is the name of the
		.pyt file)."""
		self.label = "Toolbox"
		self.alias = "demo"
		# List of tool classes associated with this toolbox
		self.tools = [Demo]


class Demo(object):
	def __init__(self):
		"""Define the tool (tool name is the name of the class)."""
		self.label = "Demo"
		self.description = ""
		self.canRunInBackground = False
		demo_folder = os.path.dirname(os.path.abspath(__file__))
		toolbox = os.path.join(demo_folder, "..", "partition.pyt")
		arcpy.ImportToolbox(toolbox)

	def getParameterInfo(self):
		"""Define parameter definitions"""
		params = None
		return params

	def isLicensed(self):
		"""Set whether tool is licensed to execute."""
		return True

	def updateParameters(self, parameters):
		"""Modify the values and properties of parameters before internal
		validation is performed.  This method is called whenever a parameter
		has been changed."""
		return

	def updateMessages(self, parameters):
		"""Modify the messages created by internal validation for each tool
		parameter.	This method is called after internal validation."""
		return

	def execute(self, parameters, messages):
		"""The source code of the tool."""
		input = r"workspace.gdb\line"
		workspace = "workspace.gdb"
		output = r"by_length"
		length = 50
		overwriteOutput = True

		arcpy.Length_partition(input, workspace, output, length, overwriteOutput)