# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:37:59 2018
img format conversion:
    numpy to pillow ((0,1)->(0,255) + transpose)
    pillow to numpy
    numpy to torch(.from_numpy or .Tensor, adding dimension(optional))
    torch to numpy()
Ref.: https://github.com/DmitryUlyanov/deep-image-prior/blob/master/utils/common_utils.py
@author: modified from Ref.
"""

import numpy as np
import torch
from PIL import Image
import matplotlib.pyplot as plt

def pil_to_np(img_PIL):
    """Format conversion: PIL -> np.array.
    Input: W x H x C [0,255]
    Output: C x W x H [0,1]
    """
    ar = np.array(img_PIL)
    
    if len(ar.shape) == 3:
        ar = ar.transpose(2,0,1)
    else:
        ar = ar[None,...]  #add C=1 dim for grayscale images (1, 256, 256)
    return ar.astype(np.float32)/255.

def np_to_pil(img_np):
    """Format conversion: np.array -> PIL.
    Input: C x W x H [0,1]
    Output: W x H x C [0,255]
    """
    ar = np.clip(img_np*255,0,255).astype(np.uint8)
    
    if img_np.shape[0] == 1: #(1, 256, 256)
        ar = ar[0] #(256, 256))
    else:
        ar = ar.transpose(1,2,0)
    return Image.fromarray(ar)
    
def torch_to_np(img_var):
    """Convers an image from torch.Tensor to np.array.
    Input: 1 x C x H x W [0,1] torch.tensor
    Output: C x H x W [0,1]    
    """
    return img_var.detach().cpu().numpy()[0]
    
def np_to_torch(img_np):
    """Convers an image from numpy to torch.Tensor.
    Input: C x H x W [0,1] torch.tensor
    Output: 1 x C x H x W [0,1]    
    """
    return torch.from_numpy(img_np)[None,:] #or you can use,[None,:],then  torch.Tensor()   