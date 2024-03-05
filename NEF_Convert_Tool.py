#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Wrote this program because I couldn't find a good online converter for free and I'm a hustler like dat."""
import rawpy
import imageio
import os

# Defining the folder containing the .nef files
nef_path = 'C:/Users/fiona/Downloads/uploadimages1'
jpeg_path = 'C:/Users/fiona/Downloads/Fire_Dataset_1'

# Checking if JPEG folder exists, if not creating it
if not os.path.exists(jpeg_path):
    os.makedirs(jpeg_path)

# Iterating over each file in the folder
for filename in os.listdir(nef_path):
    if filename.lower().endswith('.nef'):
        # Constructing full file path
        nef_path = os.path.join(nef_path, filename)
        jpeg_path = os.path.join(jpeg_path, os.path.splitext(filename)[0] + '.jpg')
        
        # Processing the NEF file
        with rawpy.imread(nef_path) as raw:
            rgb = raw.postprocess()
        
        # Saving the image as JPEG
        imageio.imwrite(jpeg_path, rgb)
        print(f"Successfully converted {filename} to JPEG and saved to {jpeg_path}")


# In[ ]:




