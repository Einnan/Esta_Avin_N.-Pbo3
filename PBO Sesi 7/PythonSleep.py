import time

#Python contoh time sleep atau delay 
time.sleep(2)
print("Tunggu sampai 2 detik...")

#Python membuat jam digital 
while True:
    ct = time.localtime()
    formatt = time.strftime("%I:%M:%S:%p", ct)

    print(formatt)
    time.sleep(1)