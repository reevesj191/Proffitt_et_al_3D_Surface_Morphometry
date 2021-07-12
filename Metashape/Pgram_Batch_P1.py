########################################################################################################################
# Title: Batch Align                                                                                                   #
# Author: Jonathan S. Reeves                                                                                           #                #
########################################################################################################################

import Metashape
import os

Align_Acc = 0  # a number from 0 to 5 that sets the accuracy of the alignment.
Dense_Res = 0  # a number from 0 to 5 that sets the resolution of the dense cloud.

proj_path = "E:/Tomos_Data/Photogrammetry"
align_path = os.path.join(proj_path, "To_Align")
model_names = os.listdir(align_path)
#model_names.remove('.DS_Store') # Uncomment if using a mac.
nameext = ".psx"
target_path = os.path.join(proj_path, "To_MDM_Export")


### Generate Psx Files
for name in model_names:

    model_path = os.path.join(align_path, name)
    doc = Metashape.app.document
    doc.remove(doc.chunks)
    doc.save(os.path.join(model_path, name + nameext))



for name in model_names:

  model_path = os.path.join(align_path, name)

  doc = Metashape.app.document

  doc.open(os.path.join(model_path, name + nameext))


  top = doc.addChunk()
  bottom = doc.addChunk()
  top_path = os.path.join(model_path,"Top")
  bottom_path = os.path.join(model_path, "Bottom")

  mask_path = os.path.join(model_path,"Masks")


# load top images

  img_list = os.listdir(top_path)
  img_paths = []
  for img in img_list:
    img_paths.append(os.path.join(top_path,img))
  top.addPhotos(img_paths)

# load bottom images

  img_list = os.listdir(bottom_path)
  img_paths = []
  for img in img_list:
    img_paths.append(os.path.join(bottom_path,img))

  bottom.addPhotos(img_paths)

  doc.save()


## Load Masks

  top.importMasks(path = os.path.join(mask_path, "{filename}.png"),
 source=Metashape.MaskSourceFile)

  bottom.importMasks(path = os.path.join(mask_path, "{filename}.png"),
  source=Metashape.MaskSourceFile)

  doc.save()

## align Photos

  top.matchPhotos(downscale=0,
                  generic_preselection=True,
                  filter_mask=True)### change to 0 for highest
  top.alignCameras()
  bottom.matchPhotos(downscale=0,
                     generic_preselection=True,
                     filter_mask = True)
  bottom.alignCameras()

## Make bounding box huge

  top.region.size = Metashape.Vector([100,100,100])
  bottom.region.size = Metashape.Vector([100,100,100])

  doc.save()
  
## Build Dense Cloud

  print("building Depth Maps")

  top.buildDepthMaps(downscale=2)
  bottom.buildDepthMaps(downscale=2)
  doc.save()
    
  print("building Dense Cloud")

  top.buildDenseCloud()
  bottom.buildDenseCloud()
  doc.save()





