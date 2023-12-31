# Membuat Class Transaction
from tabulate import tabulate
class Transaction:
    #membuat class transaction dengan dictionary self.item_awal
    def __init__(self):
        self.item_awal = {}

    #Function yang digunakan untuk menambah item ke dalam dictionary yang sudah dibuat
    def add_item(self):

        nama_item = input('Masukan nama item yang mau dibeli : ')
        while nama_item in self.item_awal:
            print(f'{nama_item} sudah ada dalam daftar belanja anda.')
            nama_item = input('Silahkan masukan ulang nama item yang mau dibeli : ')
        jumlah_item = int(input('Masukan jumlah item yang mau dibeli : '))
        harga_item = int(input('Masukan harga item yang mau dibeli : '))
        total_price = jumlah_item*harga_item
        print(f'{nama_item} berhasil ditambahkan')
        self.item_awal.update({nama_item : [jumlah_item, harga_item, total_price]})

    #Function yang digunakan untuk meng-update nama item ke dalam dictionary yang sudah dibuat
    def update_item_name(self):

        old_item_name = input('Masukan item yang mau diupdate : ')
        if old_item_name in self.item_awal:
            new_item_name = input('Masukan nama item yang benar untuk diupdate : ')
            self.item_awal[new_item_name] = self.item_awal.pop(old_item_name)
            print(f'Item berhasil diupdate dari {old_item_name} menjadi {new_item_name}')
        else:
            print('Item tidak terdapat di dalam list belanja.')

    #Function yang digunakan untuk meng-update jumlah item ke dalam dictionary yag sudah dibuat
    def update_item_qty(self):

        nama_item = input('Masukan item yang ingin diperbarui jumlahnya : ')
        if nama_item in self.item_awal:
            new_item_qty = int(input('Masukan jumlah baru : '))
            self.item_awal[nama_item][0] = new_item_qty
            print(f'Jumlah item untuk {nama_item} berhasil diperbarui. ')
        else:
            print('Item tidak ditemukan dalam list belanja.')

    #Function yang digunakan untuk meng-update harga item ke dalam dictionary yang dibuat
    def update_item_price(self):

          nama_item = input('Masukan item yang ingin diperbarui harganya :')
          if nama_item in self.item_awal:
              new_item_price = int(input('Masukan harga item : '))
              self.item_awal[nama_item][1] = new_item_price
              print(f'Harga item untuk {nama_item} berhasil diperbarui. ')
          else:
              print('Item tidak ditemukan dalam list belanja.')

    #Function yang digunakan untuk delete item
    def delete_item(self):

          nama_item = input('Masukan item yang mau dihapus : ')
          if nama_item in self.item_awal:
              del self.item_awal[nama_item]
              print(f'{nama_item} berhasil dihapus dari list belanja. ')
          else:
              print(f'Item tidak ditemukan dalam list belanja.')

    #Function yang digunakan untuk reset item
    def reset_transaction(self):
          reset = input('Anda yakin untuk menghapus transaksi (Y/N)? ')
          if reset == 'Y' or reset =='y':
              self.item_awal.clear()
              print('List belanja berhasil dihapus.')
          else:
              print('Hapus transaksi dibatalkan.')

    #Function yang digunakan untuk total payment
    def total_payment(self):
          sum_total = 0
          merged_data = [[key] + values for key, values in self.item_awal.items()]
          headers = ['Nama Item', 'Jumlah Item', 'Harga Item', 'Total Harga']
          print(tabulate(merged_data, headers, tablefmt = 'fancy_grid'))
          for key, values in self.item_awal.items():
              total_harga_bayar = values[0]*values[1]
              self.item_awal[key][2] = total_harga_bayar
              sum_total +=values[2]
          if sum_total == 0:
              print('Belum ada transaksi. ')
          elif sum_total <200000:
              print(f'Anda tidak mendapatkan diskon')
              print(f'Total belanja anda adalah {sum_total}')
          elif sum_total <300000:
              print(f'Total belanja sebelum diskon adalah {sum_total}')
              sum_total == 0.95*sum_total
              print(f'Selamat anda mendapat diskon 5%! ')
              print(f'Total belanja anda adalah {sum_total}')
          elif sum_total <500000:
              print(f'Total belanja sebelum diskon adalah {sum_total}')
              sum_total == 0.92*sum_total
              print(f'Selamat anda mendapat diskon 8%! ')
              print(f'Total belanja anda adalah {sum_total}')
          elif sum_total > 500000 or sum_total == 500000:
              print(f'Total belanja sebelum diskon adalah {sum_total}')
              sum_total == 0.9*sum_total
              print(f'Selamat anda mendapat diskon 10%! ')
              print(f'Total belanja anda adalah {sum_total}')

    #cek item untuk melihat list belanja
    def check_item(self):
        print(self.item_awal)
        merged_data = [[key] + values for key, values in self.item_awal.items()]
        print(merged_data)
        headers = ['Nama Item', 'Jumlah Item', 'Harga Item', 'Total Harga']
        print(tabulate(merged_data, headers, tablefmt = 'fancy_grid'))

