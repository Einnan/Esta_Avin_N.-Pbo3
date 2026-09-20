#Python global keyword mengakses dan memodifikasi variable global
a = 7
def add():
   # a = a + 3 <Output akan menunjukan error karena variable global tidak bisa diubah didalam fungsi
    print(a)

add()

    #caranya dengan menambahkan method (global) agar variable global tetap bisa di ubah didalam fungsi
a = 7
def add():
    global a
    a = a + 3
    print(a)
add()