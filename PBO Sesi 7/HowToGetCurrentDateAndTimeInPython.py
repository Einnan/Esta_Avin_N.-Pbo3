from datetime import date

#Python mencetak tanggal hari ini
harini = date.today()
print("Sekarang Tanggal :",harini)

#Python mencetak tanggal saat ini namun dengan format yang berbeda
harini = date.today()

h1 = harini.strftime("%d/%m/%Y")
print("\nH1 :",h1)

h2 = harini.strftime("%B %d, %Y")
print("H2 :",h2)

h3 = harini.strftime("%m/%d/%y")
print("H3 :",h3)

h4 = harini.strftime("%b-%d-%Y")
print("H4 :",h4)

#Python mencetak tanggal dan waktu sekarang
from datetime import datetime
a = datetime.now()

print("\nSekarang :",a)

tglstring = a.strftime("%d/%m/%Y %H:%M:%S")
print("Tanggal dan Waktu :", tglstring)