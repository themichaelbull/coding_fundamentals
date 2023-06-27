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

user_weight, weight_type = (input("What is your weight and what measurement is it in? Please seperate these by a space: ")).split()

if weight_type.lower() in pound_terms:
    print(round(int(user_weight) * 0.45359237,1), "pounds")
elif weight_type.lower() in kg_terms:
    print(int(user_weight) * 2.2, "kg")
else:
    print("You didn't provide a weight or weight type correctly. Please run the program again.")