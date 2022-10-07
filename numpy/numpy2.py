# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:38:38 2022

@author: HAMZA
"""

#  numpy basic operations

import numpy as mrl

c= mrl.array([1,2,3,4])

d=mrl.array([4,5,6,7])

print(c+d)

print(c-d)

print(d-c)

print(c*d)

print(c**2)

print(mrl.sin(c))

print(c<2)


a = mrl.array([[1,2,3],[4,5,6]])
b = mrl.array([[7,8,9],[10,11,12]])

# element wise prodcut
print(a*b)

b.T
# matrix prodcut
a.dot(b.T)

print(mrl.exp(a))


a= mrl.random.random(5,5)

print(a.sum())

print(a.max())

print(a.min())

print(a.sum(axis=0))

print(a.sum(axis=1))

print(mrl.sqrt(a))
print(mrl.square(a)) # a**2


print(mrl.add(a,a))

#%%




