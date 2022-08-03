def harian(jam,tipe):
    c = 0
    if tipe == 'mobil':
        c = 2000 * jam
    elif tipe == 'motor':
        c = 1000*jam
    else:
        c = 4000
    return c

def langganan(saldo):
    d = saldo-5000
    return d

gol = input('Golongan parkir = (harian/langganan)')
tipe = input('Tipe kendaraan?(mobil/motor)')
if gol == 'harian':
    jamnya = input('Berapa jam?')
    jamnyaint = int(jamnya)
    ongkos = harian(jamnyaint,tipe)
    print('Ongkos parkir = {}'.format(ongkos))

elif gol == 'langganan':
    saldo = 40000
    saldoakhir = langganan(saldo)
    print('Saldo anda = {}'.format(saldoakhir))