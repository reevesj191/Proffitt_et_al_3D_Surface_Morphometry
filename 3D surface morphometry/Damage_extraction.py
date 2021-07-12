########################################################################################################################
# Title: Damage Extraction Script                                                                                      #
# Author: Jonathan S. Reeves                                                                                           #
# Summary: This is used pair surface morphometry data with the 3D models representing the damaged regions of the       #
# nodule. KDTrees are used to assign values from one 3D model to the closest vertex of another model.                  #
########################################################################################################################

import os
import pandas as pd
import pyvista as pv
from scipy.spatial import KDTree

print("Damage?")
Damage = input()
print("Behaviour?")
Behaviour = input()

#Folder than contains all other folders with models
project_path = "C:/Users/tomos_proffitt/Desktop/Methods Paper Data Extraction/Data/Unmodified to Extract/S Shell"
models = os.listdir(project_path)
print(models)
data_compile = {"Tool_ID": [],
                    "Segment":[],
                    "x": [], # here
                    "y": [],
                    "z": [],
                    "Depth": [],
                    "Mean_Depth": [],
                    "TPI": [],
                    "Roughness": [],
                    "Mean_Curvature": [],
                    "Slope": [],
                    "Damage": [],
                    "Behaviour": []}
data_compile = pd.DataFrame(data_compile)

for name in models:
    model_path = os.path.join(project_path,name)
    files = os.listdir(model_path)
    stone = [x for x in files if x.endswith("Surface Analysis.xyz")] ### Make sure that your full model ends with the string writing.

    full_mesh_path = os.path.join(model_path,stone[0])
    full_mesh_csv = pd.read_csv(full_mesh_path)

    ### Calculate Convex Hull Distances

    xyz_array = full_mesh_csv[["//X", "Y", "Z"]].to_numpy()
    full_mesh = pv.PolyData(xyz_array)


    #full_mesh["CH_distances"] = convex_hull_distances(xyz_array)

    full_mesh["Depth"] = full_mesh_csv[["C2M signed distances"]]
    full_mesh["Mean_Depth"] = full_mesh_csv[["C2M signed distances.smooth(0.005)"]]
    full_mesh["TPI"] = full_mesh_csv[['(SF#0) - (SF#1)']]
    full_mesh["Roughness"] = full_mesh_csv[["Roughness (0.0005)"]]
    full_mesh["Mean_Curvature"] = full_mesh_csv[['Mean curvature (0.0005)']]
    full_mesh["Slope"] = full_mesh_csv[["Gradient norms(C2M signed distances)"]]

    ### Load Damage files
    damage_files = [x for x in files if not x.endswith("Surface Analysis.xyz") and not x.endswith("xyz")]

    damage = []

    for model in damage_files:
        x = pv.read(os.path.join(model_path,model))
        damage.append(x)

    for pos in range(len(damage)):

        x = damage[pos]
        seg = damage_files[pos]
        print(seg)
        tree = KDTree(x.points)
        d, idx = tree.query(full_mesh.points)
        full_mesh["d2damage"] = d
        damaged = full_mesh.clip_scalar(scalars="d2damage",
                                        value=.00015)


        data_dict = {"Tool_ID": name,
                     "Segment": seg,
                     "x": damaged.points[:,0],
                     "y": damaged.points[:,1],
                     "z": damaged.points[:,2],
                     "Depth": damaged["Depth"],
                     "Mean_Depth": damaged["Mean_Depth"],
                     "TPI": damaged["TPI"],
                     "Roughness": damaged["Roughness"],
                     "Mean_Curvature": damaged["Mean_Curvature"],
                     "Slope": damaged["Slope"],
                     "Damage": Damage,
                     "Behaviour": Behaviour}

        data_dict = pd.DataFrame(data_dict)
        data_compile = data_compile.append(data_dict,
                                           ignore_index=True)



data_compile.to_csv(os.path.join(model_path,"%s.csv" % name))


