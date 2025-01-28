# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:14:40 2023

@author: ENES
"""

x=5 #101
y=2#010

a=4
print("sayi:{} tipi:{}".format(x,type(x)))
print(x**y)
print(x//y) #tek slah olursa float gösterir çift slash ile int yapıyoruz yuvarlama
x -= y
print(x) 
x%=y
print(x)
#comparasion operator(karşılaştırma operatörleri)
print(x==y)
print(x<y)
print(x!=y)
print(x>=y)
#string comparasion
isim1="enes"
isim2="Memet"
print(isim1<isim2)#ilk harten başlar asciye göre sıralar
print(isim1!=isim2)
print(isim1==isim2)
print(isim1>=isim2)
print(ord("m"))#ascii

isim2=isim2.lower()#kelimeyi küçük harf yapar
print(isim2)
print(isim1<isim2)
print(x<2 or 3>y)
print(x<1 and 3>y)
switch=True
switch = not switch
print(switch)
q=bool("herhangi bir sayı")
w=bool(0)
print(q,w)
print(x is  y)#x y dir  hem değer hem tipi 
print(x is not y)



