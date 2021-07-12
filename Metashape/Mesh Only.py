########################################################################################################################
# Title: Mesh Only                                                                                                     #
# Author: Jonathan S. Reeves                                                                                           #                #
########################################################################################################################

import Metashape
import os

proj_path = "E:/Tomos_Data/Photogrammetry/"
align_path = os.path.join(proj_path, "To_Mesh_Standard")
model_names = os.listdir(align_path)
# model_names.remove('.DS_Store')
nameext = ".psx"
#target_path = os.path.join(proj_path, "To_MDM_Export")

for name in model_names:
    model_path = os.path.join(align_path, name)

    doc = Metashape.app.document

    doc.open(os.path.join(model_path, name + nameext))

    chunk3 = doc.chunks[2]



    ## Build Mesh

    print("building Mesh")

    chunk3.buildModel(face_count = Metashape.FaceCount.CustomFaceCount, 
    face_count_custom=8000000)
    
    
    doc.save()
    
    sa = chunk3.model.area() * 10000
    
    new_face_count = sa * 20000
    
    standard_mesh = chunk3.copy()
    
    if new_face_count >= 8000000:
        
        standard_mesh.buildModel(face_count = Metashape.FaceCount.CustomFaceCount,
        face_count_custom=new_face_count)
        
    else:
        
        standard_mesh.decimateModel(face_count=new_face_count)

        
    doc.save()

    
