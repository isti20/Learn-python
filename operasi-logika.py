"""Operasi logika atau boolean: not, or, and, xor (^)
"""

#Operasi logika NOT
print("\n==NOT==")
a = True
b = not a
print('data a =',a)
print('data b (not a) =',b)

#Operasi logika OR (Jika salah satu True maka hasilnya True)
print("\n==OR==")
c = False
d = False
hasil = c or d
print(c,'or',d,'=',hasil)

#Operasi logika AND (Jika dua buah nilai True maka hasilnya True)
print("\n==AND==")
e = False
f = False
hasil = e and f
print(e,'and',f,'=',hasil)

#Operasi logika XOR (akan True jika salah satu True, sisanya False)
print("\n==XOR ^==")
g = True
h = True
hasil = g^h
print(g,'^',h,'=',hasil)