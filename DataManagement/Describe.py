"""
Script Name : Describe.py
Description : Retrieves properties of a feature class using ArcPy Describe.
Author      : Nandraj Surwase
Software    : ArcGIS Pro
"""

import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Describe Dataset
desc = arcpy.Describe(input_fc)

print("Name :", desc.name)
print("Shape Type :", desc.shapeType)
print("Spatial Reference :", desc.spatialReference.name)

print("Describe Completed")
