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

