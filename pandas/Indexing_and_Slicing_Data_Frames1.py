# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:07:28 2022

@author: HAMZA
"""

import pandas as pnd

dictionary={"NAME":["ubeyd","halil","hamza","furkan","sezaii","mehmetşah"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]}

dataframe = pnd.DataFrame(dictionary)

print(dataframe["AGE"])

print(dataframe.AGE)

dataframe["sorname"]=["maral1","maral2","maral3","maral4","maral5","maral6"]

print(dataframe.loc[:,:])

print(dataframe.loc[1:3,"NAME":"MAAS"])

print(dataframe.loc[::-1,:])

print(dataframe.iloc[1:3,2:3])

print(dataframe.loc[:,"NAME":"MAAS"])

#%% filtering

dataframe1=dataframe.MAAS<200

print(dataframe1)


filitre_data1=dataframe[dataframe1]


dataframe2=dataframe.AGE >22

filitre_data2=dataframe[dataframe2]

filitre_data3=dataframe[dataframe1 & dataframe2]

print(dataframe[dataframe.AGE>60])
