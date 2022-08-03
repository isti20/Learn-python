gol = input("Golongan parkir?(harian/langganan) ")
langganan = 50000
if gol == 'harian' :
    ongkos = 3000
    jmljam = input("Lama parkir?(jam) ")
    jmljamx = int(jmljam)
    for i in range (1,jmljamx):
        ongkos += 2000
        if ongkos > 22000:
            ongkos = 20000
            break
    print(ongkos)
elif gol == 'langganan' :
    ongkos = 5000
    langganan -= ongkos
    print('Sisa saldo anda Rp. {}'.format(langganan))
else:
    print('Golongan parkir tidak ada')
