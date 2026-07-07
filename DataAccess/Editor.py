import arcpy

# Geodatabase Workspace
workspace = r"C:\GIS\MyDatabase.gdb"

# Start Editing Session
editor = arcpy.da.Editor(workspace)

editor.startEditing(False, True)
editor.startOperation()

print("Editing Started Successfully")

# Stop Editing Session
editor.stopOperation()
editor.stopEditing(True)

print("Editing Saved Successfully")
