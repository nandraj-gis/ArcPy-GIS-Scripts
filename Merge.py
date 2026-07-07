import arcpy

# Input Feature Classes
input_features = [
    r"C:\GIS\Village1.shp",
    r"C:\GIS\Village2.shp"
]

# Output Feature Class
output_fc = r"C:\GIS\Village_Merge.shp"

# Perform Merge
arcpy.management.Merge(
    input_features,
    output_fc
)

print("Merge completed successfully.")
