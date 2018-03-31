#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:17:15 2018
1)softmax, for multiclass classification, P(y=j|x)=exp(x'*w_j)/sum(exp(x'*w_k)), k=1,..,K
  1)the largest value will be augmented while the rests suppressed, and the least ones significantly suppressed.
  2)scale variant due to the NONLINEARITY of exp(), denominators are the same for all entries
2)cross_entropy
@author: yongweiw
"""

import numpy as np
import math

"case 1) assuming one value is significantly greater than the rests"
z_1 = [1.0, 1.0, 1.0, 5.0, 1.0, 1.0]  # sum(z_1) =10 

# 1)calculate exp()
z1_exp = [math.exp(j) for j in z_1]
print([round(k,2) for k in z1_exp])  # [2.72, 2.72, 2.72, 148.41, 2.72, 2.72]

# 2)calculate sum of exp()
sum_z1_exp = sum(z1_exp)             
print([round(sum_z1_exp,2)])         # [162.0]

softmax = [round(j / sum_z1_exp, 3) for j in z1_exp]
print(softmax)                       # [0, 0, 0, 1, 0, 0], due to precision

"""
original: [1.0, 1.0, 1.0, 5.0, 1.0, 1.0] 
exp: [2.72, 2.72, 2.72, 148.41, 2.72, 2.72]
softmax output: [0, 0, 0, 1, 0, 0]
ONE value is significantly augmented compared with its rest counterparts

"""

"case 2) assuming some values are significantly greater than the rests"
z_2 = [2.0, 2.0, 2.0, 3., 1.]

z2_exp = [math.exp(j) for j in z_2]   
print([round(k,2) for k in z2_exp])   #[7.39, 7.39, 7.39, 20.09, 2.72] 

sum_z2_exp = sum(z2_exp)
print(round(sum_z2_exp))  # 45

softmax_ = [round(j / sum_z2_exp, 3) for j in z2_exp]
print(softmax_)        # [0.164, 0.164, 0.164, 0.447, 0.06]
"""
comparing entries in z_2 with softmax_:
3.0 -> 0.447, 2.0->0.164, and 1.0-> 0.006
3.0 highlighted, 2.0 suppressed, and 1.0 significantly suppressed.
"""