"""
Program Perulangan Dengan "While"
"""

# Dengan 'While'

jumlah_buku = 10
print('Perintah ibu, "Baca bukumu"')

buku_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {buku_dibaca} buku")

while buku_dibaca < jumlah_buku:
    buku_dibaca += 1
    print(f"Baca buku ke - {buku_dibaca} dibaca")

print(f"Jumlah buku yang sudah dibaca adalah {buku_dibaca}")
