# operator dalam bentuk methods

## merubah case pada string

# merubah semua ke upper case
salam = "bro!"
print("normal " + salam)
salam = salam.upper()
print("upper " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieeZZZ"
print("normal " + alay)
alay = alay.lower()
print("lower " + alay)

# merubah huruf pertama menjadi kapital
txt = "huruf pertama menjadi kapital"
x = txt.capitalize()
print (x)

# merubah huruf pertama menjadi huruf kecil 
txt = "Huruf pertama menjadi huruf kecil"
x = txt.casefold()
print(x)

## method is, untuk pengecekan

# contoh isupper()
salam = "SIST"
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))
salam = salam.lower()
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah desimal
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case
# isdigit() <- untuk mengecek apakah angka semua
# isnumeric() <- apakah numerik semua

judul = "It Is Okay To Not Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))

# startwith() dan endwith() <-- keren

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start " + str(cek_start))
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end " + str(cek_end))

# join() dan split() <-- buat orang males

pisah = ['aku','sayang','kamu']
gabungan = ' ehm '.join(pisah)
print(pisah)
print(gabungan)

myTuple = ("ada", "apa", "sayang")
x = "#".join(myTuple)
print(x)

gabungan = "naik vespa keliling kota"
pisah = gabungan.split()
print(gabungan)
print(pisah)
print(gabungan.split())

gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm")
print(gabungan)
print(pisah)

# alokasi karakter
print("'kiri      '")

kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'")

tengah ="tengah".center(20) # rata tengah dengan 20 karakter
print("'" + tengah + "'")

tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
print("'" + tengah + "'")

# kebalikan dari alokasi karakter (rata kiri)
txt = "     pisang     raja"
x = txt.lstrip()
print(x)

# menghapus spasi diawal atau akhir
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# mengganti karakter string
a = "Hello, World!"
print(a.replace("H", "J")) # H diganti J

txt = "Hai Sam San!"
mytable = txt.maketrans("S", "P") # S diterjemah jadi P
print(txt.translate(mytable))

