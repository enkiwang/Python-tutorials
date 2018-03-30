#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 22:03:07 2018

@author: yongwei
"""

import random
import numbers 

# generate random integers
def RandGen(num, val_min, val_max):
    # return num integers \in [val_min, val_max]
    if not isinstance(num, numbers.Integral) and isinstance(val_min, numbers.Integral) and (val_max, numbers.Integral) :
        raise ValueError("val, val_min, val_max should be integers!")
    
    random.seed(123)
    for i in range(num):
        yield random.randint(val_min, val_max)
        
for random_int in RandGen(6,0, 100):
    print("The next random integer is.. %d" % (random_int))

    
"""
Case 1) RandGen(6, 0, 100.1)
    ValueError: non-integer stop for randrange()
    
Case 2) RandGen(6, 0, 100)
The next random integer is.. 6
The next random integer is.. 34
The next random integer is.. 11
The next random integer is.. 98
The next random integer is.. 52
The next random integer is.. 34

"""
