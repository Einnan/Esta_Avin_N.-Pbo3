#Python Function
def p ():
    print("hello world")

p()

print

#Python function argumen
def arg(nama):
    print("hello", nama)

arg("einnan")

#Python function operasi aritmatika
def nmr(nmr1, nmr2):
    jml = nmr1 + nmr2
    print("Hasil : ",jml)

nmr(4,5)

#Python function pengembalian statement sehingga nilai tetap bisa di jalankan tidak seperti print()
def cari(nmr):
    hasil = nmr*nmr
    return hasil

kotak = cari(3)
print("Kotak : ", kotak)

#Python function pass statement untuk mengosongkan nilai agar tidak error
def kosong():
    pass

kosong()

#Python function library contoh : (rumus matematika)
import math
    #sqrt untuk hasil akar
x = math.sqrt(4)
print("Akar dari 4 adalah : ",x)

    #pow untuk hasil pangakat
x = math.pow(4,5)
print("Hasil 4^5 adalah : ", x)