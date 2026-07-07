"""
Script Name : DeleteField.py
Description : Deletes an existing field from a feature class using ArcPy.
Author      : Nandraj Surwase
Software    : ArcGIS Pro
"""

import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Delete Field
arcpy.management.DeleteField(
    input_fc,
    "Area_Ha"
)

print("Field Deleted Successfully")
