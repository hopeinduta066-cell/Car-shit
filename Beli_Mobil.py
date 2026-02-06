print('----Dealer Mobil----')
print('1.Mazda Rx7 FD3S - 7.000.000.000')
print('2.Mitsubishi Lancer Evo X - 700.000.000')
print('3.Porsche 911 GT3 RS - 13.500.000.000')
print('4.BMW M4 Competition - 3.200.000.000')
print('5.Audi RS7 Sportback - 2.500.000.000')
print('--------------------------------')


def get_item(choice):
    if choice == 1 :
        return 'Mazda Rx7 FD3S', 7000000000
    elif choice == 2 :
        return 'Mitsubishi Lancer Evo X', 700000000
    elif choice == 3 :
        return 'Porsche 911 GT3 RS', 13500000000
    elif choice == 4 :
        return 'BMW M4 Competition', 3200000000
    elif choice == 5 :
        return 'Audi RS7 Sportback', 2500000000
    else :
        return 'Mobil Tidak Ditemukan', 0


cart = []
while True:
    try:
        Choice = int(input('Pilih Nomor : '))
    except ValueError:
        print('Input tidak valid, masukkan nomor.')
        continue

    item_name, price = get_item(Choice)
    if price == 0:
        print('Pilihan Tidak Valid Coba Lagi')
        continue

    try:
        Jumlah_Pembelian = int(input('Masukkan Jumlah Pembelian : '))
    except ValueError:
        print('Jumlah tidak valid, coba lagi.')
        continue

    subtotal = Jumlah_Pembelian * price
    cart.append({'name': item_name, 'price': price, 'qty': Jumlah_Pembelian, 'subtotal': subtotal})

    lagi = input('Tambah mobil lagi? Yes or No : ').strip().lower()
    if lagi != 'yes':
        break

if not cart:
    print('Tidak ada pesanan.')
else:
    print('====Ringkasan Pesanan====')
    grand_total = 0
    for i, it in enumerate(cart, 1):
        print(f"{i}. {it['name']}")
        print(f"   Harga Satuan : Rp {it['price']:,}".replace(',','.'))
        print(f"   Jumlah Pembelian : {it['qty']}")
        print(f"   Subtotal : Rp {it['subtotal']:,}".replace(',','.'))
        grand_total += it['subtotal']

    print(f'Total Harga : Rp {grand_total:,}'.replace(',','.'))

print('====Terimakasih====')

