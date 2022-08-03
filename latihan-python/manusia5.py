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
    def berjalan(self):
        return "bisa berjalan"

class Makhluk:
    def __init__(self,jenkel):
        self.jenis = jenkel + 'dong'
    def bersuara(self):
        return "halo aku {}".format("makhluk hidup")
    def __str__(self):
        return self.jenis

class Pegawai(ManusiaHidup):
    def __init__(self,nama,alamat,jamtidur):
        self.tidur = 'aku tidur selama {} jam'.format(jamtidur)
        super().__init__(nama,alamat)
        print(super().bersuara()) #Outputnya: haloo namaku wiku

dia = Pegawai('wiku','tasik','7')
print(dia)
print(dia.tidur) #Outputnya: aku tidur selama 7 jam --> class Pegawai(ManusiaHidup)
print(dia.jmltangan) #Outputnya: 2 -->class atribute