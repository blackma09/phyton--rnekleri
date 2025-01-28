# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 01:40:47 2023

@author: ENES
"""

import sys #kütüphane
a=1
print(sys.getsizeof(a))
#a değerine 28 bayt atamış python c gibi statik değil dinamik bie dildir.


#%%

x=7
y=7.1
z="2"
print(int(y))
print("z"*2)
print(y/float(z))
z="2.3"
print(int(z))
print(float(x)) #string floata ,int floata, float int a çevrilebilir.

#%%
degis1=input("sayı gir:")
print(type(degis1))
print("giridisin sayi:",degis1)
degis1=int(degis1)
print("{}+4={}".format(degis1,degis1+4)),
print(r"ahmet\/mehmet\\\///selin\/melek")
print(7 / 2 * 2 + 4 / 4 + 3 ** 2)
kelime = "Bilgisayar"
print(kelime[:2]+kelime[-1])
print(type("python"))