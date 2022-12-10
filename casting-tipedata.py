"""Casting tipe data adalah merubah tipe data dari
   satu tipe data ke tipe yang lain"""

"""Kita akan merubah tipe data integer ke tipe data float"""

print("==Casting tipe data==")
data_int = 9
print("data :", data_int, "bertipe :", type(data_int))

"""cara merubahnya adalah"""
data_float = float(data_int)
print("data float: ", data_float, "bertipe: ", type(data_float))

"""Keterangan:
output dari data fload adalah 9.0 artinya yang tadinya 9 itu data integer
berubah menjadi data float.

note:
1. Data integer jika diubah ke data boolean outputnya akan False
   jika nilai integernya adalah 0 dan akan True jika nilai integernya 
   bukan 0
2. data float jika diubah ke data integer maka akan dibulatkan ke
   bawah nilainya. Misal: angka 9.9 akan menjadi 9
3. Data string dapat diubah ke data integer atau float jika stringnya
   adalah angka (bukan huruf)
4. Data string yang isinya kosong jika diubah ke data boolean maka
   outputnya akan False, sebaliknya jika ada isinya maka akan True
"""

## INTEGER
print("====INTEGER====")
data_int = 9;
print("data = ", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # akan false jika nilai int = 0
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

## FLOAT
print("====FLOAT====")
data_float = 0;
print("data = ", data_float, ",type =",type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
data_str   = str(data_float)
data_bool  = bool(data_float) # akan false jika nilai float = 0
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = False;
print("data = ", data_bool, ",type =",type(data_bool))

data_int = int(data_bool) # hasilnya 0 jika data bool adalah False
data_str   = str(data_bool)
data_float  = float(data_bool) # hasilnya akan 0.0 jika data bool adalah false
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_float, ",type =",type(data_float))

## STRING
print("====STRING====")
data_str = "10";
print("data = ", data_str, ",type =",type(data_str))

data_int    = int(data_str) # string harus angka
data_float  = float(data_str)  # string harus angka
data_bool   = bool(data_str) # false jika string kosong
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_bool, ",type =",type(data_bool))


