import datetime

#Python tanggal dan waktu saat ini
print("Get Current Date and Time")
sekarang = datetime.datetime.now()
print(sekarang)

#Python hanya tanggal saat ini juga
print("\nGet Current Date")
tanggal = datetime.date.today()
print(tanggal)

#Python menampilkan attribut modul dengan fungction dir()
print("\nAttributes of datetime Module")
print(dir(datetime))

#Python object tanggal untuk mempresentasikan tanggal
print("Date object to represent a date")
x = datetime.date(2026, 3, 11)
print(x)
    #atau hanya dengan impor tanggal kelas saja
from datetime import date 

x = date(2026, 3, 11)
print(x)

#Python tanggal saat ini dengan menggunakan today()
print("\nGet the current date using today()")
tgl = date.today()
print("Sekarang Tanggal = ",tgl)

#Python tanggal dari timestamp Titik awal 1 Januari 1970 unix epoch
timestamp = date.fromtimestamp(1778341426)
print(timestamp)

#Python cetak tahun, bulan, hari ini dengan satu persatu
harini = date.today()

print("Tahun ini : ", harini.year)
print("Bulan ini : ", harini.month)
print("Hari ini : ", harini.day)

#Python kelas datetime.time
from datetime import time

x = time()
print(x)

y = time(10, 30, 10)
print(y)

z = time(hour = 5, minute = 4, second = 12)
print(z)

q = time(5, 23, 55, 895222)
print(q)

#Python jam, menit, detik dan detik mikro
p = time(8, 30, 20)

print("Jam        :",p.hour)
print("Menit      :",p.minute)
print("Detik      :",p.second)
print("DetikMikro :",p.microsecond)

#Python Objek datetime
from datetime import datetime
a = datetime(2026, 3, 11)
print(a)

b = datetime(2026, 3, 11, 20, 30, 40, 378256)
print(b)

#Python print tahun, bulan, jam, menit, detik dan timestamp
l = datetime(2026, 3, 11, 20, 30, 40, 378256)
print("Tahun        :",l.year)
print("Bulan        :",l.month)
print("Jam          :",l.hour)
print("Menit        :",l.minute)
print("Timestamp    :",l.timestamp())

#Python datetime.timedelta
from datetime import datetime, date
a1 = date(year = 2006, month = 3, day = 11)
a2 = date(year = 2012, month = 7, day = 12)

a3 = a1 - a2
print(a3)

a4 = datetime(year = 2026, month = 3, day = 11, hour = 6, minute = 1, second = 30)
a5 = datetime(year = 2006, month = 3, day = 11, hour = 6, minute = 1, second = 30)
a6 = a4 - a5
print(a6)

print("Tipe dari a4 :",type(a4))
print("Tipe dari a5 :",type(a5))

#Python perbedaan antara 2 objek timedelta  
from datetime import timedelta
b1 = timedelta(weeks = 1, days = 3, hours = 5, seconds = 7)
b2 = timedelta(weeks = 2, days = 4, hours = 6, seconds = 8)
b3 = b1 - b2
print(b3)

#Python durasi time di detik
t = timedelta(days = 3, hours = 2, seconds =  44, microseconds = 122466)
print("Total Detik :",t.total_seconds())

#Python strftime() Method
k = datetime.now()

v = k.strftime("%H:%M:%S")
print("Time :",v)

n1 = k.strftime("%m/%d/%Y, %H:%M:%S")
print(n1)

n2 = k.strftime("%d/%m/%Y, %H:%M:%S")
print(n2)

#Python strptime() method
ds = "13 october, 2026"
print("Tanggal String =",ds)

do = datetime.strptime(ds, "%d %B, %Y")
print("Objek Tanggal =",do)

#Python menangani timezone
import pytz

lokal = datetime.now()
print("Lokal:", lokal.strftime("%m/%d/%Y, %H:%M:%S"))


Jakarta = pytz.timezone('Asia/Jakarta') 
datetime_Jakarta = datetime.now(Jakarta)
print("Waktu Jakarta :", datetime_Jakarta.strftime("%d/%m/%Y, %H:%M:%S"))

Mesir = pytz.timezone('Africa/Cairo')
datetime_Mesir = datetime.now(Mesir)
print("Waktu Mesir :", datetime_Mesir.strftime("%m/%d/%Y, %H:%M:%S"))