import arcpy

# Input Feature Class
input_fc = r"C:\GIS\Village.shp"

# Fields to Read
fields = ["GAT_NO", "OWNER"]

# Read Records
with arcpy.da.SearchCursor(input_fc, fields) as cursor:
    for row in cursor:
        print("GAT NO :", row[0])
        print("OWNER  :", row[1])
        print("-" * 30)

print("Search Completed Successfully")
