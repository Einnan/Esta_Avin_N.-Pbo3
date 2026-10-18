from datetime import datetime 

#Python string ke objek date & time
ds = "11 march, 2006"

print("String Tanggal   :", ds)
print("Tipe Datanya     :",type(ds))

do = datetime.strptime(ds, "%d %B, %Y")

print("Objek Data   :",do)
print("Tipe Datanya :", type(do))

#Python string ke objek date & time 2
dts = "11/03/2006 08:30:00"

dto1 = datetime.strptime(dts, "%d/%m/%Y %H:%M:%S")
print("Tanggal dan Waktu objek 1    :", dto1)

dto2 = datetime.strptime(dts, "%m/%d/%Y %H:%M:%S")
print("Tanggal dan Waktu objek 1    :", dto2)

#Python value error di strptime()
# datestring = "03/06/2023"
# dateobject = datetime.strptime(datestring, "%d %m %Y")

# print("Objek Data :",dateobject)