# Lists 

subjects = ['Maths', 'Physics', 'Social Science', 'II Lang', 'III Lang', 'CompSci', 'Biology' , 'Chemistry']
print(subjects) # Prints the whole list
# Length function
print(len(subjects))
# Accessing Each Index
print(subjects[3]) # Wrong index gives "Index out of range"
# Accessing multiple indexes / Slicing
print(subjects[0:5]) # Second index will not be included but the first will be
# Other way this can be done is
print(subjects[:4])
print(subjects[4:])
print(subjects[2:3])

# List Methods

# Adding items to lists
subjects.append('Art') 
print(subjects) 
# Insert Method for adding indexes to perticual place (Take 2 args [place , 'Id'])
subjects.insert(4,'Music')
print(subjects)
# Other lists can also be inserted 
subjects_2 = ['DP', 'Econimics', 'Geography', 'History']
# subjects.insert(6,subjects_2) #(Remove this line from comment to see)
print(subjects) # Inserts the list itself than as a str
# Extend
subjects.extend(subjects_2)
print(subjects)
# Remove Method ( Removes indexs)
subjects.remove('Maths')
print(subjects)
# Pop Method ( Removes the last index)
subjects.pop()
print(subjects)
# Get the poped Index
poped_index = subjects_2.pop()
print(poped_index)
# Reverse Method ( Reverses the List)
subjects_2.reverse()
print(subjects_2)
# Sort Method  (sorts lists in alphabetical order)
subjects.sort()
print(subjects)
# If lists contains numbers it sorts them in asending order 
marks = [3 , 5,7,2,8]
marks.sort()
print(marks)
# Descending order sorting
marks.sort(reverse=True)
subjects.sort(reverse=True)
print(marks,subjects)
# Sorted Method ( Sorts the List but saves the orignal one)
sorted_subs = sorted(subjects)
print(sorted_subs)
# Min , Max and Sum
# Min = Minimum value of the list
print(min(marks))
# Max = Maximum value of the list
print(max(marks))
# Sum = Sum of the list
print(sum(marks))
# Index Method (Finds indexes)
print(subjects.index('CompSci')) # If value doesn'e exsist then gives value error
# In oparator (checks if the index is presnt and gives a true/false)
print('DP' in subjects) 
#for loop can also be used 
for item in subjects: #item is a var
  print(item) # Prints each index in the list 
#  Getting the index and the value (enumerate)
for index,item in enumerate(subjects): 
  print(index,item) 
# Enumrate start value 
for index,item in enumerate(subjects, start=1): 
  print(index,item) 
# Join Method ( List in to Str)
subjects_str = ' - ' .join(subjects) # '' is how you want to separate the list like , . -
print(subjects_str)
 # Turning turning Str into list
subjects_list = subjects_str.split(' - ')
print(subjects_list)

# Tuples (unmodifiable/inmuteable lists)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci') # () should be used instead of []
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art' # Type error Cannot be done

#print(tuple_1)
#print(tuple_2)
# Excpcet Methods that change list others can be used

# Sets : Values that are unordered and have no duplicates of them
# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'} # use {} instead of ()/[]
# Sets order can change each time you run them
print(cs_courses) 

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}# Sets are used to check if a value is a part of a set or remove duplicates aka membership test
print(cs_courses)

# Intersection method ( checks the common Value in sets)
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'DP'}
print(cs_courses.intersection(art_courses))
# Difference methdod (Check what are not common in sets)
print(cs_courses.difference(art_courses)) # This says uncommon values only in main set(cs_courses) not in the sub set(art_courses)
# Union method (Check what are not common in both sets)
print(cs_courses.union(art_courses))

# Empty List Tuples Sets

# Empty Lists
empty_list = []
empty_list = list() # More ideal

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()