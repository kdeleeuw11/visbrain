"""
Parcellize brain surface
========================

Parcellize the brain surface using .annot files. This example use Nibabel to
read the .annot file.

See https://surfer.nmr.mgh.harvard.edu/fswiki/CorticalParcellation for files
used in this example.

.. image:: ../../picture/picbrain/ex_parcellates.png
"""
import numpy as np

from visbrain import Brain
from visbrain.objects import BrainObj
from visbrain.io import download_file, path_to_visbrain_data


file1 = 'lh.aparc.a2009s.annot'
file2 = 'rh.aparc.annot'

# Download files if needed :
download_file(file1)
download_file(file2)

# Get the path to the files :
path_to_file1 = path_to_visbrain_data(file1)
path_to_file2 = path_to_visbrain_data(file2)

# Define a brain object :
b_obj = BrainObj('inflated', hemisphere='both', translucent=False)

"""Parcellize the left hemisphere using the Destrieux Atlas. By default, no
parcellates are selected
"""
b_obj.parcellize(path_to_file1, hemisphere='left')

"""If you want to get the list of all predefined parcellates, use the
`get_parcellates` method which returns a pandas DataFrame with the index, the
name and the color associated to each parcellates
"""
df = b_obj.get_parcellates(path_to_file2)
# print(df)

"""Select only some parcellates. Note that this parcellization is using an
other atlas (Desikan-Killiany atlas)
"""
select = ['insula', 'paracentral', 'precentral', 'precuneus', 'frontalpole',
          'temporalpole', 'fusiform', 'cuneus', 'inferiorparietal',
          'inferiortemporal', 'precentral', 'superiorfrontal',
          'superiortemporal']

"""Instead of using predefined colors inside the annot file, we use some data
"""
data = np.arange(len(select))
b_obj.parcellize(path_to_file2, hemisphere='right', select=select, data=data,
                 cmap='Spectral_r')

"""Finally, pass the brain object to `Brain` and disply the GUI
"""
Brain(brain_obj=b_obj).show()
