#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 21:18:47 2018
two methods of reading and writing images from/to files. 
Note that, .imread(*arg, **args), *arg is in string format.
1)np.clip(data, val_min, val_max), clip values within interval [val_min, val_max]
2)scipy.misc: .imread(), imsave(image_name_in_string_format, data)
3)imageio: imwrite()
@author: yongwei
"""

import numpy as np

from scipy.misc import imsave
from imageio import imwrite

"********************* clip *********************"
data = np.arange(10)
print("original data:", data)

val_min = 3
val_max = 8
data_ = np.clip(data, val_min, val_max)
print("clipped data:", data_)

"create rgb data"
rgb = np.zeros((255, 255, 3), dtype=np.uint8)
rgb[...,0] = np.arange(255)
rgb[...,1] = 55
rgb[...,2] = 1 - np.arange(255)

"********************* scipy.misc.imsave *********************"
#imsave('rgb_gradient.png', rgb)


"********************* imageio.imwrite *********************"
#imwrite('~/Documents/rgb_img.png', rgb)
imwrite('rgb_img.png', rgb)



