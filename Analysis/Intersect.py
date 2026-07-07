import arcpy

# Input Feature Classes
input_features = [
    r"C:\GIS\Roads.shp",
    r"C:\GIS\Village.shp"
]

# Output Feature Class
output_fc = r"C:\GIS\Roads_Intersect.shp"

# Perform Intersect Analysis
arcpy.analysis.Intersect(
    input_features,
    output_fc
)

print("Intersect completed successfully.")
