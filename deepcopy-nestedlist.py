"""Deep copy nested list"""

data_0 = [1,2]
data_1 = [3,4]
data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy() # di data list: copy() mengcopy ID address list data_0, data_1

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil data dari nested list

data = data_2D[1][0]
print(f"data = {data}")

#[1] yang pertama masuk ke list di dalam list (index ke-1)
#[0] yang ambil data didalam list yang kita masuki (index ke-0)

# address semuanya

print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")

# Hasilnya ID Address dari data_2D[0] dan data_2D_copy[0] adalah sama
# Karena copy() mengcopy ID Adress dari tiap data list di dalam data list (list bersarang)

# merubah data di dalam data list
data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# Hasilnya angka 3 di data_2D dan data_2D_copy berubah jadi 5
# Tapi data 10 di data_2D_copy tidak ikut berubah jadi 9
# Karena copy() mengcopy ID address data list

# kita gunakan deepcopy --> mengcopy data list bersarang

from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}") # data 3 di [3,4] tidak ikut berubah menjadi 30