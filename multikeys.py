"""Multi keys dan Nesting Dictionary"""

import datetime
mahasiswa1 = {
    "nama":"ucup",
    "nim":"19022001", #data string
    "sks_lulus":130, #data number
    "beasiswa":False, #data boolean
    "lahir":datetime.datetime(2001,4,10)
}

print(mahasiswa1)

data_mahasiswa = {
    "MAH001":"Mahasiswa1",
    "MAH002":"Mahasiswa2",
    "MAH003":"Mahasiswa3"
}

print(f"{'KEY':<6}{'nama':<17}{'sks':<3}{'beasiswa':<9}{'lahir':<10}")

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strf('%x')

print(f"{'KEY':<6}{'nama':<17}{'sks':<3}{'beasiswa':<9}{'lahir':<10}")
