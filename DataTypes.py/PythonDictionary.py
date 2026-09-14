#Python dictionary
siswa = {
    'nama': 'Avin',
    'umur': 20,
    'kelas': 'XV'
}

#Python membuat dictionary
d1 = {'a': 1, 'b': 2}
d2 = dict(x=10, y=20)    
d3 = {}                   
d4 = dict()               

#Python akses elemen
print(siswa['nama'])             
print(siswa.get('umur'))
print(siswa.get('alamat', '-')) 

#Python tambah dan ubah data
siswa['umur'] = 18        
siswa['alamat'] = 'Jakarta'    

#Python hapus data
siswa.pop('kelas')              

#Python method penting
d = {'a': 1, 'b': 2}
print(d.keys())              
print(d.values())          
print(d.items())             
d.update({'c': 3})  
d.setdefault('d', 4)  

#Python iterasi dictionary
for key in d:            
    print(key)
for value in d.values():         
    print(value)
for key, value in d.items(): 
    print(key, value)

# Python cek key dan panjang
print('a' in d)          
print(len(d))        

#Python dictionary comprehension
kuadrat = {x: x**2 for x in range(1, 6)}
print(kuadrat)                 

#Python dictionary bertumpuk
mahasiswa = {
    'mhs1': {'nama': 'Andi', 'umur': 20},
    'mhs2': {'nama': 'Budi', 'umur': 21}
}
print(mahasiswa['mhs1']['nama']) 