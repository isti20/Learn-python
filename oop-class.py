"""
Object Oriented Programming (OOP): paradigma pemrograman yang berorientasi
pada konsep class (kelas) dan object (objek).

class Kendaraan: 
    def __init__(self,kecepatan,jarak): 
        self.max_speed = kecepatan 
        self.mileage = jarak

Note:
- Class Kendaraan adalah parent class. Huruf awal pada class kapital (aturan kesepakatan)
- def __init__ adalah fungsi constructor (spesial method). Kecepatan dan jarak adalah
  attribute dari class Kendaraan yang didefinisikan oleh fungsi contructor (def __init__)
- self.max_speed adalah object attribute dari attribute kecepatan dan self.mileage adalah
  object attribute dari attribute jarak.

Dengan perumpamaan:
Class sebagai template atau kategori umum seperti kendaraan yang memiliki
karakteristik (attribute) dan perilaku (method) untuk membuat sebuah object.

Contoh:
Kita punya class Kendaraan. Ia memiliki attribute kecepatan dan jarak dan
didalam mobil memiliki method KecepatanMax() dan JarakTempuh().

Attribute adalah karakteristik dari sebuah class. Attribute ini berupa
suatu variabel di dalam class, disebut variabel global/instance (turunan) 
variabel.

Method adalah fungsi yang didefinisikan dalam suatu class. Biasanya method
memiliki hubungan dalam behaviour/perilaku class tersebut.
Disetiap mendefinisikan sebuah method parameter keyword self harus selalu
ada. Misal: Melaju(self).

Kenapa harus ada parameter self? agar dapat mengakses attribute atau method
dari class tersebut. Misal: print(Kendaraan.Melaju())

Object adalah instance atau representasi dari sebuah class. Jika class adalah
sebuah cetakan, maka object adalah adalah hasil dari cetakan tersebut.

Cara mendeklarasikan object dari sebuah class pada python adalah dengan
memanggil nama class beserta dengan parameter yang diberikan pada fungsi
contructor (__init__). Misal: busku = Bus("Volvo",180,12)
Bus adalah object(child class) dan ("Volvo",180,12) adalah parameter

Variabel global didefinisikan dalam fungsi constructur (__init__) dan
menggunakan keyword self. Kenapa pakai constructor? karena instance
variabel hanya bisa didefinisikan dari sebuah method.

Jika class adalah blueprint dari suatu kategori yang umum, maka objek di
umpamakan sebagai hal yang lebih spesifik seperti Bus. Jadi, class kendaraan
tadi bisa membuat banyak objek yang lebih spesifik, misal Bus atau Truk.

Class Kendaraan:
- Attribute(properties): kecepatan dan jarak
- Method: Melaju dan Jarak Tempuh

Child class (object):

Note:
def __init__(self):
    self.roda = None
    self.tipe = None
    self.kecepatan = 0

pada kode diatas kita mendeklarasikan attribute dengan nilai default
(None dan 0) menggunakan fungsi constructor (__init__) pada class.

Sedangkan pada kode dibawah ini, nilai pada instance variavel didefinisikan
mengikuti parameter yang diberikan pada fungsi constructor (__init__)

def __init__(self,kecepatan,jarak):
        self.max_speed = kecepatan
        self.mileage = jarak

Penerapan kedua kode diatas tergantung kondisi pada saat pendeklarasian
sebuah object, apakah object ini perlu parameter atau tidak. Jika tidak
maka pakai kode default.
"""

class Kendaraan: #parent class (class kendaraan)
    def __init__(self,kecepatan,jarak): #fungsi constructor (__init__) adalah special method. Kecepatan dan Jarak adalah attribute / parameter yang disefinisikan fungsi __init__
        self.max_speed = kecepatan #max_speed dan mileage -> object attribute
        self.mileage = jarak

    def Melaju(self): #Melaju(self) adalah method
        return 'Melaku dengan kecepatan maksimal : {}'.format(self.max_speed)
    def JarakTempuh(self): #JarakTempuh(self) adalah method
        return 'jarak tempuh kendaraan : {}'.format(self.mileage)

class Bus(Kendaraan): #Class Bus adalah object. Class bus extend ke class Kendaraan jadi attribute kecepatan dan jarak tidak perlu di definisikan lagi (inheritance)
    safety_level = 'Level IV' #class attribute
    def __init__(self,merk,kecepatan,jarak): 
        self.brand = merk #Hanya merk yang didefinisikan karena Bus sudah extend ke class Kendaraan
        super().__init__(kecepatan,jarak) #super init untuk mendefinisikan kecepatan, jarak di class Kendaraan
    def __str__(self): #Fungsi constructor (__str__) untuk menampilkan output
        return 'kendaraan merk = {}, kecepatan maksimal = {}, jarak tempuh = {} dan level safety = {}'.format(self.brand,self.max_speed,self.mileage,self.safety_level)

busku = Bus("Volvo",180,12) #variabel busku ingin memanggil class Bus makanya namanya busku
print(busku)
print(busku.Melaju())