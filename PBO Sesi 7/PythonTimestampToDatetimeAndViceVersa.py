from datetime import datetime

#Python timestamp ke datetime
ts = 1800000000

dto = datetime.fromtimestamp(ts)
print("Objek tanggal dan waktu :",dto)
print("Tipe Datanya            :",type(dto))

#Python datetime ke timestamp
x = datetime.now()

ts = datetime.timestamp(x)
print("Timestamp               :",ts)