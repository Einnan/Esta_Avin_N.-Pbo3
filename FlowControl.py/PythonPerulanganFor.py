#Python perulangan for syntax
model = ["gemini", "claude", "deepsek"]

for ai in model:
    print(ai)
    print("====")

#Python perulangan identitas
nomor = [1,2,3]

for nmr in nomor:
    print(f"Proses : {nmr}")
    print(f"Proses Selesai : {nmr}")

#Python perulangan range
value = range(1,5)

for i in range (1, 11):
    print(f"Menampilkan produk {i}")

#Python perulangan untuk string
x = "Ambatukam"

for y in x:
    print(x)

#Python break pada perulangan 
for nmr in range(1, 11):
    if nmr == 3:
        break
    print(nmr)

#Python continue pada perulangan
for nmr in range(1, 11):
    if nmr == 3:
     continue
    print(nmr)

#Python perulangan for menggunakan else
stock = ["Laptop", "Handphone", "Tablet"]

req = input("Masukan barang : ")

for i in stock:
    if i == req:
        print(f"{req} tersedia")
        break
    else:
        print(f"{req} tidak tersedia")

#Python perulangan tanpa items
for _ in range(1,4):
    print("halo")

#Python perulangan untuk penjumlahan
total = 0

for i in range(0,6):
    total += i
print(f"total : {total}")

#Python penumpukan perulangan
attribut = ['Electric', 'Fast']
mobil = ['Tesla', 'Porsche', 'Mercedes']

for attribute in attribut:
    for mbl in mobil:
        print(attribute, mbl)
    
    print("-----")