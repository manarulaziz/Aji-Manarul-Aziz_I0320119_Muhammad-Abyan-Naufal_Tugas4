import time
start_time = time.time()

# Mendaftar kursus online

print("Selamat datang di pendaftaran Elektron Surakarta")
print("------------------------------------------------")

umur = int(input("Berapakah umur Anda: "))
print("Baik, umur Anda adalah ", umur, "tahun")

print("Apakah Anda lulus ujian kualifikasi? [Y/T]")
lulus = input().upper()
if lulus == "Y":
    print("Baik, tunggu sebentar")
else:
    print("Baik, tunggu sebentar")

syarat1 = umur >= 21
syarat2 = lulus == "Y"

hasil = syarat1 and syarat2

if hasil == True:
    print("\nAnda dapat mendaftar di kursus.")
else:
    print("\nAnda tidak dapat mendaftar di kursus.")
print("\n------------------------------------------------")
print("Terima kasih sudah berkunjung")

print("\nWaktu runtime adalah",time.time() - start_time, "detik")
