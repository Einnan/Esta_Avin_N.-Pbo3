#Python break di dalam perulangan for
nomor = int(input("Masukan nomor : "))
for i in range(1, 10):

    if i == nomor:
        break
    print(i)

#Python break di dalam perulangan while
while True:
    nomor = int(input("Masukan Nomor : "))
    if nomor < 0:
        break
    print(f"Kau memasukan nomor : {nomor}")

#Python contine di dalam perulangan for
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#Python penjumlahan hanya dengan menggunakan bilangan positif
total = 0

while True:
    nomor = int(input("Masukan nomor (0 untuk berhenti): "))

    if nomor < 0:
        continue

    if nomor == 0:
        break

    total += nomor

print(f"Penjumlahan bilangan positif : {total}")

#Python loop dengan else klaus
stok = ["baju","celana","topi"]

order = input("Masukan produk untuk dibeli : ")

for produk in stok:
    if produk == order:
        print(f"{order} masukan kedalam keranjang.")
        break
else:
    print(f"Maaf, {order} tidak ada di dalam stok.")