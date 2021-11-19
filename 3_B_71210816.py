Bil1 = int(input("Masukkan bilangan pertama: "))
Bil2 = int(input("Masukkan bilangan kedua: "))
Kalimat = input("Masukkan Kalimat: ")
kali = 'kali'
bagi = 'bagi'
tambah = 'tambah'
kurang = 'urang'

if kali in Kalimat:
    print ("Hasil Perkalian", Bil1 ,"dengan", Bil2, "adalah", Bil1*Bil2)
elif bagi in Kalimat:
    print ("Hasil Pembagian", Bil1 ,"dengan", Bil2, "adalah", Bil1/Bil2)
elif tambah in Kalimat:
    print ("Hasil Penjumlahan", Bil1 ,"dengan", Bil2, "adalah", Bil1+Bil2)
elif kurang in Kalimat:
    print ("Hasil Pengurangan", Bil1 ,"dengan", Bil2, "adalah", Bil1-Bil2)
else:
    print ("error")
