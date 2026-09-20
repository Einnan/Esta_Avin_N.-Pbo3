#Python local variable (tidak bisa di deklarasikan  diluar fungsi)
def halo():
    pesan = "Halo gais"
    print("Pesan : ",pesan)
halo()
#Print(pesan) < tidak bisa dan akan error karena variable "pesan" berada dalam fungsi halo()

#Python Global Variable (bisa di deklarasikan diluar maupun didalam fungsi)
pesan = "halo"

def coba():
    print("Lokal", pesan)

coba()
print("Global", pesan)

#Python NonLocal variable
def luar():
    pesan = "lokal"

    def dalam():
        nonlocal pesan

        pesan = "nonlocal"
        print("Dalam : ", pesan)

    dalam()
    print("Luar : ", pesan)

luar()