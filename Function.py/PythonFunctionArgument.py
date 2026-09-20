#Python function argument
def jml(a,b):
    hasil = a + b
    print(hasil)
jml(10,5)

#Python function dengan nilai bawaan
def tambah(a = 5, b = 4):
    jml = a + b
    print(jml)
tambah(2,3)
tambah(a = 2)
tambah()

#Python function kata kunci
def kata(nama1, nama2):
    print("Nama awal : ",nama1)
    print("Nama kedua : ", nama2)
kata("Avin", "Nirmawan")

#Python Function untuk nomor sembarang
def cari(*nmr):
    hasil = 0

    for nom in nmr:
        hasil = hasil + nom

        print("hasil : ", hasil)

cari(5,4,3)
cari(9,1)