#Pyhton perulangan while
nomor = float(input("Masukan nomor : "))

while nomor >= 0.0:
    print(nomor)
#Jika tanpa kode dibawah maka akan jadi infinite loop
    nomor = float(input("Nomor lain : "))

#Python identation
tugas = input("Tugas : ")

while tugas != "q":
    print("Tugas Selesai!!")
    tugas = input("Tugas : ")

print("semua tugas Selesai")

#Python perulanan while dari 1 ke n
n = 10
i = 1

while i <= n:
    print(i)
    i+=1

#Python perulangan penjumlahan sampai user input angka 0
total = 0
n = float(input("Masukan nomor (0 untuk berhenti): "))

while n != 0.0:
    total += n
    n = float(input("Masukan nomor (0 untuk berhenti): "))

print(f"Hasil : {total}")

#Python break dan continue statement
while True:
    nomor = int(input("Masukan Nomor : "))
    if nomor == 0:
        break
    print(nomor)

    i = 0
    #continue statement ↓↓↓↓↓↓↓↓↓↓
while i <= 10:
    i += 1
    
    if i % 2 != 0:
        continue

    print(i)

#Python perulangan dengan else klaus
percobaan = 3

while percobaan > 0:
    pin = input("Masukan PIN : ")

    if pin == "3636":
        print("Akses diterima.")
        break

    percobaan -= 1
    print(f"PIN salah. {percobaan} coba lagi.")
else:
    print("Akun dikunci. terlalu banyak percobaan")