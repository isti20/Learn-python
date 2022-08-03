from parkirfunc import harian,langganan

golongan = input('Masukkan tipe parkir = (harian/langganan)')

if golongan == 'harian':
    biaya = 3000
    jamparkir = input('Masukkan lama parkir?')
    jmljam = int(jamparkir)

    for i in range(1,jmljam): #range dimulai dari index ke-1
        biaya += 2000
        if biaya > 22000:
            biaya = 20000
            break
    print("Total biaya parkir", biaya)
elif golongan == 'langganan':
        langganan = 50000
        biaya = 5000
        langganan -= biaya
        print('Sisa saldo anda Rp. {}'.format(langganan))
else:
    print('Golongan parkir tidak ada')
print("selesai")



    

