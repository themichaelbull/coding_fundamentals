print('\nHi there! Below is Task 1\'s output:\n')

# Task 1 - If/Elif/Else Student Score

student_score = int(input("Hi there! What was your score from the exam today?\n"))

if student_score >= 85:
    print("You got a distinction. Well done!")
elif student_score >= 65:
    print("You got a pass. Nice!")
else:
    print("I'm sorry to say you failed.")

### ### ###

# Task 2 - Weight Converter

pound_terms = ("lb", "lbs", "pounds")
kg_terms = ("kg", "kgs", "kilograms")

user_weight, weight_type = (input("""What is your weight and what measurement 
is it in? Please seperate these by a space: """)).split()

if weight_type.lower() in pound_terms:
    print(round(int(user_weight) * 0.45359237,1), "kg")
elif weight_type.lower() in kg_terms:
    print(round(int(user_weight) * 2.2,1), "pounds")
else:
    print("You didn't provide a weight or weight type correctly. Please run the program again.")


### ### ###

# Task 3 - Create a Calculator

num_1, num_2 = (input("Give me two numbers please. Seperated by a space: ")).split()
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1)
print(num_2)

print("1. Add +\n2. Subtract -\n3. Multiply *\n4. Divide /\n5. Square s\n")
operator = int(input(("Choose an operator: ")))

if operator == 1:
    print(num_1 + num_2)
elif operator == 2:
    print(num_1 - num_2)
elif operator == 3:
    print(num_1 * num_2)
elif operator == 4:
    print(num_1 / num_2)
elif operator == 5:
    print(num_1 ** num_2)
else:
    print("You didn't choose from 1-5, run the program again.")

### ### ###

# Task 4 - Calculate Exam Grades Redux

student_score = int(input("Hi there! What was your score from the exam today?\n"))

if student_score >= 71:
    print("You got a distinction. Well done!")
elif student_score >= 61:
    print("You got a merit. Nice work!")
elif student_score >= 50:
    print("You passed. Good stuff.")
else:
    print("I'm sorry to say you failed.")

### ### ###

# Task 5 - Calculate Exam Grades with Levels

student_score, student_level = (input("Hi there. Please give me your score and your student level, seperated by a space: ")).split()

student_score = int(student_score)

if student_level == "1":
    if student_score >= 71:
        print("You got a distinction. Well done!")
    elif student_score >= 61:
        print("You got a merit. Nice work!")
    elif student_score >= 50:
        print("You passed. Good stuff.")
    else:
        print("I'm sorry to say you failed.")
if student_level == "2":
    if student_score >= 66:
        print("You got a distinction. Well done!")
    elif student_score >= 51:
        print("You got a merit. Nice work!")
    elif student_score >= 40:
        print("You passed. Good stuff.")
    else:
        print("I'm sorry to say you failed.")

### ### ###

# Task 6 - Pythagoras Calculator

import math

user_option = int(input("Pythagoras' Calculator - Choose an Option!\n\n1. Find the length of A given B and C\n2. Find the length of B given A and C\n3. Find the length of C given A and B\n\n"))

if user_option == 1:
    b, c = (input("\nGive me the lengths of side B and C, seperated by a space: ")).split()
    b = int(b)
    c = int(c)
    print("The length of side A is:\n")
    print(math.sqrt((c**2) - (b**2)))
elif user_option == 2:
    a, c = (input("\nGive me the lengths of side A and C, seperated by a space: ")).split()
    a = int(a)
    c = int(c)
    print("The length of side B is:\n")
    print(math.sqrt((c**2) - (a**2)))
elif user_option == 3:
    a, b = (input("\nGive me the lengths of side B and C, seperated by a space: ")).split()
    a = int(a)
    b = int(b)
    print("The length of side C is:\n")
    print(math.sqrt((a**2) + (b**2)))

### ### ###

# Extra Task

a = int(input("Give me your first number: "))
b = int(input("Give me your second number: "))
c = int(input("Give me your third number: "))

if a > b and a > c:
    x = a
elif b > a and b > c:
    x = b
elif c > a and c > b:
    x = c

if x % 2 == 0:
    print("Even number")
elif (x % 2 != 0) and (x % 3 == 0):
    print("Odd number and multiple of 3")
elif (x % 2 != 0):
    print("Odd number")

# Extra Task - Shorter

numbers = []

numbers.insert(1, int(input("Give me your first number: ")))
numbers.insert(2, int(input("Give me your second number: ")))
numbers.insert(3, int(input("Give me your third number: ")))

sorted(numbers)
x = numbers[-1]

if x % 2 == 0:
    print("Even number")
elif (x % 2 != 0) and (x % 3 == 0):
    print("Odd number and multiple of 3")
elif (x % 2 != 0):
    print("Odd number")

# Extra Task - Shorter Again

numbers = []

while len(numbers) < 3:
    num = int(input("Enter number"))
    numbers.append(num)

sorted(numbers)
x = numbers[-1]

if x % 2 == 0:
    print("Even number")
elif (x % 2 != 0) and (x % 3 == 0):
    print("Odd number and multiple of 3")
elif (x % 2 != 0):
    print("Odd number")

# While Loop Example

x = 0
while x < 5:
    name = (input("Give me a persons name please!\n"))
    print(f"{name} is great!")
    x += 1

###########################
###########################

### LAB 3 Start  - While Loops ###

# Task 1 - Squares

x = 1

while x < 100:
    print(x ** 2)
    x += 1
    if (x ** 2) > 2000:
        break

# Task 2 - Factorial

factorial = int(input("Give me a number, I'll give you the factorial: "))
new_factorial = list(range(1, factorial+1))
number = 1
while True:
    if new_factorial == []:
        break 
    number = new_factorial.pop() * number

print(f"Your factorial result is: {number}")

# Task 3 - Investment

init_invest = 100
years = 0

print(f"Initial Investment: {init_invest}")

while init_invest < 1000:
    interest_amount = init_invest / 10
    init_invest = round(init_invest + interest_amount)
    years += 1
    print(f"Year {years}: {init_invest}")

print(f"\nIt will take {years} years to get your investment to £1000")

# Task 4 - Input an Integer Between Two Limits

min = 1
max = 100

x = 3
while x != 0:
    user_guess = int(input("Give a number between range of the two numbers 1 to 100: "))
    if user_guess >= 1 and user_guess <= 100:        
        print(f"Yes! {str(user_guess)} is in that range specified")
        break
    x = x - 1
    if x == 0:
        print(None)
    else:
        print("Incorrect try again")

# Task 5 - Count Vowels

chosen_word = (input("Please give me a word: "))
user_word = list(chosen_word)
vowel_count = 0
while user_word:
    letter = user_word.pop()
    if letter in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

print(f"Your word '{chosen_word}' has a vowel_count of {vowel_count}")

# Task 6 - Exam Average

subjects = ['maths', 'english', 'ict']
average_mark = 65
overall_result = 0

while True:
    subject = subjects.pop()
    x = 1
    while True:
        result = int(input(f"Please give me your result for {subject}: "))
        if result >= 0 and result <= 100:
            overall_result = overall_result + result

            break
        else:
            print("Enter a valid mark")
    if subjects == []:
        break

user_average_result = round(overall_result / 3)

if user_average_result >= average_mark:
    print(f"\nPass! Well done! You passed with: {user_average_result}")
else:
    print(f"\nUnlucky, you failed. You're score was {user_average_result}")
print(f"\nThe average result typically is {average_mark}")

# Task 7 - Squares again but with For Loops

for number in range(1,100):
    squared = number ** 2
    if squared >= 2000:
        break
    print(squared)

# Task 8 - Factorial Again but with For Loops

factorial = int(input("Give me a number, I'll give you the factorial: "))
factorial += 1
number = 1

for x in range(2, factorial):
    print(f"{number} multipled by {x}")
    number = number * x

print(f"Your factorial result is: {number}")

###########################
###########################

### Lab 4 Start - For Loops ###


# Task 1 - Ages List

# Original ages list

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,
9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,
63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

# Length of list

amount_of_ages = len(ages)
print(f"Here is the length of the list ages: {amount_of_ages}\n")

print("\n",80 * "*","\n")

# List printed one at a time

print(f"Here is all the ages in the list ages, one at a time:\n")

for age in ages:
    print(age)

print("\n",80 * "*","\n")

# List items altered by 1

print(f"Here is all the ages in the list ages, altered to be aged up by 1\n")

updated_ages = []

for age in ages:
    age += 1
    updated_ages.append(age)
    print(updated_ages[-1])

print("\n",80 * "*","\n")

# List items altered exlusively having ages 16-65

removeold = [age for age in updated_ages if (age <= 65) and (age >= 16)]
print(f"Here is our list, with the age range being 16-65\n\n{removeold}")

print("\n",80 * "*","\n")

# List altered using .sort() method

print(f"Here is the list sorted using the .sort() method\n")
removeold.sort()
print(removeold)

print("\n",80 * "*","\n")

# Getting proporation/percentage of altered list that has ages between 16-25

print(f"Here is the proporation/percentage of ages that fall between 16-25:\n")

sixteen_to_twenty25 = [age for age in removeold if (age <= 25) and (age >= 16)]
decimal = len(sixteen_to_twenty25) / len(removeold)
percentage = round(decimal * 100, 2)
print(str(percentage) + "%")

# Task 2 - Count Vowels w/ For Loops

word = input("Please enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for letter in word:
    if letter in vowels:
        count += 1

print(f"Your word is {word} and the amount of vowels in that word is: {count}")

# Task 3 - Time Calculator # In Progress

import sys

# Functions/Logic of Time Calculator and Menu

def showmenu():
    print("\n", 80 * "*", "\n")
    print()
    print("Time Calculator")
    print("1. Add 2 times")
    print("2. Find the difference between 2 times")
    print("3. Convert to Hours")
    print("4. Convert to Minutes")
    print("5. Convert Minutes to Time")
    print("6. Convert Hours to Time")
    print("7. Convert Days to Time") # Don't do
    print("8. Exit\n")

def option_one(user_time1, user_time2): # still kinda jank
    days = int(user_time1[0:2]) + int(user_time2[0:2])
    hours = int(user_time1[3:5]) + int(user_time2[3:5])
    minutes = int(user_time1[6:]) + int(user_time2[6:])
    extra_days = (hours // 24)
    days = days + extra_days
    extra_hours = hours % 24
    hours = hours + extra_hours
    extra_minutes = minutes // 60
    hours = hours + extra_minutes
    minutes = minutes % 60
    print(f"Your time added together is: {days}:{hours}:{minutes}")

def option_two(user_time1, user_time2):
    user_time1_DtoM = int(user_time1[0:2]) * 1440
    user_time1_HtoM = int(user_time1[3:5]) * 60
    user_time1_M = int(user_time1[6:])
    user_time1minutes = user_time1_DtoM+user_time1_HtoM+user_time1_M
    print(user_time1minutes)

    user_time2_DtoM = int(user_time2[0:2]) * 1440
    user_time2_HtoM = int(user_time2[3:5]) * 60
    user_time2_M = int(user_time2[6:])
    user_time2minutes = user_time2_DtoM+user_time2_HtoM+user_time2_M
    print(user_time2minutes)

    timediff = user_time1minutes - user_time2minutes

    print(timediff)
    option_five(timediff)

def option_three(user_time):
    days = (int(user_time[0:2]) * 24)
    hours = (int(user_time[3:5]))
    print(f"You time convereted to hours is {days+hours} hours!")

def option_four(user_time):
    days = (int(user_time[0:2]) * 24) * 60
    hours = (int(user_time[3:5])) * 60
    minutes = (int(user_time[6:]))
    print(f"You time convereted to minutes is {days+hours+minutes} minutes!")

def option_five(minutes):
    if int(minutes) <= 60:
        print(f"Your minutes moved into time format is: 00:00:{int(minutes)}")
    if int(minutes) > 61 and int(minutes) < 1440:
        hours = int(minutes) // 60
        minutes = int(minutes) % 60
        print(f"Your minutes moved into time format is: 00:{int(hours)}:{int(minutes)}")
    if int(minutes) >= 1440:
        days = int(minutes) // 1440
        hours = (int(minutes) % 1440) // 60
        minutes = (int(minutes) % 1440) % 60
        print(f"Your minutes moved into time format is: {int(days)}:{int(hours)}:{int(minutes)}")

def option_six(hours):
    if int(hours) < 24:
        print(f"Your hours moved into time format is: 00:{int(hours)}:00")
    if int(hours) >= 24:
        days = int(hours) // 24
        hours = int(hours) % 24
        print(f"Your hours moved into time format is: {int(days)}:{int(hours)}:00")

### ### ###

# While Loop with calling of logic functions

while True:

    showmenu()

    user_option = input("Please select an option: ")

    if user_option == "1":
        time1 = input("Give me your first time please, in the format DD:HH:MM: ")
        time2 = input("Give me your second time please, in the format DD:HH:MM: ")
        option_one(time1, time2)
    if user_option == "2":
        print("Make sure to put in your larger time first")
        time1 = input("Give me your first time please, in the format DD:HH:MM: ")
        time2 = input("Give me your second time please, in the format DD:HH:MM: ")
        option_two(time1, time2)
    if user_option == "3":
        time1 = input("Give me your first time please, in the format DD:HH:MM: ")
        option_three(time1)
    if user_option == "4":
        time1 = input("Give me your first time please, in the format DD:HH:MM: ")
        option_four(time1)
    if user_option == "5":
        time1 = input("Give me a set of time in minutes, I'll give you the time format: ")
        option_five(time1)
    if user_option == "6":
        time1 = input("Give me a set of time in hours, I'll give you the time format: ")
        option_six(time1)
    if user_option == '7':
        print("Chris said to skip this one. Functionality not available, try another option!")
    if user_option =='8':
        print("Thanks for using, goodbye!")
        sys.exit()