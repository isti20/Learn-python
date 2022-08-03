"""While loop (perulangan). While artinya saat.

Alur perulangan while loop:
1. while kondisi (boolean)
2. aksi ini
3. aksi itu
4. akhir dari program
"""

print("\n==While loop==")
#angka = 10
#while angka > 5: # angka > 5 itu True (karena kondisi selalu True maka akan ngeloop terus)
    #print("faqihza")
#print("cukup") #outputnya mengulang 'faqihza' tanpa henti
"""Untuk menjalankan while loop ini hilangkan # didepan kata print(cukup)
da print("faqihza")
"""
"""Note:
tekan alt+c untuk menghentikan output.
"""
print("\n==While loop dengan batas==")
nomor = 0 #nomor dimulai dari 0 (lihat disini)
while nomor < 5: #akan diulang sebanyak 5x dimulai dari 0
    nomor += 1 #saat ketemu ini nomor akan ditambah 1
    print("faqihza")
print("selesai")

"""Penjelasan output:
faqihza (0+1=1)
faqihza (1+1=2)
faqihza (2+1=3)
faqihza (3+1=4)
faqihza (4+1=5) setelah ini selesai karena kondisinya < 5
selesai 
"""
#Continue dan pass
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

print("\n==Pass==")
nomorjuga = 0
while nomorjuga < 5:
    nomorjuga += 1
    if nomorjuga == 3:
        pass #tidak melakukan apa-apa (dummy)
        print("Yuhuuu!")
    print(nomorjuga)

"""def (fungsi) pass : fungsi ini tidak akan dieksekusi, itu salah
   satu fungsi pass"""

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
jadi akan menammpilkan data sebanyak jumlah angka yang diinput.
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