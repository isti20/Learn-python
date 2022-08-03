"""Mengambil input dari data user.

langkah-langkah:
1. Membuat print untuk input user menggunakan method input
   (tambahkan kata input didepan dalam kurung data string)
2. Coba jalankan dan masukkan datanya, maka akan muncul. Jika
   kita input angka 9 maka akan diprint 9"""

print("==Mengambil input dari data user==")
data = input("Masukan data: ")
print("data:", data)

print("\n==Data yang dimasukkan pasti string==")
data = input("Masukan data: ")
print("data : ", data, "bertipe:", type(data))

"""Jika ingin data yang diinput user hasilnya data integer, maka
   caranya sbb:"""
print("\n==Mengambil data integer==")
data = input("Masukan data: ")
print("data: ", data, "bertipe:", type(data))

data_int = int(input("Masukan data: "))
print("data int: ", data_int, "bertipe: ", type(data_int))

"""Bagaiamana dengan data boolean? Jika data integer yang diinput
   nilainya 1 maka outputnya True, jika 0 maka outputnya False.

Note:
1 dan 0 adalah data boolean """

print("\n=Data inputan bertipe boolean==")
biner = bool(int(input("Masukan nilai boolean: ")))
print("data biner: ", biner, ",bertipe: ", type(biner))

