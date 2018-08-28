import arcpy
from math import ceil

class Proportion(object):
	def __init__(self):
		"""Define the tool (tool name is the name of the class)."""
		self.label = "Proportion"
		self.description = "Partition line segments approximately a specified length. The number of parts per line segment will vary depending on the length of the original line segment."
		self.canRunInBackground = False

	def getParameterInfo(self):
		"""Define parameter definitions"""
		param0 = arcpy.Parameter(name = "in_lines",
		                         displayName = "Input Lines",
		                         direction = "Input",
		                         parameterType = "Required",
		                         datatype = "DEFeatureClass")
		param1 = arcpy.Parameter(name = "out_lines",
		                         displayName = "Output Partitioned Lines",
		                         direction = "Output",
		                         parameterType = "Required",
		                         datatype = "DEFeatureClass")
		param2 = arcpy.Parameter(name = "proportion",
		                         displayName = "Number of parts per line",
		                         direction = "Input",
		                         parameterType = "Required",
		                         datatype = "GPLong")
		
		params = [param0, param1, param2]
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
		in_lines = parameters[0].valueAsText
		out_lines = parameters[1].valueAsText
		length = parameters[2].value
		
		out_mem = "in_memory/out"
		
		sr = arcpy.Describe(in_lines).spatialReference
		arcpy.CreateFeatureclass_management("in_memory", "out", "POLYLINE", template=in_lines,spatial_reference=sr)
		
		fields = arcpy.ListFields(in_lines)
		
		fields = map(lambda f: f.name, fields)

		fields.remove("SHAPE")
		fields.insert(0, "SHAPE@")
		
		with arcpy.da.SearchCursor(in_lines, fields) as scur:
			with arcpy.da.InsertCursor(out_mem, fields ) as icur:
			
				for srow in scur:
					line = srow[0]
					line_segments = self.segment(line, length)
					
					for line_segment in line_segments:
						irow = [line_segment,]+list(srow[1:])
						icur.insertRow(irow)
						
		arcpy.CopyFeatures_management(out_mem, out_lines)
		arcpy.Delete_management(out_mem)
		
		return

	def segment(self, line, partitions):
		length = line.getLength("PLANAR", "FEET")
		segments = list()
		start = 0
		end = length/partitions
		for part in range(partitions+1):
			line_segment = line.segmentAlongLine(start, end)
			if line_segment.length > 0:
				segments.append(line_segment)
			start = end
			end = (part+1)*length/partitions
		return segments
		
		