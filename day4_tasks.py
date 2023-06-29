### Lab 5 ###

# Exercise 1 - Student Grade Statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
grades = data.split(",") # turns string of values into a list
new_grades = []

# For Loop Method 

for item in grades:
    item = int(item)
    new_grades.append(item)

print(min(new_grades)) # Displays minimum value of the grades
print(max(new_grades)) # Displays maximum value of the grades

# Map Function Method

new_grades = list(map(int, grades))
minimum = (min(new_grades))
maximum = (max(new_grades)) 
print(minimum) # Displays minimum value of the grades
print(maximum) # Displays maximum value of the grades

# List Comprehension Method
new_grades = [int(x) for x in data.split(',')] # Chris's solution - very neat

# Average of grades to 2 decimal points

total = sum(new_grades)
amount = len(new_grades)
average = round(total / amount, 2)
print(average)

# Use mean() function to get the average grade to 2 decimal places
import statistics

mean = round(statistics.mean(new_grades), 2)
print(mean)

# Use median() function to get the median value

median = round(statistics.median(new_grades), 2)
print(median)

# Use string.format() function to display min, max, average, mean and median values
statement = "The average of the grades is {}, the mean is {} and the median is {}\nMin is {} and Max is {}"
print(statement.format(average, mean, median, minimum, maximum))

##########################

### Lab 6 ### - This might be broken, need to test # Chris' solution

def getIncomeTax(salary):
    if salary < 11850:
        return 0
    elif 11850 <= salary <= 34500:
        return (salary - 11850) * 0.2
    elif 34501 <= salary <= 150000:
        return 4530 + ((salary - 34500) * 0.4)
    else:
        return 50730 + ((salary - 150000)) * 0.45 

salary = 200000
tax_amount = getIncomeTax(salary)
print("Tax anmount for salary £{} is £{}".format(salary, tax_amount))

# Task 3 - Function Challenges

# Sub-Task 1 - Password Checker

def password_checker():
    common_pwords = ["password", "abc123", "password1"]
    user_pword = input("Give me a new password: ")
    if user_pword.lower() in common_pwords:
        print(f"Use a safer password, '{user_pword}'' is compromised")
    else:
        print("Password is safe")

password_checker()

# Sub-Task 2 - Simple Calc

def simple_calc():
    x,y = (input("Please give me two numbers seperated by a space: ").split())
    x = int(x)
    y = int(x)
    print(f"{x} + {y} = {x+y}")
    print(f"{x} - {y} = {x-y}")
    print(f"{x} x {y} = {x*y}")

simple_calc()

###

# Sub-Task 3 - Highest Num

def highest_num(a,b,c):
    list_of_nums = []
    list_of_nums.append(a)
    list_of_nums.append(b)
    list_of_nums.append(c)
    highest = max(list_of_nums)
    return highest

print(highest_num(1,2,3))

# Sub-Task 4 - Odd or Even

def odd_or_even():
    user_num = input("Give me a number and I'll tell you if it's odd or even: ")
    if int(user_num) % 2 == 0:
        return f"{user_num} is even"
    else:
        return f"{user_num} is odd"
    
print(odd_or_even())

# Sub-Task 5 - Upper

def stringupper():
    user_string = input("Give me a string: ")
    return f"Here is your string in upper case: {user_string.upper()}"

print(stringupper())

###

## Sub-Task 6 - Radius to Area

import math

def area_of_circle():
    radius = int(input("Give me the radius of your circle: "))
    area = pow(radius, 2) * math.pi
    return area

print(area_of_circle())

###

# Sub-Task 7 - Celcius to Farenheight

def ctof(c):
    f = (c * 1.8) + 32
    return f

print(ctof(2))
