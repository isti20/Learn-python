# Perulangan (loop)

# for kondisi:
# 	aksi

# ini dengan list
angka2_list = [0,2,4,8,10] # ini adalah list
print(angka2_list)

for i in angka2_list:
	print(f"i sekarang -> {i}")

print("akhir dari program 1 \n")

# ini dengan range
angka2_range = range(5) # dimulai dari nol --> 0,1,2,3,4

for i in angka2_range:
	print(f"i sekarang -> {i}")

print("akhir dari program 2 \n")

angka2_range = range(1,10) # dimulai dari 1 --> 1,2,3,4,5,6,7,8,9

for i in angka2_range:
	print(f"i sekarang -> {i}")
	# print("saya keren")

print("akhir dari program 3 \n")

for x in range(5): # dimulai dari nol --> 0,1,2,3,4
    print(x)

print("akhir dari program 4 \n")

for x in range(2, 30, 3): # dimulai dari 2 dengan penambahan 3 tiap looping --> 2,5,8,11,14,17,20,23,26,29 
  print(x)

# menggunakan string
data_str = "saya ganteng"

for huruf in data_str:
	print(huruf)

print("akhir dari program 5 \n")

for huruf in "banana":
	print(huruf)

print("akhir dari program 6 \n")

# menggunakan break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

print("akhir dari program 7 \n")

colors = ["red", "yellow", "green"]
for x in colors:
  if x == "yellow":
    break
  print(x)

print("akhir dari program 8 \n")

# menggunakan continue statement
animals = ["cat", "bird", "butterfly"]
for x in animals:
  if x == "bird": # bird di skip (tidak di print)
    continue
  print(x)

print("akhir dari program 9 \n")

# menggunakan else statement
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("akhir dari program 10 \n")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") #If the loop breaks, the else block is not executed.

print("akhir dari program 11 \n")

# menggunakan nested loop
colors = ["red", "yellow", "purple"]
numbers = ["1", "2", "3"]

for x in colors:
  for y in numbers:
    print(x, y)

print("akhir dari program 12 \n")

# menggunakan pass statement
for x in [0, 1, 2]:
  pass # hasilnya kosong

print("akhir dari program 13 \n")
