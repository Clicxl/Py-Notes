# Loops

nums = [1 , 2 ,3 ,4 , 5]

# For loop 
for num in nums: # Each time the code is looped the output will be the next value
  print(num)
# For loop keyword :
# Break ( Breaks the loop completely)
print('Break Loop')
for num in nums: 
  # print(num) # Prints the no. 3
  if num == 3:
    print('Found!')
    break
  print(num) # Does not print the equalent num (3) because it is below the break keyword
# Continue (Ingnore a value and continues in the loop)
print('Continue Loop')
for num in nums :
  if num == 3:
    print('Skipped' , num)
    continue
  print(num)  

# Loop within a Loop
for num in nums :
  for letter in 'abcde': # Be careful with nested list as it takes a lot of time to loop thorugh
    print(num, letter) # Loops thorugh every char in the str and print out number and prints the letter and then to the next num (Run to understand)
  
# Range (Looping a certain number of times)
for i in range(10): 
  print(i) # Goes up to but including the number passsed in the range
# Giving where to start in the range
for i in range(1,10): 
  print(i)
# To include the last the number in the range go up a no.
for i in range(1,11):
  print(i)

# While Loop (Just loops umtil a certain condition is met or until a break is hit)
x = 0
while x < 10:
  print(x)
  x +=1 # Dont forget to increase the value of the var or the loop keeps on going

# Break for the While loop
x = 0
while x < 10:
  if x == 5:
    break
  print(x)
  x +=1

# Infinite Loop ( Loops until a certain input is given or some value is found)

x = 0
while True:
  if x == 5:
    break # This Break statement is compulsory to stop the 
  print(x)
  x +=1