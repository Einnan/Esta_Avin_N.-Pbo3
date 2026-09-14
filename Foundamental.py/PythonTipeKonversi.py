#Python konversi integer (bilangan bulat) ke float (bilangan pecahan) secara implisit
bilbul = 36
bilpe = 3.6

hasil = bilbul + bilpe

print("Nilai : ", hasil)
print("Tipe Data : ", type(hasil))

#Python punya tipe data explisit
int()
str()
float()

nmrstr = "3"
nmrint = 6

    #konversi dari string ke integer
nmrstr = int(nmrstr)
print("Tipe data nmrstr setelah di konversi : ", type(nmrstr))

nmrjml = nmrstr + nmrint

print("hasil : ", nmrjml)
print("Tipe data nilai baru : ", type(nmrjml))