"""
Program Perulangan Dengan "While" undefined count with stop point
"""

# Dengan 'While'
print("Dengan WHILE")
jumlah_buku = 10
print('Perintah ibu, "Baca bukumu"')

total_baca = 0
buku_dibaca_dan_dipahami = 0
print(f"Jumlah buku yang sudah dibaca & dipahami {buku_dibaca_dan_dipahami} buku")

while total_baca < jumlah_buku * 2:
    total_baca += 1
    if buku_dibaca_dan_dipahami == 9:
        print(f"Buku ke - {buku_dibaca_dan_dipahami + 1} belum paham")
    else:
        buku_dibaca_dan_dipahami += 1
        print(f"Buku ke - {buku_dibaca_dan_dipahami} dibaca & dipahami")

print(f"Jumlah buku yang sudah dibaca & dipahami adalah {buku_dibaca_dan_dipahami}")

if buku_dibaca_dan_dipahami == jumlah_buku:
    print('Budi berkata, "Bu, semua buku sudah dibaca & dipahami"')
else:
    print(f'Budi berkata, "Bu, '
          f'saya hanya bisa memahami {buku_dibaca_dan_dipahami} buku" ')
