# Classes and Instances
# Creating and instantiating simple classes

# Why are classes used :
# Allow to logically group data so it is easy to reuse and easy to build upon
 
# Simple Class 
class Employee: # No attribute 
  pass 

# A Class is a blue print for creating intances 
emp_1 = Employee()
emp_2 = Employee() # Now here each are an intances of the class Employee  
print(emp_1)
print(emp_2)

# Instance Variable ( Contain data that is unique to each instance )
# Manually create instances
emp_1.first = 'Clicxl'
emp_1.last = 'Youtube'
emp_1.email = 'Clicxl.Youtube@company.com'
emp_1.pay = 500000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 250000

print(emp_1.email)
print(emp_2.email)

# Setting this format for all classes 
# init Method
class Employee:
  def __init__(self,first , last , pay): # Always use a convention that is self ( you can use other thing but stick to self)
      self.first = first # the self.first can be chnaged like self.fname but keep both same
      self.last = last
      self.pay = pay
      self.email = f"{first}.{last}@company.com"

emp_1 = Employee('Sammy','Beast',100000) # emp_1 will be the self attibute and the rest stes itself in order
emp_2 = Employee('Anny','Chad',100000)
print(emp_1.email) 
print(emp_2.pay)

# Other useful things you can do
print(f'{emp_1.first} {emp_1.last}') # too much code
# Easier method

class Employee:
  def __init__(self,first , last , pay): 
      self.first = first 
      self.last = last
      self.pay = pay
      self.email = f"{first}.{last}@company.com"
  
  def fullname(self):
    return f'{self.first} {self.last}'

emp_1 = Employee('Sammy','Beast',100000) 
emp_2 = Employee('Anny','Chad',100000)

print(emp_2.fullname())