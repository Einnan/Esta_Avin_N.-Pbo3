#Python tipe data nomor
nmr1 = 36
print(f"tipe data dari nmr1 adalah {type(nmr1)}")

nmr2 = 3.6
print(f"tipe data dari nmr2 adalah {type(nmr2)}")

nmr3 = 36j
print(f"tipe data dari nmr3 adalah {type(nmr3)}")

#Python sistem bilangan
print(0b1101011)  #< Bilangan Binary

print(0xFB + 0b10) #< Bilangan Octal

print(0o15) #< Bilangan Hexadecimal

#Python tipe konversi
num1 = int(2.3)
print(num1) 

num2 = int(-2.8)
print(num2) 

num3 = float(5)
print(num3) 

num4 = complex('3+5j')
print(num4) 

#Python modul acak
import random

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

print(random.choice(list1))

random.shuffle(list1)

print(list1)

print(random.random())

#Python Matematika
import math

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))