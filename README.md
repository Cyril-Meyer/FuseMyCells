# FuseMyCells `🔬+🤖 = 2×🔬`
France-BioImaging's Fuse My Cells challenge

Link to the challenge for more information :
* [fusemycells.grand-challenge.org](https://fusemycells.grand-challenge.org/)
* [france-bioimaging.org announcement](https://france-bioimaging.org/announcement/france-bioimaging-challenge-is-back-fuse-my-cells/)


## Results
For now, no results at all.


## Usage

### Prepare dataset

1. Download the dataset zip files un put all of them in
a folder. The following instruction need to be executed
from this folder.
2. Run script `01_unzip.py`
    * Notes: the scripts for data prepration are located
      in the `data` folder.
3. Run script `02_tif_to_hdf5.py`

Now, the zip files have been extracted to an `images` folder
and then put in a single file named `FuseMyCells.hdf5`.


## Changelog

#### 17/01/2025

* Working on data acquisition and preprocessing
  * script to unzip all the data at once
  * script to convert all the images into a single HDF5 file for easier load


## Current idea

* 2D and 3D U-Net
* Multiple scale prediction
* Diffusion model
  * learn noise to image
  * predict image to image
* Merge multiple methods
* Morphological neural network (max+ convolutions) post processing
