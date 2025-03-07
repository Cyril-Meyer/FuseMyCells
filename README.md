# FuseMyCells `🔬+🤖 = 2×🔬`
France-BioImaging's Fuse My Cells challenge

Link to the challenge for more information :
* [fusemycells.grand-challenge.org](https://fusemycells.grand-challenge.org/)
* [france-bioimaging.org announcement](https://france-bioimaging.org/announcement/france-bioimaging-challenge-is-back-fuse-my-cells/)


## Results

* [test_phase/leaderboard](https://fusemycells.grand-challenge.org/evaluation/test_phase/leaderboard/)
  * closed 07/03/2025 (initial date 28/02/2025)
* [evaluation/leaderboard](https://fusemycells.grand-challenge.org/evaluation/evaluation/leaderboard/)

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


## Method

Taking the [docker_template](https://seafile.lirmm.fr/d/233a5a399c8544dfb41a/) given by the organizer as a start point.

```python
from scipy import ndimage
if metadata['channel'] == 'nucleus':
    image_predict = ndimage.gaussian_filter(image_input, 0.442)
else:
    image_predict = ndimage.gaussian_filter(image_input, 0.5)
```

The filter sigma values have been manually selected from evaluation on the training dataset.


## Changelog

#### 07/03/2025

* Add result used to specify methods
* Update README (add method)

#### 28/02/2025

* Adding evaluation of method script
  * usage for classical computer vision methods
* Update README (put my exp results in the idea section)

#### 17/01/2025

* Working on data acquisition and preprocessing
  * script to unzip all the data at once
  * script to convert all the images into a single HDF5 file for easier load


## Ideas

* Merge multiple methods
  * Average of the two best methods ?

### Classical computer vision

* Simple filters
  * Gaussian filter with `sigma=0.5` is the best result for now.
  * Wavelet, test in progress, looks promising.
  * Total variation (Bregmann) worse than nothing.
* Simple morphological filters
  * Ball erosion / dilation / opening / closing : worse than nothing.

### Machine Learning (non deep but learning)

* Learned convolution (single layer and single / multiple kernel)
  * Not tested yet.
* Single learned morphological neural network
  * Worse than nothing.

### Deep Learning

* 2D and 3D U-Net
  * Worse than nothing.
* Multiple scale prediction
  * Best results seems to show that the smallest the context is, the best
    are the results.
* Morphological neural network (max+ convolutions) post processing
  * Single layers seems the "less bad"
* Diffusion model (learn noise to image / predict image to image)
  * TLDT (too long didn't test)


## Requirements

```
h5py==3.12.1
numpy==2.2.1
tifffile==2025.1.10

scipy==1.15.2
scikit-image==0.25.2
PyWavelets==1.8.0

tensorflow==2.18.0
```
