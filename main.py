from google.colab import files
files.upload()

#Import Module
from SuperCashier import Transaction

trnsct_123 = Transaction()
#Menampilkan menu Utama Super Cashier
print('                  WELCOME TO SUPERMARKET KEJUJURAN                 ')
print('===================================================================')
print('                        SELF SERVICE CASHIER ')
print('===================================================================')
print('\n1. Tambah item yang dibeli \n2. Ubah nama item \n3. Ubah jumlah item \n4. ubah harga item \n5. Delete Item \n6. Reset transaksi \n7. Periksa list belanja \n8. Pembayaran \n9. Selesai Transaksi')
print('===================================================================')
while True:
    try:
        fitur = input('\nPilih fitur yang diinginkan : ')
        fitur01=int(fitur)
    except ValueError:
        print("Menu yang diinput tidak sesuai")

    if fitur01 == 1:
          trnsct_123.add_item()

    elif fitur01 == 2:
          trnsct_123.update_item_name()

    elif fitur01 == 3:
          trnsct_123.update_item_qty()

    elif fitur01 == 4:
          trnsct_123.update_item_price()

    elif fitur01 == 5:
          trnsct_123.delete_item()

    elif fitur01 == 6:
          trnsct_123.reset_transaction()

    elif fitur01 == 7:
          trnsct_123.check_item()

    elif fitur01 == 8:
          trnsct_123.total_payment()

    elif fitur01 == 0:
        print('Terima kasih sudah berbelanja di Supermarket Andi. ')
        break

    else:
        print("Menu tidak tersedia")

