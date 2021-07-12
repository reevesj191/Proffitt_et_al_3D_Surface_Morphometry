########################################################################################################################
# Title: Find Perimeter                                                                                                #
# Author: Jonathan S. Reeves                                                                                           #
# Summary: Calculates the perimeter of a 3D surface with easily defined edges.                                         #
########################################################################################################################

import pyvista as pv
from Vector_functions import perimeter
import os
from pandas import DataFrame

proj_path = "D:/TechPrim_Working/BNE All Stars/Methods Data/Data/UNK3_Area and Perim"
Out_Path = "User Defined"
model_names = os.listdir(proj_path)

model_names = [name for name in model_names if not name.endswith("xyz")]

perims = []

for name in model_names:
    print(name)
    model_path = os.path.join(proj_path, name)
    mesh = pv.read(model_path)
    #mesh=mesh.fill_holes(hole_size=.001)
    #mesh.plot()
    mesh.extract_feature_edges(boundary_edges=True,
                           non_manifold_edges=True,
                           feature_edges=False,
                           manifold_edges=False,
                                   inplace=True,
                               feature_angle=10)
    #mesh.plot()
    p = perimeter(points=mesh.points,
          line_idx= mesh.lines)

    perims.append({"name": name,
                    "perimeter": p})

    perimeter(points=mesh.points,
          line_idx= mesh.lines)

sheet = DataFrame(perims)
sheet.to_csv("D:/TechPrim_Working/BNE All Stars/Methods Data/Data/UNK3_Area and Perim/UNK3_perimeter.csv")


