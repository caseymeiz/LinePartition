# Line Partition

Python Toolbox for slicing line features in to equal portions.

## Requirements

ArcGIS license: Basic

## Usage

**You can use it as a stand alone Python Toolbox**

**Or import it into your workflow**

```python
import arcpy

arcpy.ImportToolbox(r"path\to\the\tool\partition.pyt")

in_lines = r"path\to\input\workspace.gdb\line"
workspace = r"path\to\workspace\workspace.gdb"
out_lines = r"by_length" # just the name of the output features
length = 100
overwriteOutput = True

arcpy.Length_partition(in_lines, workspace, out_lines, length, overwriteOutput)
```

## Examples

**Original** 

![Original](img/original.png)





**By proportions (3)**

```python
arcpy.Proportion_partition(in_lines, workspace, out_lines, length, overwriteOutput)
```



![Proportion](img/proportion.png)

**By length (100 feet)**

```python
arcpy.Length_partition(in_lines, workspace, out_lines, length, overwriteOutput)
```



![by length](img/bylength.png)

