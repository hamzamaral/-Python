# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 00:23:16 2022

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








csdvdföbvlqdjhvb qşkdnv
1.5. Grafiğe ızgara ekleme (grid) komutları
grid:Grafiğin arkasına grid(ızgara) çizer.

alpha:Grid çizgilerinin saydamlığını ayarlar.0-1 arasında değer alır. 1'e yaklaştıkça saydamlık artar.0'a yaklaştıkça azalır.

linestyle: Grid çizgilerinin biçimini belirler.'-', '--', '-.', ':', '', gibi değerler alabilir.

linewidth: Grid çubuklarının kalınlığını belirler. İnteger değerler alır.

color: Grid çizgilerinin rengini belirler.

Farklı Stiller (Veri kümesine göre kullanılabilir.)

dash_capstyle:'butt', 'round', 'projecting'

dash_joinstyle:'miter', 'round', 'bevel'

drawstyle: 'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'

fillstyle: 'full', 'left', 'right', 'bottom', 'top', 'none'






