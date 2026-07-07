import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Fields to Insert
fields = ["GAT_NO", "OWNER"]

# Insert New Record
with arcpy.da.InsertCursor(input_fc, fields) as cursor:
    cursor.insertRow([101, "Nandraj"])

print("Record Inserted Successfully")
