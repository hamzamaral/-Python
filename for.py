# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:28:47 2022

@author: HAMZA
"""

# 1640. yil == 17. yuzyil
# 109. yil == 2. yuzyil
# 2000. yil = 20. yuzyil
    
# metod yazin.
    # input integer yillar
    # output integer yuzyil

# input = year  >> 1 <= year <= 2005

def if_yapısı(year):
    year_str=str(year)
    
    if (len(year_str)==3):
        if (year_str[1:3]=="00"):
            return  int(year_str[0])
        else:
            return int(year_str[0])+1
    elif (len(year_str)<3):
        return 1
     
    else:
        if (year_str[2:4]=="00"):
            return  int(year_str[:2])
        else:
            return int(year_str[:2])+1
#%%

for i in range(1,20):
    print(i)

for i in  "afferim ahmet" :
    print(i)
    
for i in "afferim f  f  ahmet".split("f"):
    print(i)
    
liste=[1,2,3,4,5,6,7,8,9,10]

count=0

for i in liste:
    count=count+i
    print(count)
    
summmation=sum(liste)

#%%
liste=[1,2,3,4,5,6,7,8,9,10]
i=0
count=0
listeem=len(liste)
while(i<listeem):
    count=count+liste[i]
    i=i+1
    print(count)
#%%













