from datetime import datetime

#Python waktu sekarang menggunakan objek date & time
sekarang = datetime.now()

ct = sekarang.strftime("%H:%M:%S")
print("Waktu Sekarang   :",ct)

#Python waktu sekarang menggunakakn modul 
import time
t = time.localtime()
ct = time.strftime("%H:%M:%S", t)
print("\nWaktu Sekarang   :",ct)

#Python waktu saat ini dengan menggunakan zona tertentu dengan format timezone IANA
from datetime import datetime
import pytz

shanghai = pytz.timezone("Asia/Shanghai")
dtshanghai = datetime.now(shanghai)
print("Waktu China :",dtshanghai)

pontianak = pytz.timezone("Asia/Pontianak")
dtpontianak = datetime.now(pontianak)
print("Waktu IKN :",dtpontianak)