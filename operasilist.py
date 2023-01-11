"""Operasi pada List"""

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print('data angka = {}'.format(data_angka))

#Count data
print('\n==Count data==')
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print('jumlah angka 4 = {}'.format(jumlah_data_4))
print('jumlah angka 3 = {}'.format(jumlah_data_3))

#Ambil posisi data (index)
print('\n==Ambil posisi data (index)==')
data = ['ucup','otong','dudung','ujang']
index_dudung = data.index('dudung')
print('index si dudung = {}'.format(index_dudung))

#Mengurutkan list
print('\n==Mengurutkan list==')
data_angka.sort()
print("data angka sort = {}".format(data_angka))

print('\n==mengurutkan data string==')
nama_buah = ['mangga','apel','jambu','kelengkeng']
nama_buah.sort()
print('data nama buah sort = {}'.format(nama_buah))
##Hasil urutannya sesuai abjad

#Balik listnya
print('\n==Balik list==')
data_angka.reverse()
print('data direverse = {}'.format(data_angka))

#hasil data angka dari belakang (dibalik)
