class Mahasiswa:
    def __init__(self,nama,nim,hobi):
        self.nama = nama
        self.nim = nim
        self.hobi = hobi
    
    def __str__(self):
        return 'Nama mahasiswa: {}, nim: {}, hobi: {}'.format(self.nama,self.nim,self.hobi)

if __name__ == '__main__':
    lala = Mahasiswa('Lala','12345','Menyanyi')
    print(lala)