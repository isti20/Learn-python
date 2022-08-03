"""Casting tipe data adalah merubah tipe data dari
   satu tipe data ke tipe yang lain"""

"""Kita akan merubah tipe data integer ke tipe data float"""

print("==Casting tipe data==")
data_int = 9
print("data :", data_int, "bertipe :", type(data_int))

"""cara merubahnya adalah"""
data_float = float(data_int)
print("data float: ", data_float, "bertipe: ", type(data_float))

"""Keterangan:
output dari data fload adalah 9.0 artinya yang tadinya 9 itu data integer
berubah menjadi data float.

note:
1. Data integer jika diubah ke data boolean outputnya akan False
   jika nilai integernya adalah 0
2. data float jika diubah ke data integer maka akan dibulatkan ke
   bawah nilainya. Misal: angka 9.9 akan menjadi 9
3. Data string dapat diubah ke data integer atau float jika stringnya
   adalah angka (bukan huruf)
4. Data string yang isinya kosong jika diubah ke data boolean maka
   outputnya akan False, sebaliknya jika ada isinya maka akan True
"""