# If dan Else Statement

# 1. if nya
# 2. kondisinya
# 3. aksinya

nama = input("Siapa nama anda? ")

# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1. program if inline (harus satu baris kondisi dan aksinya)
# if nama=="ucup" : print("Kamu Ganteng abieeez!!!!")
# print(f"Terima kasih {nama}")

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Kedua kondisi benar")

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("Setidaknya salah satu kondisi benar")

# x = 41
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

# a = 33
# b = 200
# if b > a:
#   pass # menskip aksi

# 2. program if indentation

# if nama=="ucup":
# 	print("kamu ganteng abieeeez!")
# 	print("kamu juga keren banget!")
# print(f"Terima kasih {nama}")

# 3. Else Statement

if nama=="otong":
	print("hai otooong, si keren!!!")
else:
	print("Ah kamu bukan otong, kamu gak keren! :(")

print("akhir dari program")

a = 2
b = 330
print("A") if a > b else print("B")