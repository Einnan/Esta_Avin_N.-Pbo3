#python set
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

#Python menciptakan set kosong
empty_set = set()          
empty_dictionary = { }   

print('Data type of empty_set:', type(empty_set))

print('Data type of empty_dictionary:', type(empty_dictionary))

#Python set menghapus duplikasi
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)  

#Python menambah elemen di set
numbers = {21, 34, 54, 12}
print('Initial Set:', numbers)
numbers.add(32)
print('Updated Set:', numbers)

#Python memperbarui set
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)

#Python menghilangkan elemen di set
languages = {'Swift', 'Java', 'Python'}
languages.discard('Java')
print(languages)   

#Python iterasi himpunan
fruits = {"Apple", "Peach", "Mango"}
for fruit in fruits:
    print(fruit)

#Python mencari set element
even_numbers = {2, 4, 6, 8}
print('Total Elements:', len(even_numbers))


#Python set operasi
    #gabungan 2 set
A = {1, 3, 5}
B = {0, 2, 4}
print('Union using |:', A | B)
print('Union using union():', A.union(B))   

    #set irisan
A = {1, 3, 5}
B = {1, 2, 3}
print('Intersection using &:', A & B)                 
print('Intersection using intersection():', A.intersection(B)) 

    #perbedaan antar set     
A = {2, 3, 5}
B = {1, 2, 6}
print('Difference using -:', A - B)                 
print('Difference using difference():', A.difference(B))  

    #set perbedan simetris
A = {2, 3, 5}
B = {1, 2, 6}
print('using ^:', A ^ B)                            
print('using symmetric_difference():', A.symmetric_difference(B))

#Python set kesamaan 
A = {1, 3, 5}
B = {3, 5, 1}
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')