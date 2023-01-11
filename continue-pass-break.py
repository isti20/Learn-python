#Menyelipkan data
print("\n==Menyelipkan data==")
print("==contoh ke-1 menyelipkan data==")
angkasaja = 0
while angkasaja < 5:
    angkasaja +=1
    print(angkasaja)

print("==contoh ke-2 menyelipkan data==")
angkalagi = 0
while angkalagi < 5:
    angkalagi += 1
    if angkalagi == 3: #artinya pada saat angkalagi sama dengan 3 maka akan mencetak whadaw!
        print("whadaw!")
    print(angkalagi) #setelah itu melanjutkan looping hingga kondisi terpenuhi
print("selesai")

print("==contoh ke-3 menyelipkan data==")
angkajuga = 0
while angkajuga < 5:
    angkajuga += 1
    print(f"angka sekarang: {angkajuga}")
    if angkajuga == 2:
        print("Nice!")
        print("whatsup!")
    print("selesai")

# continue (melanjutkan ke step berikutnya)
print("\n==Continue==")
nomorlagi = 0
while nomorlagi < 5:
    nomorlagi += 1
    print(f"nomor sekarang: {nomorlagi}")
    if nomorlagi == 3:
        print("Good!") #saat nomorlagi ==3 program menampilkan good lalu continue keawal
        continue #setelah ini lanjut ke atas (tidak print hellow)
    print("helllowwww")
print("finish")

# pass (bersifat dummy)
print("\n==Pass==")
nomorjuga = 0
while nomorjuga < 5:
    nomorjuga += 1
    if nomorjuga == 3:
        pass #tidak melakukan apa-apa (dummy)
        print("Yuhuuu!")
    print(nomorjuga)

"""pass : fungsi ini tidak akan dieksekusi, itu salah
   satu fungsi pass"""

# break (berhenti)
print("\n==Break==")
print("\n==Contoh ke-1 Break==")
nomorlain = 0
while nomorlain < 5:
    nomorlain += 1
    print(f"angka lain:{nomorlain}")

    if nomorlain == 3: #setelah mencapai 3 program berhenti (break)
        print("Okeeey!")
        break
    print("Siaaaappp")
print("finishh")

print("\n==Contoh ke-2 Break==")
dataint = int(input("Hitung sampai ="))
angka = 0
while True:
    angka += 1
    print(f"count = {angka}")
    if angka == dataint:
        print("Nice!")
        break
    print("Helllow!")
print("selesai")

"""Keterangan:
saat kita input datanya bilangan positif maka kondisinya True,
jadi akan menampilkan data sebanyak jumlah angka yang diinput.
Misal:3 maka outputnya:
Count = 1
Helllow!
Count = 2
Helllow!
Count = 3
Nice!
Selesai

tapi kalo kita inputkan datanya bilangan negatif, misalnya -1
maka kondisinya jadi False, sehingga akan terus melooping tanpa
henti.
"""