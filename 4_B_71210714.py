print("=====GEBYAR DISKON=====")
print("=====MASUKKAN JUMLAH BARANG YANG DIPESAN=====")

barang1 = int(input("KIPAS ANGIN DISKON 10%\tRp 25.000,00\t: "))
barang2 = int(input("SEPEDA DISKON 55%\tRp 6.000,00\t: "))
barang3 = int(input("HELM ROSSI DISKON 77%\tRp 8.000,00\t: "))

rumus1 = barang1 * (25000 * 10/100)
rumus2 = barang2 * (6000 * 55/100)
rumus3 = barang3 * (8000 * 77/100)
jumlah = rumus1 + rumus2 + rumus3

print("=====TOTAL=====")
print("TOTAL KIPAS ANGIN\t: ", rumus1)
print("TOTAL SEPEDA SUPER\t: ", rumus2)
print("TOTAL HELM ROSSI\t: ", rumus3)
print("Jumlah total diskon yang didapat adalah ", jumlah)