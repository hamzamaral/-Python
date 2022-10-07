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
dataframe["NAME"]

ort= dataframe.MAAS.mean()


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
 
 dataframe["maaş_seviyesi"]=[if dataframe.MAAS>200 for each in len(dataframe.MAAS)]
 
 
 