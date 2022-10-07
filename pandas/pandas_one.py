# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:07:29 2022

@author: HAMZA maral
"""
# 1) pandas hizli ve etkili for dataframes
# 2) csv ve text dosyalarına acip inceleyip sonuclarimiza bu dosya tiplerine rahat bir sekilde kaydedbilir.
# 3) pandas bizim isimizi kolaylastiriyor for missing data
# 4) reshape yapip datayi daha etkili bir sekilde kullanabiliriz
# 5) slicing indexing kolay
# 6) time series data analizinde cok yardimci
# 7) ayrica herseyden onemlisi hiz pandas hiz acisindan optimize edilmis hizli bir kutuphane



import pandas as pd

dictionary={"NAME":["ubeyd","halil","hamza","furkan","sezaii","mehmetşah"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]}
inspect=pd.DataFrame(dictionary)

head=inspect.head()

tail=inspect.tail()

#%%

print(inspect.columns)
print(inspect.info())
print(inspect.describe())
print(inspect.dtypes)




