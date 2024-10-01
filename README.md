# Mini-Project-1
Nama: Indah Maramin Al Inayah Nim: 2409116086

Coding

![Screenshot 2024-10-01 004412](https://github.com/user-attachments/assets/5da77e9b-f103-4943-9365-433dbcc81b06)
![Screenshot 2024-10-01 002426](https://github.com/user-attachments/assets/b97deb38-1fe1-47da-bac4-feac5dcca6a1)
![Screenshot 2024-10-01 004330](https://github.com/user-attachments/assets/0d1a08ff-5d18-4cc8-a119-1e8caac92f73)

[Upload
    
    print("_____________________________")
    print("Nama: Indah Maramin Al Inayah")
    print("_______Nim: 2409116086_______")
    print("_____________________________")

    # input nama dan nim
    while True:
    print("Selamat Datang")
    Nama = input("Masukkan Nama: ")
    Nim = input("Masukkan Nim: ")
    if Nama == "Naya" and Nim == "2409116086": 
        print("Selamat Datang, ",Nama,"Dengan Nim",Nim)
        break
    else:
        print("Maaf Nama dan Nim salah")
        
    # input harga dan jumlah
    while True:
    Harga = int(input("Masukkan harga barang : Rp. "))
    Jumlah = int(input("Masukkan jumlah barang"))
    
    if Harga == 0:
        print("Program Selesai")
        break
    
    total = Harga * Jumlah
    kondisi = 250000
    
    #  Percabangan menentukan apakah total harga lebih dari Rp. 250.000 untuk diskon
    if total > 250000:
        Harga = total - (0.25 * total)
        print("Selamat anda mendapatkan diskon")
        print("Total harga adalah: Rp. ", Harga)
        
    else:
        print("Total harga adalah Rp. ",total)
        print("Anda tidak mendapatkan diskon")
        
    # Perulangan untuk user yang ingin menghitung totalnya kembali
    ulang = input("Apakah anda ingin menghitung total lagi? (ya/tidak): ")
    if ulang != 'ya': 
        print("Terimakasih telah menggunakan program ini. Sampai Jumpa!")
        breaking mini project 1.py…]()


Flowchart

![Screenshot 2024-10-01 004958](https://github.com/user-attachments/assets/00df4a0c-6c88-42c9-a231-53431eca632e) 

Mulai: Program dimulai.

Input Nama dan Nim: Pengguna memasukkan nama dan nim

Nama= Naya, Nim= 2409116086: Pengguna memasukkan nama dan nim

Jika Ya: Lanjut ke Input harga dan jumlah barang

Jila Tidak: Menampilkan "Maaf Nama dan Nim salah" dan mengulang untuk Input nama dan nim 

Input harga dan jumlah: Pengguna memasukkan harga dan jumlah barang lalu menhitung total = harga * jumlah 

Total > Rp. 250.000 untuk medapatkan diskon dengan harga = total - (0.25 * total)

Jika Ya: Pengguna mendapatkan diskon 25%

Jika Tidak: Pengguna tidak mendapatkan diskon

Tanya apakah ingin menghitung total harga lagi: Program memberikan pilihan kepada pengguna

Jika Ya: Kembali ke langkah input barang

Jika Tidak: Program selesai

Selesai: Program berakhir jika pengguna memilih tidak menghitung total harga lagi.
Jika Ya: 
