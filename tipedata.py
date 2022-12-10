"""Tipe Data

Kategori tipe data python
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType

Note:
Data string bisa menggunakan single kutip atau double kutip
"""

#Tipe data kumpulan karakter (string)
print("==\nTipe data string==")
data_string = "lala"
print(type(data_string))
print("data : ", data_string, "bertipe : ", type(data_string))

#Tipe data: angka satuan (integer)
print("==Tipe data integer==")
data_integer = 1
print(type(data_integer))
print("data : ",data_integer,"bertipe :",type(data_integer))

#Tipe data: angka dengan koma (float)
print("\n==Tipe data float==")
data_float = 1.5
print(type(data_float))
print("data :", data_float, "bertipe :", type(data_float))

#Tipe data khusus: bilangan kompleks
print("\n==Tipe data kompleks==")
data_complex = complex(5,6) #angka 5 bil.real & angka 6 bil.imajiner
print(data_complex)
print("data complex: ", data_complex, "bertipe: ", type(data_complex))

#Tipe data biner: True/False (boolean)
print("\n==Tipe data Boolean==")
data_boolean = True
print(data_boolean)
print("data :", data_boolean, "bertipe : ", type(data_boolean))


#Tipe data dari bahasa C
#from ctypes import c.double 
#data_c_double = c_double(10.5) #double merupakan salah satu dari bahasa c
#print("data : ", data_c_double)
#print("data : ", data_c_double, "bertipe : ", type(data_c_double))

print("\n==Contoh-contoh lain==")
# Text Type: str
print("==Text Type: str==")
x = "Hello World"
print(x)

# Numeric Types: int, float, complex
print("\n==Numeric Types: int, float, complex==")
x = 20
y = 20.5
z = 1j
print(x, y, z)

# Sequence Types: list, tuple, range
print("\n==Sequence Types: list, tuple, range==")
x = ["apple", "banana", "cherry"]
y = ("apple", "banana", "cherry")
z = range(6)
print(x)
print(y)
print(z)

# Mapping Type: dict
print("\n==Mapping Type: dict==")
x = {"name" : "John", "age" : 36}
print(x)

# Set Types: set, frozenset
print("\n==Set Types: set, frozenset==")
x = {"apple", "banana", "cherry"}
print(x)

x = frozenset({"apple", "banana", "cherry"})
print(x)

# Boolean Type: bool
print("\n==Boolean Type: bool==")
x = True
print(x)

# Binary Types: bytes, bytearray, memoryview
print("\n==Binary Types: bytes, bytearray, memoryview==")
x = b"Hello"
print(x)

x = bytearray(5)
print(x)

x = memoryview(bytes(5))
print(x)

# None Type: NoneType
print("\n==None Type: NoneType==")
x = None
print(x)

# Random Number
import random

print(random.randrange(1, 10))










