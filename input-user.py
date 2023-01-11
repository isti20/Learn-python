"""Input user"""

#data yang dimasukan pasti string
data = input("Masukan data: ")
print("data = ",data,",type =",type(data))

#jika kita ingin mengambil int, maka
angka = int(input("masukan angka: "))
print("data = ",angka,",type =",type(angka))

# jika kita ingin mengambil biner (boolean)
biner = bool(int(input("masukan nilai boolean: ")))
print("data = ",biner,",type =",type(biner))