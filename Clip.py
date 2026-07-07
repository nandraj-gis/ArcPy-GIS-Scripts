import arcpy

# Input Features
input_fc = r"C:\GIS\Roads.shp"

# Clip Features (Boundary)
clip_fc = r"C:\GIS\Village.shp"

# Output Feature Class
output_fc = r"C:\GIS\Roads_Clip.shp"

# Perform Clip Analysis
arcpy.analysis.Clip(
    input_fc,
    clip_fc,
    output_fc
)

print("Clip completed successfully.")
