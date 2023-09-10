# Python Project-Pacmann - Super Cashier

**LATAR BELAKANG MASALAH**

Andi adalah pemilik supermarket besar di salah satu kota di indonesia memiliki rencana untuk mempercepat proses bisnis dengan membuat sistem kasir self service untuk customer yang datang ke supermarketnya. Sehingga customer bisa melakukan self service untuk transaksi yang dilakukan. Oleh karena itu, Andi meminta temannya yang merupakan seorang programmer untuk membuat program cashier self service.

**OBJECTIVES DAN REQUIREMENTS**

Tujuan dari pembuatan program ini adalah untuk memudahkan customer dan juga pemilik supermarket dalam transaksi pembelian.
List requirements untuk membuat program super cashier ini adalah membuat fitur-fitur antara lain sebagai berikut:
1. Fitur penambahan item
2. Fitur update nama item
3. Fitur update jumlah item
4. Fitur update harga item
5. Fitur delete item
6. Fitur reset transaksi
7. Fitur check order
8. Fitur menu pembayaran

**FLOWCHART**

Berikut merupakan flow customer journey pada saat berbelanja di supermarket Andi.
<img width="1262" alt="flow" src="https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/62a94fa4-eb29-4d9d-95d9-6215ce7db166">


**MODULES AND FUNCTION DESCRIPTION**

1. **Class Transaction**
   Membuat Class untuk menampung transaksi-transaksi yang diinput customer
   ![Customer ID](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/34f958d3-4b10-4063-b739-14a7b82a5e62)

2. **Fitur Add Item**
   Merupakan fitur yang digunakan customer untuk add semua item yang mau dibeli dengan detail:
   - nama item
   - jumlah item
   - harga item
![add item](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/fb339efc-1c9d-4ee8-b0ca-79d7dc57e28e)

3. **Fitur Update Nama Item**
   Fitur yang digunakan untuk update nama item apabila dari customer mau melakukan perubahan nama.
   ![Update Nama Item](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/7f016e4b-637b-4b38-b410-d3c464748ea6)

4. **Fitur Update Harga Item**
   Fitur yang digunakan untuk update harga item apabila dari customer mau melakukan perubahan harga.
   ![Update harga item](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/05abd664-bafb-4c98-b787-981e8439c371)

5. **Fitur Delete Item**
   Fitur yang digunakan untuk delete item apabila ada item yang tidak jadi dibeli.
   ![delete item](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/e2609153-7bed-4609-b316-1b9fa69b9f61)

6. **Fitur Reset Transaksi **
   Fitur yang digunakan untuk menghapus semua transaksi jika customer mau melakukan input ulang.
   ![reset transaction](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/cb50d0b5-2a3a-45c6-a3d4-defbc5563e00)

7. **Fitur Check Item**
   Fitur yang digunakan untuk melihat list belanja customer.
   ![Check item](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/17019625-ab28-4793-b87b-cc17e583ad26)

8. **Fitur Total Payment**
   Fitur yang digunakan untuk melihat total yang harus dibayar customer. Fitur ini juga membantu dalam perhitungan diskon yang didapatkan oleh customer.
   ![Total Payment](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/31276612-3eee-4796-9fcc-1d11ccd2897c)

**TEST CASE**
1. Test Case 1:
   Customer ingin menambahkan dua item baru.
   - Nama Item : Ayam Goreng, Qty : 2, Harga : 20000
   - Nama Item : Pasta Gigi, Qty : 3, Harga : 15000
   Result : As Expected
![Test1](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/702ffcc0-88e8-4f10-818b-65d9ddc22be8)

2. Test Case 2:
   Customer ingin menghapus pasta gigi dari list belanja.
   Result: As Expected
   ![test2](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/6c0b06da-7496-44d8-bdc8-e795779992ab)

3. Test Case 3:
   Customer ingin melakukan reset transaction untuk semua list belanja.
  Result : As Expected
![test 3](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/1cf39755-5122-4df7-b8eb-7458a8dac073)

4. Test Case 4:
   Customer meng-input lagi keseluruhan belanja.
   Di sini dapat kita lihat bahwa method ini dapat menghitung total beserta diskonnya.
![test4](https://github.com/beabea009009zz/Python-Project-Pacmann---Super-Cashier-/assets/130691185/fdb7f740-e639-4695-a40a-900687265c65)

**CONCLUSION and SUGGESTION**
Mesin Cashier ini tentunya sangat membantu dalam operasional supermarket ke depannya. Dilihat dari keefektifan customer dalam menginput dan mengatur transaksinya sendiri.

Untuk ke depannya program ini bisa dikembangkan lagi untuk beberapa fitur. Seperti detail harga-harga sudah tidak perlu lagi diinput oleh customer.

