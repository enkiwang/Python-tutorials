# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:18:17 2018
 sim (x_i, x_j) with RBF
 K(x,x') = exp (- squre(x-x')/2/sigma^2)
@author: Yongwei
"""

import numpy as np
import os
from scipy.misc import imread, imresize
from math import exp 

root = 'C:/Users/Yongwei/Downloads/faces/'

resize_size = 64

img_list = os.listdir(root)

img_num = 10  # images to load 
imgs = np.zeros([img_num, resize_size*resize_size])

rbf_dist = np.zeros([img_num -1])  

# pre-processing functions
def im2double(img):
    min_val = np.min(img.ravel())
    max_val = np.max(img.ravel())
    out = (img.astype('float') - min_val) / (max_val - min_val)   # 'float' for double; 'float32' for 32bits
    
    return out

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def rbf(x, y, sigma):
    
    return  exp( - np.dot(x, y) /(2*sigma**2) ) 


for i in range(img_num):
    img = imread(root + img_list[i])
    img = imresize(img, [resize_size, resize_size])
    
    if np.shape(img)[2] > 1:
        img = rgb2gray(img)
        
    img = im2double(img)
    
    imgs[i,:] = img.ravel()
    
    if i > 0:
        rbf_dist[i-1] = rbf( imgs[i-1,:], imgs[i,:], 1 )   # assign called value to rvf_dist[]
#        print( rbf( imgs[i-1,:], imgs[i,:], 1 )  )
    
    



