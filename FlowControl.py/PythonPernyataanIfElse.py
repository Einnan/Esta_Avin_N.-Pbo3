#Python if statement
umur = int(input("Masukan umur : "))

if umur >= 18:
    print("Verifikasi telah berhasil")

#Python if else statement
umur = int(input("Masukan umur : "))

if umur >= 18:
    print("Kamu sudah layak umur")

else:
    print("Kamu belum layak umur")

#Python untuk autentikasi password
userdb = "admin"
passworddb = "einnan36"

user = input("Masukan Nama : ")
password  = input("Masukan Password : ")

if (user == userdb) and (passworddb == password):
    print("Hi, Selamat Datang")
else:
    print("Login Gagal.")

#Python if elif else statement
umur = input("Masukan umur anda : ")

if umur < 0:
    print("Umur Tidak Valid")
elif umur >= 18:
    print("Umur kamu sudah legal")
else:
    print("Umur kamu belum legal")

#Python nested if (if bertumpuk)
age = int(input("Masukan umur anda : "))

if age < 18:

    if age < 0:
        print("Umur tidak valid.")
    else:
        print("Akses ditolak.")
else:
    print("Akses disetujui.")

#Python statement pendek
age = 22
status = "dewasa" if age >= 18 else "Minor"
print(status)

#Python dengan 3 nomor besar
n1 = float(input("Masukan nomor ke-1: "))
n2 = float(input("Masukan nomor ke-2: "))
n3 = float(input("Masukan nomor ke-3: "))

if n1 >= n2 and n1 >= n3:
    largest = n1
elif n2 >= n1 and n2 >= n3:
    largest = n2
else:
    largest = n3

print("Nomor terbesarnya adalah : ", largest)
