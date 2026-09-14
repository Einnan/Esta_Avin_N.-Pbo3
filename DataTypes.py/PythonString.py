#Python multistring
pesan = ''' hai nama saya avin
senang bertemu dengan kamu
'''
print(pesan)

#Python akses string karakter
model = "claude"

print(model[0])
print(model[3])

#Pyton string tidak bisa diubah karakternya tapi bisa di gabungkan dengan karakter string lain
nama = "einnan"
akhir = "smith"
nama = nama + " " + akhir
print(nama)

#Python string method
teks = "Python itu hebat"

teksbaru = teks.replace("Python", "C++")
print(teksbaru)
    #test keanggotaan karakter
print("on" in "python")

#Python iterasi dengan string
buah = "semangka"
for i in buah:
    print(i)

#Python panjang string
buah = "Jeruk"
print(len(buah))

#Python string pada tanda ""
contoh = "dia berkata, \"apakabar\""
print(contoh)
contoh = "dia berkata, 'apa yang terjadi'"
print(contoh)

#Python f{string}
hobi = "Basket"
kota = "Jombang"

print(f"aku suka bermain {hobi} di kota {kota}")