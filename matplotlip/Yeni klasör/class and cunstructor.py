# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 01:12:20 2022

@author: HAMZA
"""
class çalışan:
    def çalışan_12 (self,isim,soyisim,maaş):
       self.isim=isim
       self.soyisim=soyisim
       self.maaş=maaş
      # self.email=isim+soyisim+"@"+"gmail.com"
      
    
    
    def giveNameSorname(self):
       return self.isim + " " + self.soyisim


işci1=çalışan("halil","ibb",2800)
print(işci1.isim)
print(işci1.giveNameSorname())