"""Nested List (list bersarang): berguna untuk data berseri"""
print('\n==List biasa==')
data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print('list biasa = {}'.format(data_list_biasa))

print('\n==List bersarang==')
data_list_bersarang = [data_0,data_1]
print('list bersarang = {}'.format(data_list_bersarang))

##Hasilnya list di dalam list

print('\n==List bersarang + data biasa==')
data_list_bersarang2 = [data_0,data_1,6,'ucup']
print('list bersarang = {}'.format(data_list_bersarang2))

#Contoh penggunaan nested list
print('\n==Contoh penggunaan nested list==')
peserta_0 = ['ucup',25,'laki-laki']
peserta_1 = ['otong',10,'laki=laki']
peserta_2 = ['dedeh',50,'wanita']

list_peserta = [peserta_0,peserta_1,peserta_2]
print('peserta = {}'.format(list_peserta))

print('\n')
for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}") #peserta(index 0)
    print(f"umur\t : {peserta[1]}") #peserta(index 1)
    print(f"gender\t : {peserta[2]}\n") #peserta(index 2)

#Permasalahan dengan reference
print('\n==Permasalahan dengan reference==')
list_copy = list_peserta.copy()
print("peserta = {}".format(list_copy))

print("\n==Kita ubah data peserta_0 (index 0)")
peserta_0[0] = "michael"
print("peserta list_copy = {}".format(list_copy))
print("\npeserta list_peserta = {}".format(list_peserta))

# Permasalahannya: hasilnya data list_copy berubah juga sama seperti list peserta

