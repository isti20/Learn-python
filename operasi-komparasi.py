"""Operasi komparasi (perbandingan): setiap hasil dari
   operasi komparasi adalah boolean (True/False)

   Operasi komparasi:
   1. Lebih besar dari >
   2. Kurang dari <
   3. Lebih dari sama dengan >=
   4. Kurang dari sama dengan <=
   5. Sama dengan ==
   6. Tidak sama dengan !=

   Operasi komparasi di atas dapat bekerja pada syntax literal.
   Misalnya:
   a == 4 artinya a ada nilainya (memakan memory) dan 4 itu literal.
   
   sedangkan untuk membandingkan memory / objek menggunakan operasi is.
   """

#Lebih besar dari >
print("\n==Lebih besar dari >==")
a = 4
b = 2
hasil = a > b
print(a,'>',b,'=',hasil)

#Kurang dari <
print("\n==Kurang dari >==")
c = 4
d = 2
hasil = c < d
print(c,'<',d,'=',hasil)

#Lebih dari sama dengan >=
print("\n==Lebih dari sama dengan >= ==")
e = 4
f = 2
hasil = e >= f
print(e,'>=',f,'=',hasil)

#Kurang dari sama dengan <=
print("\n==Kurang dari sama dengan <= ==")
g = 4
h = 2
hasil = g <= h
print(g,'<=',h,'=',hasil)

#Tidak sama dengan !=
print("\n==Tidak sama dengan != ==")
i = 4
j = 2
hasil = i != j
print(i,'<=',j,'=',hasil)

# is sebagai komparasi objek
print("\n==Lihat ID x dan Y sama==")
x = 5 #ini adalah assignment membuat objek identity
y = 5
print('nilai x =',x,'id =',hex(id(x)))
print('nilai y =',y,'id =',hex(id(y)))

hasil = x is y
print("x is y : ",hasil)

"""Hasilnya: id x dan y sama karena nilai x dan y sama
   yaitu 5 (disimpan di memory yang sama). Hasilnya akan
   True
"""
print("\n==Lihat ID o dan p beda==")
o = 5
p = 6
print('nilai o =',o,'id =',hex(id(o)))
print('nilai p =',p,'id =',hex(id(p)))

hasil = o is p
print(o,'is',p,'=',hasil)

"""Hasilnya: id o dan p beda karena nilai o dan p beda
   yaitu o = 5 dan p = 6 (disimpan di memory yang sama). Hasilnya 
   akan False
"""

#contoh syntax eror
"""
hasil = x is 5 
print('x is 5 = ', hasil)

ini akan eror karena 5 literal (bukan objek/variabel)"""

# is not sebagai komparasi objek
"""Kalo is not kebalikan dari is. Maksudnya kalo id dari objek
   objek yang dibandingkan berbeda makan hasilnya akan True"""