# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:40:06 2018
Laplacian operator: second order differential for image enhancement
    mask: 3 * 3 kernelized filter (mask)
    img: original image
    img_new: convolved image by a sliding mask with stride 1
@author: Yongwei
"""

from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np

root = 'C:/Users/Yongwei/Downloads/'
img = imread(root + 'lena256.png')  #uint8
m, n = np.shape(img)  # size of img in x, y axis

mask = np.array([ [0, 1, 0],[1, -4, 1],[0, 1, 0]]) 
img_new = np.zeros([m-2, n-2]) # 2= kernel_size - 1

for y in range(n-2):
    for x in range(m-2):
        img_new[x, y] = np.dot(mask.ravel(), img[x:x+3, y:y+3].ravel() ) #[i,j] to index a np.array 
        
                
# plot convolved image
plt.imshow(img_new)
plt.show()        

