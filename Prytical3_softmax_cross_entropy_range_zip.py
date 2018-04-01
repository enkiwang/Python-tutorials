#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:01:34 2018
1)SOFTMAX: for multiclass classification, P(y=j|x)=exp(x'*w_j)/sum(exp(x'*w_k)), k=1,..,K
  1)the largest value will be augmented while the rests suppressed, and the least ones significantly suppressed.
  2)scale variant due to the NONLINEARITY of exp(), denominators are the same for all entries.
2)CROSS_ENTROPY: to measure the difference between two pdfs. (one of the many possible loss functions)
  In classification, cross_entropy function is commonly used as loss function, formulated as:
         H(prob_est, prob_one_hot) = -sum_k {prob_one_hot(k)* log(prob_est(k))}, k=1,..,K.
@author: yongweiw
"""

import numpy as np
import math

" 1)******************************** python for SOFTMAX function ********************************"
z = [2.0, 2.0, 2., 3., 1.]
#z = [1.0, 1.0, 1., 6., 1.]

z_exp = [math.exp(j) for j in z]   
print([round(k,2) for k in z_exp])   #[7.39, 7.39, 7.39, 20.09, 2.72] 

sum_z_exp = sum(z_exp)
print(round(sum_z_exp))  # 45

softmax = [round(j / sum_z_exp, 3) for j in z_exp]
print(softmax)        # [0.164, 0.164, 0.164, 0.447, 0.06]
"""
comparing entries in z_2 with softmax_:
3.0 -> 0.447, 2.0->0.164, and 1.0-> 0.006
3.0 highlighted, 2.0 suppressed, and 1.0 significantly suppressed.
"""

" 2)******************************** python for CROSS_ENTROPY function ********************************"
    
one_hot_vec = [0., 0., 0., 1., 0.]

# calculate cross_entropy function between softmax pdf and one_hot_vec pdf
# 1)calculate cross_entropy in one line
H = -sum([prob_one_hot * math.log(prob_est) for prob_one_hot, prob_est in zip(one_hot_vec, softmax) ])
print("cross_entroy of softmax and one-hot is:", round(H,3))   # 0.805

#z = [1.0, 1.0, 1., 6., 1.], H=0.026

# 2)calculate cross_entropy with a for loop
H_ = 0
for i in range(len(one_hot_vec)):    # range(len(data)) returns a list [0,1,..,len(data)-1]
    H_ -= one_hot_vec[i] * math.log(softmax[i])   # index a list with a square bracket []
print("cross_entroy of softmax and one-hot is:", round(H_,3)) # 0.805   