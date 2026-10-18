import time

#Python time.time() Function
detik = time.time()
print("Detik sejak Epoch    :",detik)

#Python time.ctime() Function
detik = 1800000000.5000000
lokal = time.ctime(detik)
print("\nWaktu Lokal  :",lokal)

#Python time.sleep() Function
print("Tampilan akan delay selama beberapa waktu")
time.sleep(2.0)
print("Tampilan mucul setelah 2 detik")

#Python time.localtime() Function
hasil = time.localtime(1700000000)
print("Hasil    :",hasil)
print("Tahun    :",hasil.tm_year)
print("Jam TM   :",hasil.tm_hour)

#Python time.gmtime() Function
hasil = time.gmtime(1789999999)
print("Hasil    :",hasil)
print("Tahun    :",hasil.tm_year)
print("Jam TM   :",hasil.tm_hour)

#Python time.mktime() Function
ttuple = (2026, 10, 14, 5, 33, 3, 3, 362, 0)
detik = time.mktime(ttuple)
print(detik)

#Pytho time.asctime Function
t = (2020, 5, 1, 6, 0, 0, 1, 362, 0)

hasil = time.asctime(t)
print("Hasilnya :", hasil)

#Python time.strftime Function
namat = time.localtime()
wstring = time.strftime("%m/%d/%Y, %H:%M:%S", namat)
print(wstring)

#Python time.strptime() Function
tstring = "02 February, 2024"
hasil = time.strptime(tstring, "%d %B, %Y")
print(hasil)