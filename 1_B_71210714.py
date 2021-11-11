n = input("Nama : ")
tampak = n.split()

m = str(input("Tempat tanggal lahir : "))
cetak = m.split()

kota = cetak[0]
tanggal = cetak[1],cetak[2],cetak[3]

if len(tampak) > 2 :
    print("Haloo! ", tampak[2] + ",", tampak[0] + " ", tampak[1])
else :
    print("Haloo! ", tampak[1] + ",", tampak[0])

print("Anda lahir di ", kota, "pada tanggal ", *tanggal)