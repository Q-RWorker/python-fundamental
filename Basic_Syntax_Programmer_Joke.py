
# Sekuensial / Sequential
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli 1 botol susu"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan / Branching
jumlah_botol_susu = 173
jumlah_telur = 1587

print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 butir telur dan 1 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")
print("Budi pulang kerumah")
print("Menyampaikan hasilnya kepada Ibu")