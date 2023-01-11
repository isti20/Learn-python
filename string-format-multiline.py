# Width and Multiline

# Data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)
print(data_string.format(data_nama, data_umur, data_tinggi, data_nomor_sepatu))

data_ucup = "nama saya {} umur {} tinggi {} nomor sepatu {}"
print(data_ucup.format(data_nama, data_umur, data_tinggi, data_nomor_sepatu))

jumlah = 3
buah = "mangga dan apel"
price = 20000
myorder = "Saya ingin membeli {1} sebanyak {0} yang harganya {2}." # menggunakan indexing
print(myorder.format(jumlah, buah, price))

# String multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Ucup Surucup"
data_tinggi = 105.17
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>12}
tinggi = {data_tinggi:>12}
sepatu = {data_nomor_sepatu:>12}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)