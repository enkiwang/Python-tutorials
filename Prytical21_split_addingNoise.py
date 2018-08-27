# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 09:25:10 2018
split:split string separately
AWGN to images, np.random.normal()
plt.imread, 
    (plt.imread creates a np array of float type with values from 0 to 1; while
    scipy.misc.imread creates array with unit8 type, i.e., 0 - 255)
@author: yongweiw
"""

import numpy as np
from math import log10
import matplotlib.pyplot as plt

x = "Good,better,best"
print(x.split(",")) #split string according to separator comma
#['Good', 'better', 'best']

word1,word2,word3 = x.split(",")

def adding_noise(img,sigma=1):
    """
    adding white Gaussian noise to an image.
    
    Args:
    img:image, np.aray \in (0,1)
    sigma: std of the Gaussian noise
    """
    
    img_noisy = np.clip(img + np.random.normal(scale=sigma,size=img.shape),0,1).astype(np.float32)
    
    return img_noisy
    

# read image
if __name__ == "__main__":
    img = plt.imread('lena.png') #float32, within (0,1)
    Sigma = 0.01 #std 
    img_noisy = adding_noise(img, sigma=Sigma)
    
    plt.figure(1)
    plt.imshow(img,cmap='gray')
    plt.show()
    
    plt.figure(2)
    plt.imshow(img_noisy,cmap='gray')
    plt.show()
    
    ##calculate PSNR
    diff = (img - img_noisy) ** 2
    mse = np.mean(diff.ravel())
    print("PSNR= %.3f dB" % (-10*log10(mse))) 
    # Sigma = 0.5, PSNR=9.047 dB,blurred a lot
    # Sigma = 0.1, PSRN=20.047 dB, noticable artefact
    # Sigma = 0.05, PSRN=25.983 dB,visually good, still with artefact
    # Sigma = 0.03, PSRN=30.445 dB,visually good, still with little artefact
    # Sigma = 0.01, PSRN=39.969 dB,visually very good, hardly with noticeable artefacts
    