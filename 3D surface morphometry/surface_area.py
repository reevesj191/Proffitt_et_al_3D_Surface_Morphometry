########################################################################################################################
# Title: Find Perimeter                                                                                                #
# Author: Jonathan S. Reeves                                                                                           #
# Summary: Extracts area of surface.                                                                                   #
########################################################################################################################

import trimesh
import os
from pandas import DataFrame


proj_path = "D:/TechPrim_Working/BNE All Stars/Methods Data/Data/UNK3 CH"
model_names = os.listdir(proj_path)


extents = []

for name in model_names:

    model_path = os.path.join(proj_path, name)
    mesh = trimesh.load(model_path)
    exts = mesh.bounding_box.extents
    print(model_path)
    extents.append({"name": name,
                    "area": mesh.area})


sheet = DataFrame(extents)
sheet.to_csv("D:/TechPrim_Working/BNE All Stars/Methods Data/Data/UNK3 CH")

