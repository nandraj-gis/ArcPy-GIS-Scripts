"""
Script Name : AddField.py
Description : Adds a new field to an existing feature class using ArcPy.
Author      : Nandraj Surwase
Software    : ArcGIS Pro
"""

import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Add New Field
arcpy.management.AddField(
    input_fc,
    "Area_Ha",
    "DOUBLE"
)

print("Field Added Successfully")
