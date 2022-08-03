class StafPengajar:
    def __init__(self,nama,nip,alamat):
        self.nama = nama
        self.nip = nip
        self.alamat = alamat
    
    def __str__(self):
        return '{} || {} || {}'.format(self.nama,self.nip,self.alamat)

class Administrasi:
    def __init__(self,nama,nip,alamat):
        self.nama = nama
        self.nipa = nip
        self.alamat = alamat

    def __str__(self):
        return '{} || {} || {}'.format(self.nama,self.nipa,self.alamat)

if __name__ == '__main__':
    dosenA = StafPengajar("andi","12345","yogya")
    print(dosenA)