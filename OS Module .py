import os
# print(dir(os)) # Get all the dir you can use 

# Prints the current dir your in
print(os.getcwd()) # get current working dir

os.chdir('C:/Users/Hrishi/Desktop/') # Change the dir
print(os.getcwd())

os.chdir('C:/Users/Hrishi/Desktop/Boomer_bots/Python/') 
print(os.getcwd())

# Lists the files in the folder 
print(os.listdir()) # path can be given but default is the dir your working in 

# Make a file in the provided dir 
# Method one
os.mkdir('ExampleDir')
print('Created ExampleDir')
# Method two
os.makedirs('ExampleDir2/Sub-Dir.py') # Can create a deep folder 
print('Created ExampleDir2/Sub-Dir.pyr')

# Remove a dir 
os.rmdir('ExampleDir') 
print('Deleted ExampleDir')
os.removedirs('ExampleDir2/Sub-Dir.py')
print('Deleted ExampleDir2/Sub-Dir.pyr')

# Remove a file or folder
os.mkdir('ExampleDir')
os.rename('ExampleDir' , 'Example')
print('Renamed')

# How to get info about a file
