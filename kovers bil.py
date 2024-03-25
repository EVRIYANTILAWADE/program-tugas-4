bilangan = int(input("Masukkan bilangan: "))

bil_oktal = oct(bilangan)[2:]
bil_hexa = hex(bilangan)[2:]
bil_desimal = bilangan
bil_biner = "{:08b}".format(bilangan)

print("Bilangan yang dimasukkan:", bilangan)
print("Bilangan biner:", bil_biner)
print("Bilangan oktal dari", bilangan, "adalah", bil_oktal)
print("Bilangan heksadesimal dari", bilangan, "adalah", bil_hexa)
print("Bilangan desimal dari", bilangan, "adalah", bil_desimal)

# Mengkuadratkan bilangan
bilangan_kuadrat = bil_desimal ** 2

# Membagi hasil kuadrat dengan 2
hasil_bagi = bilangan_kuadrat / 2

# Menghitung modulus hasil kuadrat dengan 2
hasil_modulus = bilangan_kuadrat % 2

print("Hasil kuadrat bilangan:", bilangan_kuadrat)
print("Hasil pembagian hasil kuadrat dengan 2:", hasil_bagi)
print("Modulus hasil kuadrat dengan 2:", hasil_modulus)