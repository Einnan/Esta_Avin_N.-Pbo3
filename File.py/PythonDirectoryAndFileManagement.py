#Python Directoy agar bisa mendapatkan direktori kerja saat ini menggunakan os.getcwd()
import os
print(os.getcwd())

#Python untuk mengubah direktori
import os

os.chdir("C:/Users/Einnan36/OneDrive/Documents/coding")
print(os.getcwd())

#Python directori list dan file
import os
print(os.getcwd())
# C:\\Python33

os.listdir()
['DLLs',
'Doc',
'include',
'Lib',
'libs',
'LICENSE.txt',
'NEWS.txt',
'python.exe',
'pythonw.exe',
'README.txt',
'Scripts',
'tcl',
'Tools']

os.listdir('C:/Users/Einnan36/OneDrive/Documents/coding')
['$RECYCLE.BIN',
'Movies',
'Music',
'Photos',
'Series',
'System Volume Information']

#Python directori baru
os.mkdir('test')

os.listdir()
['test']

#Python ganti nama direktori
import os

os.listdir()
['test']

os.rename('test','baru')

os.listdir()
['baru']

#Python hapus direktori
import os
    #Menghapus "myfile.txt" file
os.remove("tumbal.txt")
    
    #Menghapus direktori kosong
os.rmdir("mydir")

    #Menghapus "mydir" dan dan semua konten
import shutil

shutil.rmtree("mydir")