"""Membuat class"""
class ManusiaHidup: #nama kelas harus diawali huruf kapital
    jmltangan = 2 #class attribute
    def __init__(self,nama,alamat): # def __init__ adalah constructor
        self.name = nama            # constructor adalah special method yang dipanggil pada saat instalasi/pembuatan object (instance)
        self.address = alamat       # name dan address adalah object attribute
        self.jmlmata = 'dua'

    def bersuara(self):
        return 'haloooo namaku {}'.format(self.name)
    
    def __str__(self):
        return 'Namaku {} alamat di {} jumlah tangan {} dan punya mata {}'.format(self.name,self.address,self.jmltangan,self.jmlmata)

class Makhluk:
    def bersuara(self):
        return 'Halo aku {}'.format("makhluk hidup") #"makhluk hidup akan direturn"

class Pegawai(Makhluk,ManusiaHidup): #Pegawai adalah child class dari class ManusiaHidup
    pass 
          

dia = Pegawai("Andi","Surabaya") #Class pegawai karena anaknya dari class ManusiaHidup jadi dia mewarisi constructor dari class ManusiaHidup
print(dia)                       #Jadi hasilnya dari contructor class ManusiaHidup
print(dia.bersuara()) #outputnya: halo aku makhluk hidup --> dari class Makhluk
                      #Jadi dieksekusi dari kiri (kalo method bersuara ada di class Makhluk maka itu yang dipakai, jika tidak ada baru dieksekusi yang di class ManusiaHidup
                      #Ini jika ada method dari class yang kembar


