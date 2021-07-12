########################################################################################################################
# Title: Dense Cloud Only                                                                                              #
# Author: Jonathan S. Reeves                                                                                           #
########################################################################################################################

import Metashape
import os

proj_path = "Y:/common/Tom/"
align_path = os.path.join(proj_path, "To_Dense")
model_names = os.listdir(align_path)
#model_names.remove('.DS_Store') ## Uncomment this if you are using a mac.
nameext = ".psx"
target_path = os.path.join(proj_path, "To_MDM_Export")

for name in model_names:

    model_path = os.path.join(align_path, name)

    doc = Metashape.app.document

    doc.open(os.path.join(model_path, name + nameext))

    chunk1 = doc.chunks[0]
    chunk2 = doc.chunks[1]

    ## Build Dense Cloud

    print("building Depth Maps")

    chunk1.buildDepthMaps(downscale=2)
    chunk2.buildDepthMaps(downscale=2)
    doc.save()
    
    print("building Dense Cloud")

    chunk1.buildDenseCloud()
    chunk2.buildDenseCloud()
    doc.save()

