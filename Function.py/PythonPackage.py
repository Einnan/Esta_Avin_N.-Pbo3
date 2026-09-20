#Python Package
import math
from math import sqrt, pi

angka = 25

print("Nilai pi       :", math.pi)
print("Akar dari 25   :", math.sqrt(angka))

print("Akar dari 36   :", sqrt(36))
print("Nilai pi       :", pi)

print("Pembulatan 3.7  :", math.floor(3.7))
print("Pembulatan 3.7  :", math.ceil(3.7))
print("Pangkat 2^4     :", math.pow(2, 4))

def luas_lingkaran(r):
    return pi * r * r

jari_jari = 7

print("Luas lingkaran  :", luas_lingkaran(jari_jari))