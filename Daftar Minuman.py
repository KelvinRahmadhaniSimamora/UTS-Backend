total = 0
menu = []
harga = []
jenis= []

while True:
    print("List Minuman")
    print("========================================")
    print(" 1. Juice \t 7000 \t Juice Alpukat")
    print(" 2. Yogurt \t 11000 \t Orange Yogurt")
    print(" 3. Teh Manis \t 4000 \t Teh Manis Hangat")
    print(" 4. Hot Tea \t 10000 \t Chinese Oolong Tea")
    print(" 5. Kopi \t 8000 \t Arabica Kopi")
    print("========================================")

    kode = int(input("Masukan kode minuman :"))
    if kode == 1:
        menu.append('Juice')
        jenis.append('Juice Alpukat')
        harga.append(7000)
        total += 7000
    elif kode == 2:
        menu.append('Yogurt')
        jenis.append('Orange Yogurt')
        harga.append(11000)
        total += 11000
    elif kode == 3:
        menu.append('Teh Manis')
        jenis.append('Teh Manis Hangat')
        harga.append(4000)
        total += 4000
    elif kode == 4:
        menu.append('Hot Tea')
        jenis.append('Chinese Oolong Tea')
        harga.append(10000)
        total += 10000
    elif kode == 5:
        menu.append('Kopi')
        jenis.append('Arabica Kopi')
        harga.append(8000)
        total += 8000
    else:
        print("kode tidak valid")
    
    
    ulangi = ""
    while ulangi!=('y' or 't'):
        ulangi = input("Pesan Lagi ? y/t: ")
        if ulangi =='y':
            total+= 0
        elif ulangi == 't':
            break
        else:
            continue
    if ulangi == 't':
        break
    continue

print('minuman yang dibeli : ', menu)
print('harga minumannya : ', harga)
print('jenis minumannya : ', jenis)
print('total yang harus dibayar : ', total, '\n')

uang = int(input('masukan uang pembayaran'))
if uang > total:
    print('kembaliannya :', uang - total)
elif uang == total:
    print('uang pas')
else:
    print('uangnya kurang')


