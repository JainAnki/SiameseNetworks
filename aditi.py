#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:00:36 2020

@author: ankita
"""
# import the necessary packages
from tensorflow.keras.datasets import mnist
from imutils import build_montages
import numpy as np
import cv2
import os
import zipfile
from PIL import Image

print("[INFO] loading MNIST dataset...")
data = mnist.load_data()
a = data[0][0]
b = data[0][1]


local_zip = '/home/ankita/Downloads/Aditi.zip'

zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()
base_dir = '/home/ankita/Downlo0ads/Aditi.zip'

import os
path = '/Users/myName/Desktop/directory'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.png'])))

im = Image.open('Aditi/1.png')

print(im.size)
print(type(im.size))
# (400, 225)
# <class 'tuple'>

w, h = im.size
print('width: ', w)
print('height:', h)
# width:  400
# height: 225

