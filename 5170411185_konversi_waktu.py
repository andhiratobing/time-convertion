# 517041185
# ANDHI RATOBING

# Library time saya gunakan untuk melihat waktu,
# kalau menggunakan datetime terlalu lengkap karena terdapat tahun,bulan,hari juga
import time

# kondisi untuk input pertanyaan dengan masukkan inputan harus Kapital "Y" agar masuk ke sistem
pilihBool = "Y"

# perulangan
while pilihBool == "Y":
    # inputan
    inputDetik = int(input("Masukkan jumlah detik yang ingin konversi: "))
    # kondisi untuk mengonversi inputan menjadi format time
    konversi = time.gmtime(inputDetik)

    # pernyataan untk hasil jam berdasarkan konversi detik ke jam
    jam = time.strftime("%H jam", konversi)

    # pernyataan untk hasil jam berdasarkan konversi detik ke menit
    menit = time.strftime("%M menit", konversi)

    # pernyataan untk hasil jam berdasarkan konversi detik ke detik
    detik = time.strftime("%S detik", konversi)

    # perintah untuk mencetak konversi jam,menit,detik berdasarkan inputan
    print("Konversi detik ke jam bernilai: ", jam)
    print("Konversi detik ke menit bernilai: ", menit)
    print("Konversi detik ke detik bernilai: ", detik)

    # pertanyaan mau mengulangi inputan lagi atau tidak
    pilihBool = (str(input("Apakah ingin melakukan konversi lagi ? (Y/T): ")))

    # kondisi jika pertanyaan di jawab "T"
    if pilihBool == "T":
        exit()

else:
    # kondisi jika pertanyaan di jawab selain "Y" dan "T"
    print("Jawaban anda salah, anda harus keluar dari sistem")
    exit()
