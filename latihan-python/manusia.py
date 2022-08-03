"""Membuat class"""
class ManusiaHidup: #nama kelas harus diawali huruf kapital
    jmltangan = 2 #class attribute
    def __init__(self,nama,alamat): # def __init__ adalah constructor
        self.name = nama            # constructor adalah special method yang dipanggil pada saat instalasi/pembuatan object (instance)
        self.address = alamat       # name dan address adalah object attribute

aku = ManusiaHidup("wiku","tasik")
print(aku.name)
print(aku.address)
print(ManusiaHidup.jmltangan)

print('\n')

kamu = ManusiaHidup("joko","bandung")
print(kamu.name)
print(kamu.address)

print('\n')


