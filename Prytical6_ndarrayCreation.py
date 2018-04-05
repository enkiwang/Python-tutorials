#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:04:36 2018
create/initialize a ndarray in Python
1.use numpy only: 1)np.array(object,dtype=), 2)np.zeros(shape=,dtype=),3)np.ones(shape=,dtype=))
2.for pseudo-randoms, use:
         1)np.random.rand(d0, d1,...,dn), 
         2)np.random.randint(low,high=None,size=None,dtype='l')
         3)np.random.normal(loc=0.0, scale=1.0, size=None) #i.e., mu, std, shape
@author: yongweiw
"""
import numpy as np

"********************* use numpy module*********************"
# 1) np.array(ojb,dtype=),with a fixed number as input, not suitable for large-scale array initialization
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1,2],[3,4]])

print(arr1)  # [1 2 3]
print(arr2)  
"""
[1 2 3]
[[1 2]
 [3 4]]
"""
# 2) np.zeros(shape=,dtype=),initialize an array with any arbitrary shape, initialized to be all 0, suitable for large-scale array initialization
arr3 = np.zeros([2, 3])  #np.zeros((2,3)) also fine, as short expression of np.zeros(shape=(2,3)), but np.zeros(2,3) wrong!
arr4 = np.zeros(shape=(2,3), dtype=int)

print(arr3)
print(arr4)
"""
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
[[0 0 0]
 [0 0 0]]
"""
# 3) np.ones(shape=,dtype=),initialize an array with any arbitrary shape, initialized to be all 1, suitable for large-scale array initialization
arr5 = np.ones([2,3])
arr6 = np.ones(shape=(2,3), dtype=int)

print(arr5)
print(arr6)
"""
[[ 1.  1.  1.]
 [ 1.  1.  1.]]
[[1 1 1]
 [1 1 1]]
"""
"********************* use numpy.random module *********************"
rand1 = np.random.randint(2, size=20) #binary, 20 numbers, must use size=.., otherwise will generate one number only
rand2 = np.random.normal(loc=0.2, scale=2.0,size=(3,4,5))

print(rand1)
print(rand2) 
"""
[1 1 1 ..., 0 1 1]
[[[-2.18139339  1.03266557 -2.13231658 -0.87117738 -0.329259  ]
  [ 3.17892867 -1.77234731 -2.56718979 -1.27573066 -0.92347016]
  [-0.91423917 -0.21850651  2.83110874 -1.07815183 -0.98761529]
  [ 2.19822762  2.8871197   0.13354512  0.18414277  0.44924286]]

 [[ 0.70488899 -0.31498858 -4.44626449  0.83198997  2.89380363]
  [-2.3990291  -0.67555862  0.90269075 -0.86472435 -4.70236729]
  [-0.08717335  0.95843028  2.23867012  0.27107992  3.3829666 ]
  [ 2.69396827  2.31781281  1.2512552  -1.25588645  1.35785482]]

 [[-1.83898919  2.07268099  3.63068195  0.38130345  0.95622063]
  [ 0.91464798 -2.27042585 -0.96759825  0.65335757  2.55548467]
  [-0.93384921  0.0511637  -3.08281534 -3.47081619  0.65899343]
  [ 1.46518594 -2.41694845  0.16820777 -0.92066741 -0.13129567]]]
"""