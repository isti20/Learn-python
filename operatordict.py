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
print(data_dict.get("cup"))
print(data_dict.get("kis")) #hasilnya none karena tidak ada data dengan key "kis"

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
del data_dict["cup"]
print(data_dict)

##hasilnya: data ucup tidak ada (sudah dihapus)