########################################################################################################################
# Title: Extract Convex Hull Script                                                                                    #
# Author: Jonathan S. Reeves                                                                                           #
# Summary: This is a variation of the extract damage script specifically to be used to extract data from a convex hull #
# and assign it to another 3D model (i.e. damaged areas)                                                               #
########################################################################################################################

import os
import pandas as pd
import pyvista as pv
from scipy.spatial import KDTree
print("Tool_ID?")
Tool_ID = input()
print("Damage?")
Damage = input()
print("Behaviour?")
Behaviour = input()

model_path = "C:/Users/tomos_proffitt/Desktop/Methods Paper Data Extraction/Data/Unmodified to Extract/Curvature Morphology to Extract/Thais/ETTB"
files = os.listdir(model_path)
chull = [x for x in files if x.endswith("CH_Morph.xyz")] ### Make sure that your full model ends with the string writing.

CHULL_path = os.path.join(model_path,chull[0])
chull_csv = pd.read_csv(CHULL_path)


xyz_array = chull_csv[["//X", "Y", "Z"]].to_numpy()
chull = pv.PolyData(xyz_array)

chull["curvature"] = chull_csv[["Mean curvature"]]

damage_files = [x for x in files if not x.endswith("Surface Analysis.xyz") and not x.endswith("xyz")]

damage = []

for model in damage_files:
    x = pv.read(os.path.join(model_path,model))
    damage.append(x)

data_compile = {"Segment": [],
                "x": [], # here
                "y": [],
                "z": [],
                "plane curvature": []}

data_compile = pd.DataFrame(data_compile)

for pos in range(len(damage)):

    x = damage[pos]
    name = damage_files[pos]
    tree = KDTree(chull.points)
    d, idx = tree.query(x.points, k=1)


    data_dict = {"Segment": name,
                 "x": x.points[:,0],
                 "y": x.points[:,1],
                 "z": x.points[:,2],
                 "plane curvature": chull["curvature"][idx],
                 "Damage": Damage,
                 "Behaviour": Behaviour,
                 "Tool_ID": Tool_ID}
                 
             
    data_dict = pd.DataFrame(data_dict)
    data_compile = data_compile.append(data_dict,
                                       ignore_index=True)

data_compile.to_csv(os.path.join(model_path,
                                 "Plane_Morph_curvature.csv"))

##############################

print("Tool_ID?")
Tool_ID = input()
print("Damage?")
Damage = input()
print("Behaviour?")
Behaviour = input()

model_path = "C:/Users/tomos_proffitt/Desktop/Methods Paper Data Extraction/Data/Unmodified to Extract/Curvature Morphology to Extract/Thais/ETTB7"
files = os.listdir(model_path)
chull = [x for x in files if x.endswith("CH_Morph.xyz")] ### Make sure that your full model ends with the string writing.

CHULL_path = os.path.join(model_path,chull[0])
chull_csv = pd.read_csv(CHULL_path)


xyz_array = chull_csv[["//X", "Y", "Z"]].to_numpy()
chull = pv.PolyData(xyz_array)

chull["curvature"] = chull_csv[["Mean curvature"]]

damage_files = [x for x in files if not x.endswith("Surface Analysis.xyz") and not x.endswith("xyz")]

damage = []

for model in damage_files:
    x = pv.read(os.path.join(model_path,model))
    damage.append(x)

data_compile = {"Segment": [],
                "x": [], # here
                "y": [],
                "z": [],
                "plane curvature": []}

data_compile = pd.DataFrame(data_compile)

for pos in range(len(damage)):

    x = damage[pos]
    name = damage_files[pos]
    tree = KDTree(chull.points)
    d, idx = tree.query(x.points, k=1)


    data_dict = {"Segment": name,
                 "x": x.points[:,0],
                 "y": x.points[:,1],
                 "z": x.points[:,2],
                 "plane curvature": chull["curvature"][idx],
                 "Damage": Damage,
                 "Behaviour": Behaviour,
                 "Tool_ID": Tool_ID}
                 
             
    data_dict = pd.DataFrame(data_dict)
    data_compile = data_compile.append(data_dict,
                                       ignore_index=True)

data_compile.to_csv(os.path.join(model_path,
                                 "Plane_Morph_curvature.csv"))

##############################
##############################

print("Tool_ID?")
Tool_ID = input()
print("Damage?")
Damage = input()
print("Behaviour?")
Behaviour = input()

model_path = "C:/Users/tomos_proffitt/Desktop/Methods Paper Data Extraction/Data/Unmodified to Extract/Curvature Morphology to Extract/Thais/TTB9"
files = os.listdir(model_path)
chull = [x for x in files if x.endswith("CH_Morph.xyz")] ### Make sure that your full model ends with the string writing.

CHULL_path = os.path.join(model_path,chull[0])
chull_csv = pd.read_csv(CHULL_path)


xyz_array = chull_csv[["//X", "Y", "Z"]].to_numpy()
chull = pv.PolyData(xyz_array)

chull["curvature"] = chull_csv[["Mean curvature"]]

damage_files = [x for x in files if not x.endswith("Surface Analysis.xyz") and not x.endswith("xyz")]

damage = []

for model in damage_files:
    x = pv.read(os.path.join(model_path,model))
    damage.append(x)

data_compile = {"Segment": [],
                "x": [], # here
                "y": [],
                "z": [],
                "plane curvature": []}

data_compile = pd.DataFrame(data_compile)

for pos in range(len(damage)):

    x = damage[pos]
    name = damage_files[pos]
    tree = KDTree(chull.points)
    d, idx = tree.query(x.points, k=1)


    data_dict = {"Segment": name,
                 "x": x.points[:,0],
                 "y": x.points[:,1],
                 "z": x.points[:,2],
                 "plane curvature": chull["curvature"][idx],
                 "Damage": Damage,
                 "Behaviour": Behaviour,
                 "Tool_ID": Tool_ID}
                 
             
    data_dict = pd.DataFrame(data_dict)
    data_compile = data_compile.append(data_dict,
                                       ignore_index=True)

data_compile.to_csv(os.path.join(model_path,
                                 "Plane_Morph_curvature.csv"))

##############################
##############################

print("Tool_ID?")
Tool_ID = input()
print("Damage?")
Damage = input()
print("Behaviour?")
Behaviour = input()

model_path = "C:/Users/tomos_proffitt/Desktop/Methods Paper Data Extraction/Data/Unmodified to Extract/Curvature Morphology to Extract/Thais/TTB11"
files = os.listdir(model_path)
chull = [x for x in files if x.endswith("CH_Morph.xyz")] ### Make sure that your full model ends with the string writing.

CHULL_path = os.path.join(model_path,chull[0])
chull_csv = pd.read_csv(CHULL_path)


xyz_array = chull_csv[["//X", "Y", "Z"]].to_numpy()
chull = pv.PolyData(xyz_array)

chull["curvature"] = chull_csv[["Mean curvature"]]

damage_files = [x for x in files if not x.endswith("Surface Analysis.xyz") and not x.endswith("xyz")]

damage = []

for model in damage_files:
    x = pv.read(os.path.join(model_path,model))
    damage.append(x)

data_compile = {"Segment": [],
                "x": [], # here
                "y": [],
                "z": [],
                "plane curvature": []}

data_compile = pd.DataFrame(data_compile)

for pos in range(len(damage)):

    x = damage[pos]
    name = damage_files[pos]
    tree = KDTree(chull.points)
    d, idx = tree.query(x.points, k=1)


    data_dict = {"Segment": name,
                 "x": x.points[:,0],
                 "y": x.points[:,1],
                 "z": x.points[:,2],
                 "plane curvature": chull["curvature"][idx],
                 "Damage": Damage,
                 "Behaviour": Behaviour,
                 "Tool_ID": Tool_ID}
                 
             
    data_dict = pd.DataFrame(data_dict)
    data_compile = data_compile.append(data_dict,
                                       ignore_index=True)

data_compile.to_csv(os.path.join(model_path,
                                 "Plane_Morph_curvature.csv"))

##############################

