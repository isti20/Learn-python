"""Deep copy nested list"""

data_0 = [1,2]
data_1 = [3,4]
data_2D = [data_0,data_1]
print("data = {}".format(data_2D))

#Mengambil data dari nested list
print('\n==Mengambil data dari nested list==')
print('\n==Mengambil data list dari nested list==')
data = data_2D[0] #mengambil data list (index 0)
print('data list = {}'.format(data))

print('\n==Mengambil data member dari list di nested list==')
data = data_2D[0][0]
print('data member darai list = {}'.format(data)) 
#[0] yang pertama masuk ke list (index ke-0)
#[0] yang ambil data didalam list yang kita masuki (index ke-0)

#Address semuanya
print('\n==ID Address==')
data_2D_copy = data_2D.copy()
print('data copy = {}'.format(data_2D_copy))

print('\n==Id Address data asli dan data copy==')
print(f"id address data_2D = {hex(id(data_2D))}")
print(f"id address data_2D_copy = {hex(id(data_2D_copy))}")

##Hasilnya: id address dari data_2D dan data_2D_copy berbeda

print('\n==Id Address dari member ke-1==')
print(f"id address data_2D (index 0)= {hex(id(data_2D[0]))}")
print(f"id address data_2D_copy (index 0)= {hex(id(data_2D_copy[0]))}")

"""id adress member ke-1 (index ke-0) dari data_2D dan dari
   data_2D_copy sama. Ini yang menyebabkan ketika kita ubah
   data asli (data_2D) maka data_2D_copy ikut berubah"""

#Contoh
print('\n==Contoh==')