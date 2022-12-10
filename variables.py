"""Mengenal variabel

Variabel adalah kontainer (wadah) untuk menyimpan nilai data
Contoh:
x = 2 

x adalah variabel
2 adalah value (nilai)
= adalah assignment

Penamaan varaibel:
- Harus dimulai dengan huruf atau karakter underscore _
- Tidak bisa menggunakan spasi (hanya boleh berisi karakter alfanumerik A-z dan
  garis bawah _)
- Tidak bisa diawali dengan angka
- Nama variabel peka terhadap huruf besar dan kecil.
  contoh: A dan a berbeda meski keduanya huruf yang sama
"""

# menaru / assignment nilai
a = 10
A = 5
panjang = 1000

# pemanggilan pertama
print("Nilai a = ", a)
print('Nilai A = ', A)
print("Nilai panjang = ", panjang)

# penamaan
nilai_y = 15 # dengan menggunakan underscore
juta10 = 10000000 # ini boleh
nilaiZ = 17.5 # ini boleh

# pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai a = ", a)

# assignment indirect
b = a #nilai a yang digunakan yang ke-2 (pemanggilan kedua)
print("Nilai b = ", b)

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x, y)