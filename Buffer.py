import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Output Feature Class
output_fc = r"C:\GIS\Village_Buffer.shp"

# Create 100 Meter Buffer
arcpy.analysis.Buffer(
    input_fc,
    output_fc,
    "100 Meters"
)

print("Buffer Created Successfully")
