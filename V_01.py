import arcpy
from arcpy import env
from arcpy.sa import *
import os


interval = 0.2
catalog = "01_Tmean_years"
end_catalog = "01_iso_Tmean_years"
iso_index = str(interval).split('.')[0] + 'p' + str(interval).split('.')[1]

flt_dir = "C:\\Users\\g.gvozdik\\Desktop\\to_olya\\Group_Isolines\\" + catalog
save_dir = "C:\\Users\\g.gvozdik\\Desktop\\to_olya\\Group_Isolines\\" + end_catalog
print "data way: " + flt_dir
print "save way: " + save_dir


flt_list = []

for roots, dirs, files in os.walk(flt_dir + '\\'):
    i = 0
    for file in files:
        if file.endswith('.flt'):
            flt_list.append(file)

            print "file " + str(i) + ": " + flt_list[-1]
            i += 1

i = 1


for flt in flt_list:

    Contour(flt_dir + '\\' + flt,
            save_dir + '\\' + "01" + "_" + str(catalog).split('_')[0] + '_' + str(i) + "_" + iso_index + ".shp",
            interval, 0, 1)


    i += 1


