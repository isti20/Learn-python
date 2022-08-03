"""Copy & Pop Dictionary
"""

teman_teman = {
    "cup":"ucup",
    "tong":"otong",
    "dung":"dudung"
}

friends = teman_teman.copy()
print(f"friends: {friends}")

"""Sekarang kita akan ubah member di data asli (teman_teman)
   yaitu ucup, maka data di data copy tidak ikut berubah
"""
print('\n==Setelah data teman_teman diubah==')
teman_teman ["cup"] = "ucup keren"
print(f"teman-teman = {teman_teman}")
print(f"friends = {friends}")

#Pop dictionary: mentransfer data berdarkan key
print('\n==Pop dictionary==')
dataDudung = friends.pop("dung") #dung friendship.pop ditransfer ke dataDudung
print(f"data dudung = {dataDudung}") #hasilnya dudung
print(f"friends = {friends}") #data dudungnya tidak ada (sudah ditransfer ke dataDudung)

#Pop item dictionary: mengambil data terakhir
print('\n==Pop item dictionary==')
dataTerakhir = friends.popitem() 
print(f"data terakhir = {dataTerakhir}")
print(f"friends = {friends}") #sisa data


