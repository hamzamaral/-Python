# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:58:22 2022

@author: HAMZA
"""

#importing

import numpy as mhm

array = mhm.array([1,2,3,4,5,6])

a= array.reshape(3,2)

print("shape: ",array.shape)

print("dimension: ", a.ndim)

print("detatype: ", a.dtype.name)

print("type: ", print(a))

print("size: ", a.size)

array1 = mhm.array([[1,2,3,4],[5,6,7,8,],[9,10,11,12]])

zeros = mhm.zeros((3,4))

zeros[2,1]=5
print(zeros)

mhm.ones((3,2))

mhm.empty((3,5))
        
a = mhm.arange(10, 25,1.5)
print(a)

a = mhm.linspace(10,50,20)
print(a)

#%%

import numpy as np
array12 = np.array([1,2,3,4,5,6,7]) 

print(array[0])

print(array12[1:4])

reverse_array=array12[::-1]

print(reverse_array)

arm=mhm.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(arm)

print(arm[1,:2])

print(1,1)

print(arm[:,1])


print(arm[1,1:4])

print(arm[-1,:])

print( arm[:,-1])



