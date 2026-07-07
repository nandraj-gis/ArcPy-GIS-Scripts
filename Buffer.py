import arcpy

input_fc = r"C:\GIS\Village.shp"
output_fc = r"C:\GIS\Village_Buffer.shp"

arcpy.analysis.Buffer(
    input_fc,
    output_fc,
    "100 Meters"
)

print("Buffer Created Successfully")
