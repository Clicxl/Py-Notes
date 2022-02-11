# Dictionaries (Allow to work with key value pairs)
# Just like a real Dictionaries , where there is the word (key) and the meaning (Value)
from turtle import st


student = {'name': 'Clicxl', 'age' : 15, 'subjects': ['Math', 'CompSci'], 'number' : ''} # Value can be left enmpty also
print(student)
# To access a perticual value ['<key>']
print(student['subjects']) # Key or values in Dictionaries can be anything ( ints, str, inmuteable date, lists)
# print(['phone']) # Gives a key error if the key doesn't exists 
# Get method (Returns a none or default if there is a key err)
print(student.get('name'))
print(student.get('phone')) 
print(student.get('phone', 'Not_Found')) # A default value can be passes to the key with the second arg
# Adding keys/values to Dictionaries 
student['phone'] = '2341432539' 
student['name'] = 'Annyman'
print(student.get('phone', 'Not Found'))
# If a key already exsits and has a value this update/changes the value
student['name'] = 'Annyman'
print(student.get('name'))
# Update method ( Values can also be updated using this method) ( Useful when to update multiple values at a time)
student.update({'name' : 'Omi' , 'age' : '15' , 'phone' : '6966696420'})
print(student)

# Delete a perticual key and value
# del student['age']
# print(student) # uncomment (ctrl+c+k)

# Pop method (see #Lists Tuples Sets.py)
age = student.pop('age')
print(age)
print(student)
# Check how many keys in a Dictionaries (len)
print(len(student))
# View all keys 
print(student.keys())
# View all values
print(student.values())
# Pairs of keys and values 
print(student.items())
# Looping Dictionaries
for key in student:
  print(key) # prints only key not value

# To print both key and value 
for key, value in student.items():
  print(key ,' = ', value)
 


