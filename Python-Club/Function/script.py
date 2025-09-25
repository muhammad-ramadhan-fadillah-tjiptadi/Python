def sapa(nama):
    print(f"Halo {nama}, selamat belajar Python!")
sapa("Aisyah")
sapa("Budi")

# Dengan return
def tambah(a, b):
    return a + b
hasil = tambah(5, 7)
print(hasil) # Output: 12

# Study Case
def cari_nilai_tertinggi(data):
    tertinggi = data[0]
    for nilai in data:
        if nilai > tertinggi:
            tertinggi = nilai
    return tertinggi

angka = [18,15,16,13,12,17,11,14]
print(cari_nilai_tertinggi(angka))