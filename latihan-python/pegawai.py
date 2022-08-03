from staff import Staff

class Dosen(Staff):
    jabatan = 'dosen'
    def __init__(self,matkul,fullname,nip,gender):
        self.matkul = matkul
        super().__init__(fullname,nip,gender)
    
    def __str__(self):
        return '\n\nNama lengkap: {}, nip: {}, jabatan: {}, gender: {}, Dosen mata kuliah: {}'.format(self.fullname,self.nip,self.jabatan,self.gender,self.matkul)

class Administrasi(Staff):
    jabatan = 'Staf Administrasi'
    def __init__(self,unit,fullname,nip,gender):
        self.unit = unit
        super().__init__(fullname,nip,gender)
    
    def __str__(self):
        return '\n\nNama lengkap: {}, nip: {}, jabatan: {}, gender: {}, unit: {}'.format(self.fullname,self.jabatan,self.nip,self.gender,self.unit)

class CleaningService(Staff):
    jabatan = 'Staf Cleaning Service'
    def __init__(self,area,fullname,nip,gender):
        self.area = area
        super().__init__(fullname,nip,gender)
    
    def __str__(self):
        return '\n\nNama lengkap: {}, nip: {}, jabatan: {}, gender: {}, area: {}'.format(self.fullname,self.nip,self.jabatan,self.gender,self.area)

dosen1 = Dosen('python','lili','66666','perempuan')
print(dosen1)
admin1 = Administrasi('kemahasiswaan','didi','77777','laki-laki')
print(admin1)
cs1 = CleaningService('gedung A','lulu','88888','perempuan')
print(cs1)
