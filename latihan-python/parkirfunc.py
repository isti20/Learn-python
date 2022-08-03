def harian(jam):
    a = 0
    if jam == 1:
        a = 3000
    elif jam >= 2:
        a = 3000 + (jam-1)*2000
        if a > 22000:
            a = 20000
    return a

def langganan(saldo):
    b = saldo-5000
    return b

if __name__ == '__main__' : #berfungsi untuk test program utama
    golongan = input('Masukkan golongan parkir = (harian/langganan)')
    if golongan == 'harian':
        jamparkir = input('Masukkan lama parkir?')
        jam = int(jamparkir)
        biaya = harian(jam)
        print("Total biaya parkir {}".format(biaya))
    elif golongan == 'langganan':
        saldo = 50000
        saldoakhir = langganan(saldo)
        print('Saldo anda = {}'.format(saldoakhir)) 