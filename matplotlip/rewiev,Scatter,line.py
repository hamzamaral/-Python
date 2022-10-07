# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 06:53:44 2022

@author: HAMZA
"""

import pandas as pd

df=pd.read_csv("iris (1).csv")

print(df.columns)

print(df.info())

print(df.describe())

print(df.Species.unique())

print(df.SepalLengthCm.unique())

setosa= df[df.Species=="Iris-setosa"]
print(setosa.info())

virginica=df[df.Species=="Iris-virginica"]

print(setosa.describe())
print(virginica.describe())


#%%

import matplotlib.pyplot as plt


df1 = df.drop(["Id"],axis=1)

#df1.plot()

#plt.show()


setosa= df[df.Species=="Iris-setosa"]
virginica=df[df.Species=="Iris-virginica"]
versicolor=df[df.Species=="Iris-versicolor"]	



plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa_PetalLengthCm")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label="virginica_PetalLengthCm")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor_PetalLengthCm")
#plt.plot(setosa.Id,setosa.SepalLengthCm,color="blue",label="setosa_SepalLengthCm")
#plt.plot(setosa.Id,setosa.SepalWidthCm,color="green",label="setosa_SepalWidthCm")
#plt.plot(setosa.Id,setosa.PetalWidthCm,color="black",label="setosa_PetalWidthCm")
plt.legend()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()


df1.plot(grid=True, linestyle=":")
df1.plot(grid=True, alpha=0.3 )

plt.show()
#%%
df.columns

plt.scatter(setosa.Id, setosa.PetalLengthCm,color="red",label="setosa_PetalLengthCm")
plt.scatter(virginica.Id,virginica.PetalLengthCm,color="blue",label="virginica_PetalLengthCm")
plt.scatter(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor_PetalLengthCm")
plt.legend()
plt.title("scatter_plot")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()




