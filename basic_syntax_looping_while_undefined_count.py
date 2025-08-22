"""
Program Perulangan Dengan "While" undefined count
"""

# Dengan 'While'
print("Dengan WHILE")
jumlah_buku = 10
print('Perintah ibu, "Baca bukumu"')

buku_dibaca_dan_dipahami = 0
print(f"Jumlah buku yang sudah dibaca & dipahami {buku_dibaca_dan_dipahami} buku")

while buku_dibaca_dan_dipahami < jumlah_buku:
    if buku_dibaca_dan_dipahami == 9:
        print(f"Buku ke - {buku_dibaca_dan_dipahami + 1} belum paham")
    else:
        buku_dibaca_dan_dipahami += 1
        print(f"Buku ke - {buku_dibaca_dan_dipahami} dibaca & dipahami")

print(f"Jumlah buku yang sudah dibaca & dipahami adalah {buku_dibaca_dan_dipahami}")
