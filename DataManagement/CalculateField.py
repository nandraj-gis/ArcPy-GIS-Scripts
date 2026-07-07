"""
Script Name : CalculateField.py
Description : Calculates values for an existing field using ArcPy.
Author      : Nandraj Surwase
Software    : ArcGIS Pro
"""

import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Calculate Field
arcpy.management.CalculateField(
    input_fc,
    "Area_Ha",
    "!shape.area@HECTARES!",
    "PYTHON3"
)

print("Field Calculated Successfully")
