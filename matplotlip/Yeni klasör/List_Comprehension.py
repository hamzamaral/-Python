# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:46:04 2022

@author: HAMZA
"""

import pandas as pnd

dictionary={"NAME":["ubeyd","halil","hamza","furkan","sezaii","mehmetşah"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]}


dataframe=pnd.DataFrame(dictionary)
dataframe["sorname"]=["maral1","maral2","maral3","maral4","maral5","maral6"]

dataframe["NAME"]

ort= dataframe.MAAS.mean()

#%%

import numpy as np


mean_np=np.mean(dataframe.MAAS)

old_year_ort=np.mean(dataframe.AGE)
#dataframe["maaş_seviyesi"] =["yüksek maaş","yüksek maaş","yüksek maaş","yüksek maaş","yüksek maaş","yüksek maaş"]
#i=0
#for i in range(5):
 #   if dataframe.loc[i,"MAAS"] > 200:
 #       print()
 #   else:
 #       dataframe.loc[i,"maaş_seviyesi"]=["düşük maaş"]
 
dataframe["maaş seviyesi"]=["yüksek" if each>ort  else "düşük" for each in dataframe.MAAS]
 
 
 #♥
#%%

dataframe.columns

dataframe.columns= [each.split()[0] + "_" + each.split()[1] if len(each.split())>1 else each for each in dataframe.columns]


data1=dataframe.head()
data2=dataframe.tail()

dataframe.drop(["maaş_seviyesi"],axis=1,inplace=True)
data1.drop(["maaş_seviyesi"],axis=1,inplace=True)
data2.drop(["maaş_seviyesi"],axis=1,inplace=True)

dataframe.drop(["NAME"],axis=1)

data3= pnd.concat([data1,data2],axis=0)
data4= pnd.concat([data1,data2],axis=1)

data2.drop([1],axis=0)



#%%

def multi(AGE):
    return AGE*2

dataframe["new_columns"] = [each*2 for each in dataframe.AGE]

dataframe["new_columns2"] = [multi(each) for each in dataframe.AGE]

dataframe["new_columns3"] = dataframe.AGE.apply(multi)

