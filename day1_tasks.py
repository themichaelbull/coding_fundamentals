print('\nHi there! Below is Task 1\'s output:\n')

# Task 1 - Hello World
print('Hello World', end="\n\n---------\n")

### ### ###

print('\nBelow is Task 2\'s output:\n')

# Task 2 - Display Message Using Variable
username = 'Michael'
age = 30
print(f"{username} is {age} ", end="\n\n---------\n")

### ### ###

print('\nBelow is Task 3\'s output: (you need to enter details this time)\n')

# Task 3 - Get User Input
username, age = input("Enter your name and age, with a space seperating each:\n").split()
print(f"{username} is {age}", end="\n\n---------\n")

### ### ###

print('\nBelow is Task 4\'s output:\n')

# Task 4 - Get User Input - Perform Calculations

length = int(input("\nEnter length of one side of your rectangle.\n"))
width = int(input("Enter width of one side of your rectangle.\n"))
perimeter = (length * 2) + (width * 2)
area = length * width

print(f"\nThe perimeter of your rectangle is: {perimeter}\n"
    f"\nThe area of your rectangle is: {area}")

print("\n\nThat's it! Cheers!")

### ### ###

# Task 5

# make a dictionary of books with 3 authors, and multiple books per author.
# Use an input() asking for an author name
# print back as a string the lst of books by the author
# use the .join() method.

books = {"George Orwell": ["1984", "Animal Farm"], "Jane Austen": ["Pride and Prejudice", "Sense and Sensibility"], "Ernest Hemingway": ["The Old Man and the Sea", "For Whom The Bell Tolls"]}
author_name = input("Please give me an authors name, I'll give you a list of books\n")
authors_books = ", ".join(books[author_name])
print(authors_books)
print(type(authors_books))

### ### ###