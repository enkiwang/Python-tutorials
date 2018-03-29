#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:08:48 2018

@author: yongweiw
"""

"default params are only created for once, not for multiple times"
# case 1) default initialization with [], different lists point to a same id
def append_list(num, res=[]):
    print("res addr:", id(res))
    res.append(num)
    return res

list_1 = append_list(1)
print(list_1)  # [1]
list_2 = append_list(2)
print(list_2)  # [1, 2]
list_3 = append_list(3)
print(list_3)  # [1, 2, 3]

# display three lists after append operation
print("Three lists:", list_1, list_2, list_3)

""" 
res addr: 140619199188872
res addr: 140619199188872
res addr: 140619199188872
Three lists: [1, 2, 3] [1, 2, 3] [1, 2, 3]
"""

# case 2) default initialization with None, and force to create new id if 2nd param set to be default 
def append_list(num, res=None):
    if res is None:
        res=[]
    print("res addr:",id(res))
    res.append(num)
    return res

list_4 = append_list(4)
print(list_4)

list_5 = append_list(5)
print(list_5)

list_6 = append_list(6)
print(list_6)

# display three lists after append operation
print("Three lists:", list_3, list_4, list_5)
"""
res addr: 140619199188040
res addr: 140619188020360
res addr: 140619187974216
Three lists: [3] [4] [5]

"""
