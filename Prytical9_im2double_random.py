#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:40:38 2018

@author: yongweiw
"""
import numpy as np

def im2double(img):
    min_val = np.min(img.ravel())
    max_val = np.max(img.ravel())
    out = (img.astype('float' - min_val)) / (max_val - min_val)   # 'float' for double; 'float32' for 32bits
    
    return out


# generate random integers using random.sample()
data = random.sample(range(1, 11), 10)  # [1, 2,.., 10]
print(data)

# generate random integers using shuffle function
data2 = list(range(1,11))
random.shuffle(data2)  # shuffle option, if data3= random.shuffle(data2), print(data3) returns None.
print(data2)

"""
[1, 5, 2, 7, 4, 3, 10, 6, 8, 9]
[9, 8, 6, 10, 3, 4, 7, 2, 5, 1]
"""
