import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Update STATUS Field
with arcpy.da.UpdateCursor(input_fc, ["STATUS"]) as cursor:
    for row in cursor:
        row[0] = "Verified"
        cursor.updateRow(row)

print("Records Updated Successfully")
