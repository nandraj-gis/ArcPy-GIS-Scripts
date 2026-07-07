"""
Script Name : CopyFeatures.py
Description : Copies features from one feature class to another.
Author      : Nandraj Surwase
Software    : ArcGIS Pro
"""

import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Output Feature Class
output_fc = r"C:\GIS\Village_Copy.shp"

# Copy Features
arcpy.management.CopyFeatures(
    input_fc,
    output_fc
)

print("Features Copied Successfully")
