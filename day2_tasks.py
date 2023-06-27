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
    print((c**2) - (b**2))
elif user_option == 2:
    a, c = (input("\nGive me the lengths of side A and C, seperated by a space: ")).split()
    a = int(a)
    c = int(c)
    print("The length of side B is:\n")
    print((c**2) - (a**2))
elif user_option == 3:
    a, b = (input("\nGive me the lengths of side B and C, seperated by a space: ")).split()
    a = int(a)
    b = int(b)
    print("The length of side C is:\n")
    print(math.sqrt((a**2) + (b**2)))