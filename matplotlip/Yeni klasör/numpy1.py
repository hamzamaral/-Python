# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:58:22 2022

@author: HAMZA
"""
import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
dizii=[1,1,2,5,6,8,9]   
print(array.shape)
a = array.reshape(3,5)
print("shape: ",a.shape)
print("dimension: ",a.ndim )

print("data type: ",a.dtype.name)
print("size: ",a.size)

print("type: ",type(a))
