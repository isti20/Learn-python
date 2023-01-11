"""Tipe Collection: Tuples dan set"""

#List: menggunakan kurung siku
print("\n==Data List==")
data_list = [10,2,4,4,2]
print(data_list)

#Tuples: menggunakan kurung biasa
print("\n==Data Tuples==")
data_tuples = (7,8,9,10)
print(data_tuples[1]) #data tuples index ke-1

"""
- Tuples TIDAK BISA MERUBAH isi data
- Tuples tidak support assigment:
  tidak bisa dilakukan data_tuples[1] = "ucup"
- Tidak bisa mengganti member atau menambahkan member di
  belakang: data_tuples.append()
"""

#Sets (himpunan): menggunakan kurung kurawal
print("\n==Data Sets==")
data_sets = {10,4,3,2,4,7,6,5}
print(data_sets)

"""
Sets adalah collection yang tidak punya index (tidak ada 
urutannya / tidak ada indexnya)
"""
