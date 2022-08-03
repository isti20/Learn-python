"""Operasi Aritmatika

1. Operasi penjumlahan +
2. Operasi pengurangan -
3. Operasi perkalian *
4. Operasi pembagian /
5. Operasi eksponen (pangkat) **
6. Operasi modulus (sisa pembagian) %
7. Operasi floor division // (dibulatkan kebawah)
"""

#Operasi tambah +
print("\n==Operasi pertambahan==")
a = 10
b = 3
hasil = a+b
print(a,'+',b,'=',hasil)

#Operasi pengurangan -
print("\n==Operasi pengurangan==")
c = 10
d = 3
hasil = c-d
print(c,'-',d,'=',hasil)

#Operasi perkalian *
print("\n==Operasi perkalian==")
e = 10
f = 3
hasil = e*f
print(e,'*',f,'=',hasil)

#Operasi pembagian /
print("\n==Operasi pembagian==")
g = 10
h = 3
hasil = g/h
print(g,'/',h,'=',hasil)

#Operasi eksponen (pangkat) **
print("\n==Operasi eksponen==")
i = 10
j = 3
hasil = i**3
print(i,'**',j,'=',hasil)

#Operasi modulus (sisa pembagian) %
print("\n==Operasi modulus==")
k = 10
l = 3
hasil = k%l
print(k,'%',l,'=',hasil)

#Operasi floor division // (dibulatkan kebawah)
print("\n==Operasi floor division==")
m = 10
n = 3
hasil = m//n
print(m,'//',n,'=',hasil)

#Prioritas operasi, operational precedence
"""Prioritas operasi urutan pengerjaannya adalah:
1. ()
2. Exponen **
3. Perkalian & teman-teman *,/,%,//
4. Pertambahan & pengurangan
"""
print("\n==Prioritas Operasi==")
x = 3
y = 2
z = 4
hasil = x+y*z
print(x,'+',y,'*',z,'=',hasil)

