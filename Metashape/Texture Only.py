########################################################################################################################
# Title: Texture Only                                                                                                     #
# Author: Jonathan S. Reeves                                                                                           #                #
########################################################################################################################

import Metashape
import os

proj_path = "E:/Tomos_Data/Photogrammetry/"
align_path = os.path.join(proj_path, "To_Texture")
model_names = os.listdir(align_path)
# model_names.remove('.DS_Store')
nameext = ".psx"
#target_path = os.path.join(proj_path, "To_MDM_Export")

for name in model_names:
    model_path = os.path.join(align_path, name)

    doc = Metashape.app.document

    doc.open(os.path.join(model_path, name + nameext))

    chunk3 = doc.chunks[2]


    print("building texture")

    chunk3.buildUV(mapping_mode=Metashape.GenericMapping)
    chunk3.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=4096)

    doc.save()
