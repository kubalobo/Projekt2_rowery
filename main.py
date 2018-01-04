import arcpy
import os

arcpy.CheckOutExtension("spatial")

PATH = os.path.dirname(os.path.abspath(__file__))
dataPATH = PATH + "Data"
arcpy.env.workspace = PATH
arcpy.env.cellSize = 5
arcpy.env.overwriteOutput = True


# ================= Bicycle path =================
path_cyclePath1 = "\.shp"
