class Staff:
    def __init__(self,fullname,nip,gender):
        self.fullname = fullname
        self.nip = nip
        self.gender = gender
    
    def __str__(self):
        return 'Nama lengkap: {}, nip: {}, gender: {}'.format(self.fullname,self.nip,self.gender)

if __name__ == '__main__':
    staffX = Staff('Lala','12345','Perempuan')
    print(staffX)