from pesertadidik import Mahasiswa

class MahasiswaS1(Mahasiswa):
    jabatan = 'Mahasiswa S1'
    def __init__(self,skripsi,nama,nim,hobi):
        self.skripsi = skripsi
        super().__init__(nama,nim,hobi)
    
    @classmethod
    def jmlsks(cls,sks):
        cls.sks = sks

    @classmethod
    def printjmlsks(cls):
        return '\n\nJumlah sks: {}'.format(cls.sks)
    
    def __str__(self):
        return '\n\nNama : {}, nim: {}, jabatan: {}, hobi: {}, skripsi: {}'.format(self.nama,self.nim,self.jabatan,self.hobi,self.skripsi)

class MahasiswaS2(Mahasiswa):
    jabatan = 'Mahasiswa S2'
    def __init__(self,tesis,nama,nim,hobi):
        self.tesis = tesis
        super().__init__(nama,nim,hobi)
    
    def __str__(self):
        return '\n\nNama : {}, nim: {}, jabatan: {}, hobi: {}, tesis: {}'.format(self.nama,self.nim,self.jabatan,self.hobi,self.tesis)

nina = MahasiswaS1('Kualitatif','nina','66666','traveling')
print(nina)
abel = MahasiswaS2('Kuantitatif','abel','77777','berenang')
print(abel)
MahasiswaS1.jmlsks('24')
print(MahasiswaS1.printjmlsks())
