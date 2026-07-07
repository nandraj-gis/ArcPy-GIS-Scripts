import arcpy

fc = r"C:\GIS\Village.shp"

fields = ["GAT_NO", "OWNER"]

with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        print("GAT NO :", row[0])
        print("OWNER  :", row[1])
        print("-" * 30)
