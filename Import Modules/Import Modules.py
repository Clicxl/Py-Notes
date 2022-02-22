from Explorting_File import find_index, test # Imports specified kewords or functions 
# from Explorting_File import * # imports everything ( Cannot tell which module it came from)
import Explorting_File as export  # Makes it easy to call
courses = ['History', 'Math', 'Physics', 'CompSci'] 

# All fines if imported will run

# When importing a module you cannot call the function directly 
# index = Explorting_File.find_index(courses , 'Math') # old method
# print(index)


index = export.find_index(courses, 'Math') # Gives acces only to find index module nothing else
print(index)
print(test)


# Where does python find the module ( Sys path)
import sys
print(sys.path) # prints all the paths it checks

import random # Always use tested moudules 
random_course = random.choice(courses)
print(random_course )