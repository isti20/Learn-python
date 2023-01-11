"""Operator Dictionary"""

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung"
}

#Panjang dictionary
print('\n==Panjang Dictionary==')
LENDICT = len(data_dict)
print("panjang dictionary : {}".format(LENDICT))

#Mengecek key exist atau tidak
print('\n==Mengecek key exist atau tidak==')
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

#Mengakses value (read) dengan get
print('\n==Mengakses value (read) dengan get==')
print(data_dict["cup"])
print(data_dict.get("cup")) # pakai get untuk mengetahui data dict bukan (eror jika pakai get pada data bukan data dict)
print(data_dict.get("kis")) #hasilnya none karena tidak ada data dengan key "kis"
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan
print(data_dict.values())

#Mengupdate data
print('\n==Mengupdate data==')
data_dict["cup"] = "ucup ganteng"
print(data_dict)

##Hasilnya ucup surucup berubah menjadi ucup ganteng

#Menambah data
print('\n==Menambah data==')
data_dict["sep"] = "asep"
print(data_dict)

##hasilnya pada data ditambah key: sep, data: asep

#Mengupdate data yang sudah ada
"""Bedanya dengan cara mengupdate data di atas adalah:
   jika menggunakan cara ini maka data yang diupdate
   jika datanya belum ada maka otomatis datanya akan
   ditambahkan
"""
print('\n==Mengupdate data & otomatis menambahkan (jika data belum ada)==')
data_dict.update({"cup":"ucup surucup"})
print(data_dict)

data_dict.update({"faqih":"faqihza"})
print(data_dict)

##karena data faqih belum ada, maka otomatis ditambahkan

#Mendelete data pada dictionary
print('\n==Mendelete data pada dictionary==')
del data_dict["cup"] ##hasilnya: data ucup tidak ada (sudah dihapus)
print(data_dict)
data_dict.pop("tong")
print(data_dict)

data_dict.popitem() #mendelete data terakhir yaitu faqih: faqihza
print(data_dict)

#Mengosongkan data pada ductionary
print('\n==Mengosongkan data pada dictionary==')
data_dict.clear()
print(data_dict)

#Melooping data pada dictionary
print('\n==Melooping semua key names data pada dictionary==')
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict: #melooping key names data pada dictionary
  print(x)

for x in thisdict.keys():
  print(x)

print('\n==Melooping semua values data pada dictionary==')
for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

print('\n==Melooping melalui keys dan values data pada dictionary==')
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

#Mengcopy data pada dictionary
print('\n==Mengcopy data pada dictionary==')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

#Nested data pada dictionary
print('\n==Nested data pada dictionary==')
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

print('\natau')

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

