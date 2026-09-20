#Python Recursion function (memanggil dirinya sendiri kedalam fungsinya sendiri)
def factorial(x):
    ''' Ini adalah fungsi rekursif
    untuk mencari bilangan factorial'''

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

nmr = 8
print("Factorial dari ", nmr, "adalah", factorial(nmr))

def x():
    x()

x()