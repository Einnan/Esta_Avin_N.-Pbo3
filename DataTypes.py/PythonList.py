#Python menciptakan list
keranjang = ["baju", "celana", "topi"]
print(keranjang)

listku = [1, "python", 3.6]
print(listku)

listku = []
print(listku)

#Python bisa konversi string menjadi list
vokal = "aiueo"

vokalist = list(vokal)
print(vokalist)

#Pyhton mengakses items dari daftar list
bahasa = ["Python", "C++", "JavaScript"]

print(f"bahasa urutan pertama : {bahasa[0]}")
print(f"bahasa urutan ketiga : {bahasa [2]}")
    #bisa di mulai dari indeks yang negatif
print(f"bahasa -1 : {bahasa[-1]}")
print(f"bahasa -3 : {bahasa[-3]}")

#Python memperbarui dan menambahkan item list
keranjang = ["tomat", "wortel", "bayam"]
favitem = ["susu", "daging", "creatine"]

keranjang[1] = "Sawi" #< memperbarui/mengubah
print(keranjang)

keranjang.append("Terong") #< menambahkan
print(keranjang)

keranjang.extend(favitem) #< menggabungkan
print(keranjang)

#Python menghapus item list
kranjang = ["cpu", "ram", "keyboard", "monitor"]

kranjang.remove("ram") #< menghapus item dari nama variable
kranjang.pop() #< menghapus item dari indeks, jika indeks tidak di tulis maka item/indeks terakhir yang di hapus
print(kranjang)

#del kranjang < untuk menghapus semua item dari list
#print(kranjang)

#Python menyalin item pada list
favitem = ["sepatu", "kaos kaki", "kacamata", "kalung"]
pesan = favitem #.copy() < hilangkan # dan teks ini agar variable pesan dan favitem tidak sama nilainya

favitem.append("gelang")
print(f"favorit item : {favitem}")
print(f"pesan : {pesan}")

#Python Fungsi len
item = ["tws", "airpods", "headset"]

jumlah = len(item)
print(jumlah)

#Python test anggota dari list dengan nilai boolean 
hasil = "tws" in item
print(hasil)

hasil = "headphone" in item
print(hasil)

#Python perulangan menggunakan list
for i in item:
    print(i)