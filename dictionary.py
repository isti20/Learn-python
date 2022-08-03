"""Dictionary"""

#List --> contohnya array (mengakses menggunakan index)
print('\n==List==')
data_list = ['ucup','otong','dudung']
print(data_list[0])

#Dictionary (dict) --> associative array
#Dict mengakses menggunakan identifier (key)

print('\n==Dict==')
data_dict = {
    'key1':'value1',
    'key2':'value2'
}
print(data_dict)

print('\n==Contoh Dict==')
data_nama = {
    'cp':'ucup', #isinya bebas, bisa list juga
    'tg':'otong',
    'dg':'dudung'
}

print(data_nama['tg'])
