'''
Demo Length_partition

This script must be run from the demo folder or else the 
toolbox, input, and output locations must be adjusted for
where demo.py is being run.

cd LinePartition/demo

python -i demo.py

'''

import arcpy

arcpy.ImportToolbox(r"..\partition.pyt")

input = r"workspace.gdb\line"
workspace = "workspace.gdb"
output = r"by_length"
length = 50
overwriteOutput = True

arcpy.Length_partition(input, workspace, output, length, overwriteOutput)


