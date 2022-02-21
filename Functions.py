# Functions
# Definiton

def hello_func() : #() no parameters
  pass # pass To fill in a funtion later

# How functions work
print(hello_func) # Without parentheses ( Gives that its a function and its mem location)
print(hello_func()) # As it doesnot have a return value it says none

def hello_func():
  print('Hello Function!')  

hello_func() # does not need print coz it just runs the function
# Allows to reuse code without repeating ourselves 
# Instead of using the same code over and over ( which is also tedious to change) you can use functions
# If a function is changed the entire thing is changed 
# DRY  (Dont repeat yourself) 
# Allows to oparate on some data  and return it to the called function

# Return function ( )
def hello_func():
  return 'Hello Function.' # 

hello_func() # does not print coz its just a string
print(hello_func()) # does print it
print(len(hello_func())) # if function is a retuing a str it can have all parameters of a str
print(hello_func().upper())

# Adding args to functions 
def args_func(greeting): # Greeting arg is requied arg as it doesnot have defalut value 
  return'{} Functions.'.format(greeting)

print(args_func('Hi')) # set the Greeting functions to Hi

# Two or more args 
def two_args(greetings , name = 'You'): # Adding defalut value
  return'{} {}'.format(greetings, name)

print(two_args('Hi')) # does print without err the default value
print(two_args('Hi' , 'Clicxl'))

def student_info(*args , **kwargs): # Allows to accpet arbitary no. of postional or keyword args
  print(args)
  print(kwargs) # Other Random info , if the postional or keyword are there

student_info('Math' , 'Art' , name='Clicxl' , age=15) 

# Unpacking a sequence
courses  = ['Math', 'Art']
info = {'name':'Clicxl' , 'age':15 }
student_info(courses,info) # Passes the complete Dictionaries or the complete list as an arg 
student_info(*courses,**info) # using ** un packs lists and tupels and ** unpacks Dictionaries

# Examples 
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years.""" # """ Dock str explains how the functions goes

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017)) # False 
print(is_leap(2020)) # True

print(days_in_month(2017,month=1))
print(days_in_month(2017,month=2))
# Leap year
print(days_in_month(2020,month=1))
print(days_in_month(2020,month=2))