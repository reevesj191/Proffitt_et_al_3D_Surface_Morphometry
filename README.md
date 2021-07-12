# READ ME

DISCLAIMER: THIS WORK IS CURRENTLY UNDER REVIEW. PLEASE DO NOT CITE OR PUBLISH THE DATA, CODE, OR OTHER INFORMATION IN THE REPOSITORY WITHOUT THE APPROVED WRITTEN CONSENT OF THE AUTHORS

## Using these Scripts

The scripts maintained in the respository are those used in the workflow associated with the paper entitled: **3D surface morphometrics differentiates behaviour on primate stone tools**. These scripts can be used to generate and analyze 3D models of percussive tools. 

Examples of models and file structure needed to carry out the analysis are provided. 

### Metashape

#### Dependencies

These scripts require the Metashape python library. This is a propriety package that can be downloaded from the Agisoft website directly. Please follow their instructions on how to properly install this library. Alternatively, these scripts can also be run from within Metashape using *run script* in the "Tools" dropdown menu. 

#### File Structure

Each script in this folder follows a very specific file structure. Photos associated with the 3D models should be kept in individual folders use their associated ID as the name of the folder. It is important that the folders for each specimen are all contained within a "Project folder". The path way to this folder should then be defined in the script. This is because the script will iterate through and generate a metashape project file for each folder of photos within the "Project Folder". 

See the file structure for the files and folders within the "Examples" directory for reference. This folder provides photos and file structure necessary to excecute these scripts. 

#### Order of Scrips 

The scripts should be run in the following order.

1. Pgram_Batch.py: This will load, mask, align photos and build the dense cloud for each chunk.
2. Mesh Only.py: Constructs the mesh from the dense cloud
3. Texture_Only.py: Constructs texture

Dense_Only.py can be used compute the dense cloud from aligned photos.  

### 3D Morphometry

See "example" directory for file structure. 

### Known Bugs Errors, Corrections

Forthcoming
