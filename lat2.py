# state
nama =     input("masukan nama     : ")
golongan = input("masukan golongan : ")
jabatan =  input("masukan jabatan  : ")
status =   input("masukan status   : ")

# keluarga
jumlah_anak =      int(input("jumlah anak      : "))
jumlah_jam_kerja = int(input("jumlah jam kerja : "))

# ketentuan
# jam kerja normal 48 jam

upah = 0
upah_lembur = 3000
tunjangan_A = 300000
tunjangan_B = 400000
tunjangan_C = 500000
tunjangan_kawin = 250000
tunjangan_anak1 = 250000
tunjangan_anak2 = 500000  

if golongan == "A" or golongan == "a":
    if jumlah_jam_kerja >= 48:
        upah += (1000 * jumlah_jam_kerja) + upah_lembur
    else:
        upah += 1000 * jumlah_jam_kerja
elif golongan == "B" or golongan == "b":
    if jumlah_jam_kerja >= 48:
        upah += (15000 * jumlah_jam_kerja) + upah_lembur
    else:
        upah += 1000 * jumlah_jam_kerja
elif golongan ==  "C" or golongan == "c":
    if jumlah_jam_kerja >= 48:
        upah += (20000 * jumlah_jam_kerja) + upah_lembur
    else:
        upah += 1000 * jumlah_jam_kerja
elif golongan == "D" or golongan == "d":
    upah += 25000 * jumlah_jam_kerja
else:
    print("tidak sesuai dengan ketentuan")

print(f"upah : {upah}")


def dsiplay(nama, golongan, jabatan, jumlah_anak, jumlah_jam_kerja):
    print("nama             : " + nama)
    print("golongan         : " + golongan)
    print("status           : " + jabatan)
    print("jumlah anak      : " + str(jumlah_anak))
    print("jumlah jam kerja : " + str(jumlah_jam_kerja) + " jam")




