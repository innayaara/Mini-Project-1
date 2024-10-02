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
        break