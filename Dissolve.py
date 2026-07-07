import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Output Feature Class
output_fc = r"C:\GIS\Village_Dissolve.shp"

# Dissolve Field
dissolve_field = "District"

# Perform Dissolve Analysis
arcpy.analysis.Dissolve(
    input_fc,
    output_fc,
    dissolve_field
)

print("Dissolve completed successfully.")
