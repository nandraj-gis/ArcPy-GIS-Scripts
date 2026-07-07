"""
Script Name : ListFields.py
Description : Lists all fields in a feature class using ArcPy.
Author      : Nandraj Surwase
Software    : ArcGIS Pro
"""

import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# List Fields
fields = arcpy.ListFields(input_fc)

for field in fields:
    print(field.name)

print("Field Listing Completed")
