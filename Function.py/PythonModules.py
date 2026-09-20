#Python import modul standard
import math

print("Nilai pi adalah : ", math.pi)

#Python import modul dengan nama pengaanti library
import math as m
print("Nilai pi adalah : ", m.pi)

#Python import pernyataan dari library
from math import pi
print(pi)

#Python import semua modul pada library
from math import *
print(pi,)

#Python modul dir() untuk menampilkan semua nama fungsi dalam sebuah modul
a = 1
b = "hello"

import math

print(dir())

['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter'] 