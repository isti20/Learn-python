from ini import StafPengajar

class Dosen(StafPengajar):
    def __init__(self,matkul,nama,nip,alamat):
        self.matkul = matkul
        super().__init__(nama,nip,alamat)
    
    def __str__(self):
        return '{} || {} || {} || {}'.format(self.nama,self.nip,self.alamat,self.matkul)

class Asdos(StafPengajar):
    pass

wiku = Dosen('python','wiku','23456','tasik') #wiku ini variabel yang menunjuk ke object dosen
print(wiku)
wiku.nama = 'wina' #mengganti nama wiku jadi wina
print(wiku)
wiru = wiku
print(wiru) #outputnya: sama-sama namanya wina (karena variabel wiku diubah parameternya maka variabel wiru juga ikut berubah)
            #itu karena wiku dan wiru menunjuk ke object yg sama, yaitu dosen