# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:15:14 2018
generate linear spaced numbers:
    1)np.linspace(start, stop, num), e.g., np.linspace(0, 1, 100) will sample 100 data points from [0,1] with even space 1/100.
    2)np.arange(start, stop, step, dtype=None), defalut step is 1. NOTE: value range: [start, end) where end <= stop 
@author: Yongwei
"""

import numpy as np

"********************* linspace *********************"
# return evenly spaced numbers over specified interval np.linspace(start, stop, num=50)
linear_data1 = np.linspace(0, 1, num=11)
print(linear_data1)  # [ 0.   0.1  0.2 ...,  0.8  0.9  1. ]


"********************* arange *********************"
# returns enenly spaced values within a given interval [start, stop)

# 1)np.arange(stop_integer), default values: start=0, step=1, end <= stop
linear_arange1 = np.arange(5)
print(linear_arange1)  #[0 1 2 3 4]

# 2)np.arange(stop_float)
linear_arange2 = np.arange(5.0) #[ 0.  1.  2.  3.  4.]
print(linear_arange2)

# 3)np.arange(start_int, stop_int), default step will be set 1
linear_arange3 = np.arange(3, 8)  #[3 4 5 6 7]
print(linear_arange3)

# 4)np.arange(start_int, stop_int, step), set step value
linear_arange4 = np.arange(3, 8 , 2) #[3 5 7]
print(linear_arange4)