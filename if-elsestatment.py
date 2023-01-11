"""Percabangan: If dan Else Statement (memprogram satu alur).
Alur percabangan if:
1. program sebelumnya
2. if kondisi
3. aksi
4. program selanjutnya
"""
#Program if inline
print("\n==Program If Inline==")
nama = input("Siapa nama kamu?")
if nama == "lala": print("hi lala") #aksi true
print("program selesai") # end program

#Program if indentation (menjorok ke tengah)
print("\n==Program If Indentation==")
warna = input("Sebutkan salah satu warna pelangi?")
if warna == "merah":
    print("selamat! jawaban kamu benar") #aksi true
    print("kamu dapat hadiah permen yeay!") #aksi true
print("program selesai")

#Program Else Statment
"""Alur percabangan else statment
1. If kondisi
2. Aksi True
3. Else
4. Aksi False
"""
print("\n==Program Else Statment==")
hobi = input("Apa hobi kamu?")
if hobi == "membaca":
    print("Hobi kamu adalah:",hobi)
else:
    print("Hobi kamu bukan membaca ya")
print("program selesai")

#Program Elif (Else-If) Statment
"""Alur percabangan Elif statment
1. If kondisi
2. Aksi true
3. Elif kondisi
4. Aksi true
5. Else
6. Aksi
"""
print("\n==Program Elif statment==")
namahari = input("Masukkan nama hari?")
if namahari == "senin":
    print("Hari ini adalah hari senin")
elif namahari == "selasa":
    print("Hari ini adalah hari selasa")
else:
    print("Bukan hari senin dan selasa")
print("program selesai")

