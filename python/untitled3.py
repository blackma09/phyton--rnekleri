# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:28:16 2024

@author: ENES
"""

x=5 #101
y=2#010
a=x & y#ve and
b= x | y#veya or
c=~a#not
d=x^y#xor
e=4
e >>= x#bitwise right shift
e <<= x#bitwise left shift
print( a, b ,c,d,e)
kelime="osuruk bombası"
print("os" in kelime)
print("osurma" not in kelime)
qaqa= None#tipi olmayan değişken
x=float(8.8)
print(x) 
x=int(5)
print(x)
y=bool(0)
print(y)
y=int(True)
print(y)
e=(2+5j)*(8+4j)/(3+1j)#kompoleks sAYI
e=complex(3,4)
liste1=[5,6,4,2]
tuple1=tuple[8,8,4,7,6]#içindeki değerler değiştirilemez
liste1[0]=4
#tuple1[0]=4
tuple2=tuple("ahmet")
kelime=kelime[:7]+"bok"#osuruk bok oldu
aralık=range(10)
print(aralık,type(aralık))
print(*aralık)
print(list(aralık))
print(tuple(aralık))
print(set(aralık))
aralik=range(18,2,-5)
aralik=range(5,14)
print(list(aralik))
tup1=(45,58,4,58,1)
qwe=([67,5])#listi tuple yaptık
print(tup1[::2])
print(tup1[0:len(tup1):2])
print(tup1.count(58))#elemandan kaç tane var
print(tup1.index(58))#elaman kaçıncı sırada
print(bin(10))#binary
print(hex(368))
print(0b110101)
print(sum(tup1))
print(len(tup1))
print(min(tup1))
print(max(tup1))
print(liste1[1:3])
print(liste1[-1])
print(liste1[len(liste1)-1])
isimler=["A","B","C","D"]
isimler=isimler +["E"]
isimler[0]="a"
del isimler[0]
print(isimler)


#%%


isimler=["A","B","C","D"]
yaslar=[5,4,3,2,1]
karısık=isimler+yaslar
karısık.extend({"rty",True,47.4,4j+8})
karısık.index(True)

karısık.insert(2,753)#2. elemana yaz
karısık.append(175)#son satıra ekle
karısık.pop(14)#14. indeki sil
karısık.extend([100,100,100])#bu elemanları ekle
karısık.remove(100)#ilk karşılaştığın bu değri sil
karısık.reverse()#listeyi terse çevirir
yaslar.sort()#küçükten büyüğe sıralar
#%%
bilgiler=[["A",5],["B",4],["C",3]]
print(bilgiler[0][0])
print(bilgiler[1][1])
bilgiler=[({753:"A"},{951:"B"},{852:"C"})]#tuple oldu
print(bilgiler[0][0][753])
print(bilgiler[0][1][951])
print(bilgiler[0][2][852])          
#%%
#set mutable,içindeki değerlerde sıra yok
set1={5 ,5 ,5,1,4,8,6,1,4}
set2={4,5,8,9}
değer="a","b","c"
print(set1) #tekrarları almaz
set1.add(678)
set1.clear()
set1.update({7,5,2,3,5  })
set1.pop()
print(set1)
set1.remove(7)
set1.discard(5)#5 i çıkar
print(set1)

set1.update({7,5,2,3,5 ,8 })
set1=set1.intersection(set2) #kesişimi alır
print(set1)

print(set1.isdisjoint(set2)) #set1 ile set2 kesişimş boş küme mi
print(set1.issubset(set2))#set1 set2 ni alt kümesi mi
print(set1.issuperset(set2))#set 1 set 2 yi kapsar mı
print(set1.union(set2))#set 1 ile sert yi birleştir
print(set1.symmetric_difference(set2))
sozluk={1:"A",2:"b",5:"c"}
print(sozluk[5])
print(sozluk.get(2))
sozlukelemanları=zip(set1,değer) #dictinory haline gertiriri
sozluk1=dict(sozlukelemanları)















