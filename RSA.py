from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from nilearn.image import new_img_like
import pandas as pd
import nibabel as nib
import seaborn as sns
from nilearn import plotting
from rsatoolbox.inference import eval_fixed
from rsatoolbox.model import ModelFixed
from rsatoolbox.rdm import RDMs
from glob import glob
from rsatoolbox.util.searchlight import get_volume_searchlight, get_searchlight_RDMs, evaluate_models_searchlight
import matplotlib
import masking as mask
import nilearn as nil;
from rsatoolbox.rdm import compare
from nilearn.masking import _apply_mask_fmri
import os
import rsatoolbox
from nilearn.plotting import plot_roi
from nilearn.masking import compute_epi_mask
from nilearn.masking import apply_mask
from scipy import signal
import rsatoolbox.data as rsad
from rsatoolbox.rdm import get_categorical_rdm
from rsatoolbox import vis
#-------------------DATA   ---------------------------------------
#------Choisir la dossier pour le singe ------------
data_folder = 'Data/new/corr'

image_paths = list(glob(f"{data_folder}/*.nii"))
image_paths.sort()

# ---------- importing data -------------
num_images = len(image_paths)
images = []

for i in range(num_images):
    img = nib.load(image_paths[i])
    images.append(img)

data=nib.concat_images(images)
mask_img=nib.load(r'D:\shabnam\DESU\Projet\Data\newmask.nii.gz')


data_masked = apply_mask(data, mask_img)



# -----------------------------------------
data_new = rsatoolbox.data.Dataset(data_masked)
rdms = rsatoolbox.rdm.calc_rdm(data_new, method='correlation')
print(rdms)
index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
conditions=["speech female","speech male","non-speech female","non-speech male","coo","grunt","aggressive","scream","trill","phee","twitter","tsik","natural living","natural non-living","artificial living","artificial non-living"]
condition=['speech female','speech male','non-speech female','non-speech male','oo','grunt','aggressive','scream','trill','phee','twitter','tsik','natural living','natural non-living','artificial living','artificial non-lliving']
rsatoolbox.vis.show_rdm(rdms, cmap='YlGnBu', rdm_descriptor='RDM',show_colorbar='panel',figsize=(15,5))

fig= rsatoolbox.vis.show_rdm(rdms,
             rdm_descriptor='RDM',
             show_colorbar='panel' ,figsize=(15,5))
None

from nilearn import datasets
from nilearn.image.image import mean_img
from nilearn.plotting import plot_epi, show
# masked_data shape is (timepoints, voxels). We can plot the first 150
# timepoints from two voxels

# And now plot a few of these
import matplotlib.pyplot as plt
print('pour percy')

#np.savetxt(r'D:\shabnam\PhD\myfile.csv', x, delimiter=',')
image_paths = list(glob(f"{data_folder}/*.nii"))
file_name_table = []
for file_path in image_paths:
    normalized_path = os.path.normpath(file_path)
    file_name = os.path.splitext(os.path.basename(normalized_path))[0]
    file_name_table.append(file_name)