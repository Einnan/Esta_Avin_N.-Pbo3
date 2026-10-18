from datetime import datetime

#Python datetime string menggunakan strftime()
sekarang = datetime.now()

tahun = sekarang.strftime("%Y")
print("Tahun :",tahun)

bulan = sekarang.strftime("%m")
print("Bulan :",bulan)

hari = sekarang.strftime("%d")
print("Hari :",hari)

waktu = sekarang.strftime("%H : %M : %S")
print("Pukul :",waktu)

TanggalWaktu = sekarang.strftime("%m : %d : %Y, %H : %M : %S")
print("Tanggal & Waktu :",TanggalWaktu)

#Python membuat string dari timestamp
stamp = 1787123208
tgl = datetime.fromtimestamp(stamp)

print("Objek tanggal dan waktu :", tgl)

t = tgl.strftime("%m : %d : %Y, %H : %M : %S")
print("Output 2 :", t)

t = tgl.strftime("%d  %b,  %Y")
print("Output 3 :", t)

t = tgl.strftime("%d  %B,  %Y")
print("Output 4 :", t)

t = tgl.strftime("%I%p")
print("Output 5 :", t)

#Python date Time yang sesuai dengan lokasi
ts = 1710454653
dt = datetime.fromtimestamp(ts)

y = dt.strftime("%c")
print("Output 1     :",y)

y = dt.strftime("%x")
print("Output 2     :",y)

y = dt.strftime("%X")
print("Output 3     :",y)