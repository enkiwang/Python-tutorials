#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:35:09 2018

@author: yongweiw
"""

import numpy as np
import random 

#data = np.arange(33, 127) # linear values [33,126], where 33 for '!', 65 for 'A', 97 for 'a', 126 for '~'
data = list(range(1,11))

data_random = random.sample(list(data), len(data))
print(data_random)
print(type(data_random))


def search(number, table):
    for index, item in enumerate(table):
        if item == number:
            return index
        
index = search(3, data_random)
print(index)

"""
[6, 1, 3, 2, 8, 5, 10, 4, 9, 7]
<class 'list'>
2
"""