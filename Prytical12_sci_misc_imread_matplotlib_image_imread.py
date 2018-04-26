#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:27:55 2018
load_img:
    1)scipy.misc.imread() or matplotlib.image.imread()
    2)os.path.exists
@author: yongweiw
"""

import numpy as np
from os.path import exists
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def load_img(image_path):
    assert exists(image_path), "image {} does not exist".format(image_path)
    img = imread(image_path)
#    img = img.astype("float32")
#    img = np.ndarray.reshape(img, (1,) + img.shape)
    return img


def imread(path):
    return scipy.misc.imread(path)
#    return mpimg.imread(path)
#    return mpimg.imread(path).astype(np.float)
#    return scipy.misc.imread(path).astype(np.float)

dir_img = 'cat.jpg'
img = load_img(dir_img) 
print(np.shape(img))

# show the image read from dir_img
plt.figure()
plt.imshow(img)
plt.show()