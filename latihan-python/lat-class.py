class Kendaraan:
    def __init__(self,kecepatan,jarak):
        self.max_speed = kecepatan
        self.mileage = jarak

    def KecepatanMax(self):
        return 'kecepatan maksimal kendaraan : {}'.format(self.max_speed)
    def JarakTempuh(self):
        return 'jarak tempuh kendaraan : {}'.format(self.mileage)

class Bus(Kendaraan): #bus extend ke kendaraan
    safety_level = 'Level IV' #class attribute
    def __init__(self,merk,kecepatan,jarak): #
        self.brand = merk
        super().__init__(kecepatan,jarak) #super init untuk mengambil kecepatan, jarak di class Kendaraan
    def __str__(self):
        return 'kendaraan merk = {}, kecepatan maksimal = {}, jarak tempuh = {} dan level safety = {}'.format(self.brand,self.max_speed,self.mileage,self.safety_level)

busku = Bus("Volvo",180,12)
print(busku)
print(busku.KecepatanMax())