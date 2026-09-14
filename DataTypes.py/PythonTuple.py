#Python membuat tuple 
numbers = (1, 2, -5)
print(numbers) 

tuple_constructor = tuple(('Jack', 'Maria', 'David'))
print(tuple_constructor) 

empty_tuple = ()
print(empty_tuple) 

#Python tuple dengan tipe data berbeda
names = ('James', 'Jack', 'Eva')     
float_values = (1.2, 3.4, 2.1)      
mixed_tuple = (2, 'Hello', 'Python') 

#Python mengakses item tuple
languages = ('Python', 'Swift', 'C++')
print(languages[0])  
print(languages[2])

#Python tuple tidak dapat diubah
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')


#Python panjang tuple
print('Total Items:', len(cars))

#Python iterasi tuple
fruits = ('apple', 'banana', 'orange')
for fruit in fruits:
    print(fruit)

#Python cek keberadaan item
colors = ('red', 'orange', 'blue')
print('yellow' in colors) 
print('red' in colors)   

#Python tidak bisa mengubah itemdi tuple
fruits = ('apple', 'cherry', 'orange')

#Python menghapus tuple
animals = ('dog', 'cat', 'rat')
del animals  

#Python dengan 1 tuple 
var1 = ('Hello')   
print(var1)  
var2 = ('Hello',)  
print(var2)         