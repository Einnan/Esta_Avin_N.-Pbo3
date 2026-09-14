#Python boolean operator perbandingan
x = int(input("Masukan X : "))
y = int(input("Masukan y : "))

result = (x > y)
print(f"x > y : {result}")

result = (x < y)
print(f"x < y : {result}")

result = (x >= y)
print(f"x >= y : {result}")

result = (x <= y)
print(f"x <= y : {result}")

result = (x == 10)
print(f"x == 10 : {result}")

result = (y != 10)
print(f"y != 10 : {result}")

#Python boolean operator perbandingan untuk string
nama = "sofia"
print(nama == "Sofia")
print(nama == "sofia")
print(nama != "Sofia")
print(nama != "sofia")

#Python operator and untuk menyatakan true jika semua kondisi terpenuhi
umur = int(input("Masukan umur anda : "))
kota = input("Kota Jombang (y/n) : ")
result = (umur >= 18) and (kota == "y")
print(result)

#Python operator or untuk menyatakan true jika salah satu kondisi terpenuhi
umur = int(input("Masukan umur anda : "))
kota = input("Kota Jombang (y/n) : ")
result = (umur >= 18) or (kota == "y")
print(result)

#Python operator not untuk menyatakan true jika semua kondisi tidak terpenuhi
code = "1105"
masukan = input("Masukan kode : ")

hasil = (code == masukan)
print(f"Apakah kode yang dimasukan benar : {hasil}")

hasil = (code != masukan)
print(f"Apakah kode yang dimasukan salah : {hasil}")

#Python fungsi bool() untuk memvalidasi nilai jika int 0 itu false dan string "" adalah false
print(bool(0))

print(bool(12))

print(bool("Python"))
print(bool("False"))  

print(bool(""))