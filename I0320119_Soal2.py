print("Selamat Datang di Konter Pengecekan Maskapai Air Solo")
print("-----------------------------------------------------")

berat_bagasi = float(input("Beban bagasi Anda : "))

lbs = 50
kg = lbs * 0.45
max_berat = kg

if berat_bagasi < max_berat:
    print("Bagasi Anda dapat dibawa ke pesawat")
else:
    print("Mohon maaf bagasi Anda tidak dapat dibawa ke pesawat. Silahkan bayar biaya tambahan bagasi")

