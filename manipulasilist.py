"""Manipulasi List"""

##Operasi list

# index 0(-3)   1(-2)   2(-1)
data = ['ucup','otong','dudung']

#Mengambil data dari list
print('\n==Mengambil data dari list==')
datanama = ['lala','lili','lulu']
data_0 = data[0]
print('data pertama (index 0) = {}'.format(data_0))

#Mengambil info jumlah data dalam list
print('\n==Mengambil info jumlah data dalam list==')
data_angka = [1,2,3,4,5,6,7,8,9]
panjang_data = len(data_angka)
print('Panjang data = {}'.format(panjang_data))

#Menambahkan item pada list sesuai posisi
print('\n==Menambahkan item pada list sesuai posisi==')
data_warna = ['kuning','hijau']
print(f"data sebelum ditambah = {data_warna}")
data_warna.insert(0,'merah') # ini (index ke-, data yang ditambah)
print(f"data sesudah ditambah warna merah = {data_warna}")

#Menambah data di akhir list
print('\n==Menambah data di akhir list==')
data_buah = ['mangga','apel','nanas']
print(f"data sebelum ditambah = {data_buah}")
data_buah.append('delima')
print(f"data sesudah ditambah delima = {data_buah}")

#Menambah list dengan list
print('\n==Menambah list dengan list==')
data_awal = [1,2,3]
data_tambahan = [4,5,6]
data_awal.extend(data_tambahan)
print('data gabungan = {}'.format(data_awal))

#Merubah data
print('\n==Merubah data==')
data_lama = ['mawar','melati','anggrek']
data_lama[2] = "tulip" #kita ubah data 2 menjadi tulip
print('data baru (setelah dirubah) = {}'.format(data_lama))

#Meremove data
print('\n==Meremove data==')
nama_kota = ['jakarta','bekasi','bandung']
nama_kota.remove('bekasi') #kita akan meremove data bekasi
print('data remove = {}'.format(nama_kota))

#Meremove data paling belakang
print('\n==Meremove data paling belakang==')
data = ['mamba','kue','bumi'] 
data = data.pop() #nama variabel listnya harus data
print('data akhir = {}'.format(data))
