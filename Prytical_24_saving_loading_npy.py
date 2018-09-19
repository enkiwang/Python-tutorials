# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:18:42 2018
utility of .npy over .CSV/.txt files over:
    1)storing large data (since .csv/.txt requires bigger space, eg 13.8MB vs 7.62MB);
    2)repeated reading (since .csv/.txt are slower, eg 3.119 sec vs 0.010 sec)
https://towardsdatascience.com/why-you-should-start-using-npy-file-more-often-df2a13cc0161
@author: Yongwei
"""

import numpy as np
import time

num_samples = 1000000

data = np.random.randn(num_samples)

## saving as .txt
time1 = time.time()
with open('fdata.txt','w') as fdata:
    for k in range(len(data)):
        fdata.write(str(10*data[k]) + ',')  ##13.8MB
#loading
with open('fdata.txt','r') as fdata: #create fdata.txt beforehand
    datastr = fdata.read()
lst = datastr.split(',')
lst.pop()
print('\n time elapsed: %.3f' % (time.time() - time1)) ## 3.119 sec
data_lst = np.array(lst,dtype=float).reshape(1000,1000) #you can choose to reshape it


## saving with np.save (np.load)
time2 = time.time()
np.save('data_saved.npy',data)  #7.62MB

data_loaded = np.load('data_saved.npy')
print('\n time elapsed: %.3f' % (time.time() - time2)) ##  0.010 sec
print('\n Shape: %d' % data_loaded.shape)