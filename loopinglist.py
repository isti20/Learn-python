"""Looping list dan enumerate"""
#Looping dari list (for loop)
print('\n==Looping dari list (for loop)==')
peserta = ['ucup','otong','dadang']
for nama in peserta:
    print("nama = {}".format(nama))

#Looping dari list (for loop dan range)
print('\n==Looping dari list (for loop dan range)==')
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print('angka = {}'.format(kumpulan_angka[i]))

#While loop
print('\n==While loop==')
nomor = [10,5,4,2,6,5]
panjang = len(nomor)
i = 0 #i dimulai dari index ke-0

while i < panjang:
    print('angka = {}'.format(nomor[i]))
    i += 1 #selanjutnya i akan ditambahkan 1 (dari index-1 sampai index-5)

#List comprehension
print('\n==Contoh List comprehension 01==')
data = ['ucup',1,2,3,'otong']
[print (i) for i in data]

print('\n==Contoh List comprehension 02==')
data2 = ['ucup',1,2,3,'otong']
[print (f"data = {i}") for i in data]

#Enumerate: mengambil index dan datanya
print('\n==Enumerate==')
data_list = ['ucup',1,2,3,'otong']
for nomor_index, datanya in enumerate(data_list):
    print(f"index = {nomor_index}, data = {datanya}")
    