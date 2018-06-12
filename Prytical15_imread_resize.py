# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:13:39 2018
Functions:
1) Read all images from an image directory, specified by root,
2) Then resize the images one by one to a given size, specified by resize_size.

   scipy.misc.imread(/path/to/image/.image_extension)
   scipy.misc.imresize(image_to_resize, (resize_size, resize_size))
   scipy.misc.imsave(save_root + name, arr=img_data)
   
   Also you can refer to:  matplotlib.pyplot.imread, imresize, imsave

@author: Yongwei
"""

import os
from scipy.misc import imread, imresize, imsave

root = '/path/to/Dataset_original'
save_root = '/path/to/Dataset_resized/'

resize_size = 128

# check directory
if not os.path.isdir(save_root):
    os.mkdir(save_root)

img_list = os.listdir(root)  
# print(img_list) #img_list contains complete name of each image, e.g.,t1.bmp, t2.bmp...

for i in range(len(img_list)):
    img = imread(root + img_list[i])
    img = imresize(img, (resize_size, resize_size))
    
    imsave(save_root + img_list[i], arr=img)
    
    if (i+1) % 10 == 0:
        print ('%d images complete' % (i+1))

         
