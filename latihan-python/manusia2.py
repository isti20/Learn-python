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

aku = ManusiaHidup("wiku","tasik")
print(aku) #Hasilnya: dari __str__(self)
print(aku.bersuara()) #bersuara itu dari def bersuara(self), itu adalah method jadi manggilnya pakai ()

print('\n')

kamu = ManusiaHidup("joko","bandung")
print(kamu)
print(kamu.bersuara())

print('\n')
