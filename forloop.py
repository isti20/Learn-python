"""For loop (perulangan).

Alur loop (perulaangan)
1. Start
2. For kondisi
3. Aksi
"""
#Loop dari list
print("\n==Loop dari List==")
listnama = ['lala','lili','lulu']
print(listnama)
for i in listnama: #i disini member dari list namalist
    print(f"i sekarang:{i}")
print("akhir dari program") #outputnya ngambil satu-satu dari list

#Loop dengan range
print("\n==Loop dengan Range==")
angkarange = range(5) #range dimulai dari nol
print(angkarange)
for i in angkarange:
    print(f"i sekarang:{i}")
print("akhir dari program")

print("\n==Loop dengan range batas==")
rangebatas = range(1,5) #koma disini artinya pembatas
print(rangebatas)
for i in rangebatas:
    print(f"i range batas sekarang {i}") #range dari 1-5 tapi 5 tidak didiambil
print("akhir dari program")

#Loop dengan string
print("\n==Loop dengan string==")
datastr = "saya keren"
print(datastr)
for huruf in datastr:
    print(huruf)
print("akhir dari program")