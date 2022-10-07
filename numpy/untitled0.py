# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 00:17:24 2022

@author: HAMZA
"""


import pandas as pd

df=pd.read_csv("iris (1).csv")

import matplotlib.pyplot as plt


setosa= df[df.Species=="Iris-setosa"]
virginica=df[df.Species=="Iris-virginica"]
versicolor=df[df.Species=="Iris-versicolor"]	

plt.hist(setosa.PetalLengthCm,bins=50)#tells how many of each product
plt.legend()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.title("hist")
plt.show()
#%% bar plot
import numpy as np

#x=np.array([1,2,3,4,5,6,7,8,9])
#y=x*3-2

#plt.bar(x,y)
#plt.xlabel("X")
#plt.ylabel("Y")
#plt.title("bar")
#plt.show()

x=np.array([1,2,3,4,5,6,7,8,9])
a=["turkey","use","a","inglish","germany","kero","dadad","ada","yaysıçim"]
y=x*3-2

plt.bar(a,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("bar")
plt.show()


#%%subplots

df1 = df.drop(["Id"],axis=1)

df1.plot(subplots=True)



plt.subplot(2,1,1)#2 tane plotum var 1,1=1 columun 1 satırı
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa_PetalLengthCm")
plt.ylabel("setosa")
plt.subplot(2,1,2)#2 tane plotum var 1,2=1 columun2 satırı
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label="virginica_PetalLengthCm")
plt.ylabel("virginica")
plt.show()