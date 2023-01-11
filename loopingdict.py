"""Looping Dictionary"""

teman_teman = {
    "cup":"ucup",
    "tong":"otong",
    "dung":"dudung"
}

#Looping first try (yang keluar key nya)
print('\n==Keluar Key nya aja==')
for teman in teman_teman:
    print(teman)

#Operator untuk mengambil item/iterables
print('\n==Contoh mengambil item 01==')
keys = teman_teman.keys()
print(keys) #hasilnya: disebut iterables

print('\n==Contoh mengambil item 02==')
for key in teman_teman.keys():
    print(teman_teman.get(key))

print('\n==Contoh mengambil item 03==')
value = teman_teman.values()
print(value)

for value2 in teman_teman.values():
    print(value2)

print('\n==Contoh mengambil item 05==')
items = teman_teman.items()
print(items)

print('\n==Contoh mengambil item 06==')
for item in teman_teman.items():
    print(item)

print('\n==Contoh mengambil item 07==')
for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")

"""
Note:
Kalo kita looping biasa: yang diambil hanya key nya saja
"""