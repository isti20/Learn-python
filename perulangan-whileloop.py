"""While loop (perulangan). While artinya saat.

Alur perulangan while loop:
1. while kondisi (boolean)
2. aksi ini
3. aksi itu
4. akhir dari program
"""

print("\n==While loop==")
#angka = 10
#while angka > 5: # angka > 5 itu True (karena kondisi selalu True maka akan ngeloop terus)
    #print("faqihza")
#print("cukup") #outputnya mengulang 'faqihza' tanpa henti
"""Note:
tekan alt+c untuk menghentikan output.
"""
print("\n==While loop dengan batas==")
nomor = 0 #nomor dimulai dari 0 (lihat disini)
while nomor < 5: #akan diulang sebanyak 5x dimulai dari 0,1,2,3,4 < 5
    nomor += 1 #saat ketemu ini nomor akan ditambah 1
    print("faqihza")
print("selesai")

"""Penjelasan output:
faqihza (0+1=1)
faqihza (1+1=2)
faqihza (2+1=3)
faqihza (3+1=4)
faqihza (4+1=5) setelah ini selesai karena kondisinya < 5
selesai 
"""
