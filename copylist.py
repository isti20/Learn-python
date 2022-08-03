"""Copy list: teknik menduplikat list"""

#Teknik menduplikat list
print('\n==Menduplikat list==')
a = ['ucup','otong','dudung']
print('data a = {}'.format(a))

b = a
print('data b = {}'.format(b))

#Kita akan merubah member a
print('\n==Merubah member a==')
a[1] = 'michael' #data a (index ke-1) akan diubah jadi michael
print('data a = {}'.format(a))
print('data b = {}'.format(b))

##Hasilnya data a dan data b keduanya berubah

#Kita akan merubah sort pada b
print('\n==Merubah sort pada b==')
b.sort()
print('data a = {}'.format(a))
print('data b = {}'.format(b))

##Hasilnya data a juga ikut berubah (ter-sort) mengikuti data b

"""Mengapa ketika kita melakukan perubahan pada data a atau
pada data b, maka kedua data ikut berubah? jawabannya: karena
data b merupakan copy dari data a, dan karena id address dari
data a dan data b sama"""

#Address dari kedua list a dan b
print(f"id adress a = {hex(id(a))}")
print(f"id adress b = {hex(id(b))}")

##Hasilnya id address a dan b sama
"""List b mengambil address yang sama. Jadi jika salah satu
   komponen dirubah maka keduanya berubah.
   
   Agar list b tidak ikut berubah maka kita harus menduplikat
   datanya"""

#Menduplikat list dengan copy
print('\n==Menduplikat list dengan copy==')
c = a.copy() #membuat list c dengan a.copy()

print(f"id adress a = {hex(id(a))}")
print(f"id adress b = {hex(id(b))}")
print(f"id adress c = {hex(id(c))}")

"""Hasilnya: c memiliki data yang sama dengan a tapi 
   addressnya berbeda. Jadi kalo kita rubah data a maka
   data c nya tidak ikut berubah"""

#Bukti data a tidak berubah jika kita rubah data c
print('\n==Bukti==')
c[0] = 'lala'
print('data a = {}'.format(a))
print('data b = {}'.format(b))
print('data c = {}'.format(c))


 



