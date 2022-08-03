class Rekening:
    def __init__(self,nama,rp):
        self.nama = nama
        self.__saldo = rp #underscore 2x di saldo berfungsi membuat saldo jadi private (tidak dapat diubah dari luar)

    def printsaldo(self):
        return 'Saldo anda {}'.format(self.__saldo)
    
    def nabung(self,rp):
        self.__saldo += rp
    
    def tarik(self,rp):
        if self.__saldo >= rp:
            self.__saldo -= rp
            print('{} berhasil menarik uang sejumlah Rp. {}'.format(self.nama,rp))
        else:
            print('Maaf {}, saldo anda tidak mencukupi'.format(self.nama))

wiku = Rekening('wiku',100000)
wiku.nabung(50000)
print(wiku.printsaldo())
wiku.tarik(200000)
print(wiku.printsaldo())
wiku.__saldo = 500000
wiku.tarik(200000)
print(wiku.printsaldo())





