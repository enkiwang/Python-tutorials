#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 18:59:19 2018
Two way of listing keys in a dict:
    1).keys(), and print it
    2)find key and print it.
@author: yongweiw
"""

dict_std = {'Name': 'Anna', 'Age': 6, 'Class': 'First'}  # _std for student

# method 1
print (list(dict_std.keys()))


# method 2
for key in dict_std.keys():
    print (key)