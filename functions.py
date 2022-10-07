# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 02:41:37 2022

@author: HAMZA
"""
#%%
var1=5
var2=25
def my_firsst_function(var1,var2):
    output=var1+var2*(var1*var2*var2)/(var1-var2)
   
mlk=my_firsst_function(var1, var2)


sonuç=my_firsst_function(var1, var2)

def deneme1():
    print("bu benim ikinci denemem")
    
    #%%
    
isim="hamza"
soyisim="maral"
ayakkabi_numarasi=35
    
def func_proj(isim,soyisim,ayakkabi_numarasi,*args,yaş=15):
    print("isim:",isim,"soyisim",soyisim,"yaş:",yaş,"ayakkabi_numarasi:",ayakkabi_numarasi,"boy:",args)
    print(type(soyisim))
    print(float(ayakkabi_numarasi))
    
    output = isim[0]*ayakkabi_numarasi
    return output
    
sonuc = func_proj(isim, soyisim, ayakkabi_numarasi)
print("args[0]*yas: ", sonuc)
 #%%
 #8 list
liste = [1,2,3,4,5,6]
type(liste)
liste[2]
liste_divide=liste[0:3]

 
liste_str=["hamza","halil","ensar"]
type(liste_str)

dir(liste)
help(list.remove)
lis=[2,6,5,4,8,3,1,9,7,10,12,11]
lis.sort()
dic.values()
dic.keys()
#%%

#touple

t=(1,2,3,5,8,4,6,7,9)
dir(t)
help(tuple.count)
t.count(3)#kaç adet olduğunu döndürür
t.index(4)


#dictonary

dic={"halil":24,"ensar":22,"hamza":25}
dir(dic)

dic["halil"]

def denemee():
    dic={"halil":24,"ensar":22,"hamza":25}
    return dic

rte=denemee()
#%%

var1=20
var2=25

if var1>var2:
    print("var1 buyuktür var2")
elif var2>var1:
    print("var1 küçüktür var2")
else:
    print("var1 eişttir var2")


listele=[1,6,3,5,2,4,7,8,9]
value=3
if value in listele:
    print("listenin içinde 3 değeri var")
else:
    print("hayır")

keys = dic.keys()

if "can" in keys:
    print("evet")
else:
    print("hayir")
    
    #%%
    
# 1640. yil == 17. yuzyil
# 109. yil == 2. yuzyil
# 2000. yil = 20. yuzyil
    
# metod yazin.
    # input integer yillar
    # output integer yuzyil

# input = year  >> 1 <= year <= 2005

    
#%%






