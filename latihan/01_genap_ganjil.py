# Input: bilangan bulat
# Proses: menentukan apakah bilangan genap atau ganjil
# Output: hasil genap atau ganjil

bilangan = int(input("Masukkan bilangan bulat: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")