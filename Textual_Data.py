# Print Hello World
from turtle import st


message = 'Hello World'
print(message)

br_in_py = """use \""" 3 times to get br
like in html"""
print(br_in_py)

# Length of the String
print(len(message))
# Use [] to get a perticulars in py
print(message[8])
# Use [~:~!] to get all the char from that perticual part 
# ~ = start , ~! = end(does not include the ~! var)
print(message[2:7])
print(message[:5])
print(message[6:])

# Lower case a str
print(message.lower())
# Upper case a str
print(message.upper())
# Count a certain no. of Char in a str (takes a letters or word to count)
print(message.count('l'))
# Find something in str
print(message.find('World'))
# Change char 
new_message =message.replace('World', 'Universe') # Can reuse message instead of new str
print(new_message) 

# Multi strs and link them together
greeting = 'Hello'
name = 'Clicxl'

message = greeting + ', ' + name + '. Welcome! ' # Not ideal
print(message)

message = '{}, {}. Welcome!'.format(greeting, name) # Ideal way 
print(message)

# f strs
message = f'{greeting}, {name}. Welcome!' # New update and most ideal
print(message)

# Dir function
# print(dir(name))
# Help function
# print(help(str))
