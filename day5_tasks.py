# Classes Lab

# Task 1 - Student Class and 2 Objects

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"This is the student name: {self.name}\nThis is the student age: {self.age}\n"

student_1 = Student("Bob Dylan", 82)
student_2 = Student("Neil Young", 77)
print(student_1)
print(student_2)

# Task 2 - Student Class Modifications

import statistics

class Student:

    def __init__(self, name, age, classroom):
        self.name = name
        self.age = age
        self.classroom = classroom

    def __str__(self):
        return f"This is the student name: {self.name}\nThis is the student age: {self.age}\n"
    
    def average_test_score(self):
        score1, score2, score3 = input("Give me all your three of your scores, seperated by a space: ").split()
        scores = [int(score1), int(score2), int(score3)]
        average_score = statistics.mean(scores)
        return average_score      

student_1 = Student("Janis Joplin", 27, "A6")

print(f"{student_1.name}'s score is: {student_1.average_test_score()}")

# Task 3 - Parent and Child Classes (Bird)

class Bird:

    def __init__(self, name, age, wingspan):
        self.name = name
        self.age = age
        self.wingspan = wingspan

    def __str__(self):
        return f"This is the bird name: {self.name}\nThis is the age: {self.age}\nThis is the wingspan: {self.wingspan}"
    
class Owl(Bird):
    
    living_status = "alive"
    
    def __init__(self, name, age, wingspan, owl_type):
        super().__init__(name, age, wingspan)
        self.owl_type = owl_type

    def __str__(self):
        return f"This is the bird name: {self.name}\nThis is the age: {self.age}\nThis is the wingspan: {self.wingspan}\nThis bird is of the type: {self.owl_type}"

    def alive_or_extinct(self):
        return f"This owl is {self.living_status}"
    
class Dodo(Bird):
    
    living_status = "dead"
    
    def __init__(self, name, age, wingspan, dodo_type):
        super().__init__(name, age, wingspan)
        self.dodo_type = dodo_type

    def alive_or_extinct(self):
        return f"This dodo is {self.living_status}"

new_owl = Owl("Hawkings", 18, "85cm", "barn owl")
print(new_owl)
print(new_owl.alive_or_extinct())

print("\n")

new_dodo = Dodo("Steve", 20, "60cm", "Rodrigues solitaire")
print(new_dodo)
print(new_dodo.alive_or_extinct())


