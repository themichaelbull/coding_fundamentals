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
    
    def average_test_score(self, score1, score2, score3):
        scores = [int(score1), int(score2), int(score3)]
        average_score = statistics.mean(scores)
        return average_score      

student_1 = Student("Janis Joplin", 27, "A6")

score1, score2, score3 = input("Give me all your three of your scores, seperated by a space: ").split()

print(f"{student_1.name}'s score is: {student_1.average_test_score(score1, score2, score3)}")

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

### ### ### ### ### ###
### ### ### ### ### ###

# Classes Challenges 

# Challenge 1
# Create a Rectangle class with attributes length and width
# Add methods to calculate the area and perimeter of the rectangle

class Rectangle:
    
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        self.area = self.width * self.length
        return self.area
    
    def perimeter(self):
        self.permieter = 2 * (self.width + self.length)
        return self.permieter
    
rectangle_1 = Rectangle(5, 10)
print(rectangle_1.area())
print(rectangle_1.perimeter())

# Challenge 2
# Create a BankAccount class with attributes account_number and balance. 
# Add methods to deposit and withdraw money from the account. 

class BankAccount:
    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.balance = balance

    def __str__(self):
        return f"Account Num: {self.account_num}\nBalance: £{self.balance}"
    
    def deposit(self, money):
        self.balance = int(money) + self.balance
        return f"You have deposited £{money} into your account! Your new balance is: £{self.balance}"
    
    def withdraw(self, money):
        self.balance = self.balance - money
        return f"You have withdrawn £{money} from your account! Your new balance is £{self.balance}"
    
    def current_balance(self):
        return f"Your current balance is: £{self.balance}"
    
michael_bank_account = BankAccount(1, 0)

print(michael_bank_account)
print("\n")
print(michael_bank_account.deposit(2))
print(michael_bank_account.current_balance())
print(michael_bank_account.withdraw(1))
print(michael_bank_account.current_balance())

# Challenge 3 
# Create a Car class with attributes make, model, and year. 
# Add methods to get and set the values of the attributes. 

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}"
    
    def get_details(self, detail): # getter
        if detail == "make":
            return f"Make: {self.make}"
        elif detail == "model":
            return f"Model: {self.model}"
        elif detail == "year":
            return f"Year: {self.year}"
        
    def set_details(self, detail, value): # setter
        if detail == "make":
            self.make == value
            return f"The make of this car is now: {self.make}"
        elif detail == "model":
            self.model == value
            return f"The model of this car is now: {self.model}"
        elif detail == "year":
            self.year == value
            return f"The year of this car is now: {self.year}"
    
car1 = Car("ford", "focus", 1993)
print(car1.get_details("make"))
print(car1.set_details("year", 1982))

# Challenge 4
# Create a Product class with attributes name, price, and quantity. 
# Add methods to calculate the total value of the product (price * quantity) 
# and add or remove items from the product inventory. 

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product name: {self.name}\nProduct price: {self.price}\nProduct quantity: {self.quantity}"
    
    def total_value(self):
        return f"Total value of product is: {self.price * self.quantity}"
    
    def change_stock_count(self, inc_or_dec, num):
        if inc_or_dec == "increase":
            self.quantity = self.quantity + num
            return f"\nYou have added {num} amounts of stock to the product {self.name}\n"
        elif inc_or_dec == "decrease":
            self.quantity = self.quantity - num
            return f"\nYou have removed {num} amounts of stock to the product {self.name}\n"
        if self.quantity < 0:
            self.quantity = 0

videogame1 = Product("Mario RPG", 50, 30)
print(videogame1)
print(videogame1.change_stock_count("increase", 20))
print(videogame1)
print("\n",videogame1.total_value())

# Challenge 5 - Rewrite Rock Paper Scissors app using a class

import random, sys

class Welcome:

    def __init__(self):
        pass

    def greet_player():
        return "Hi! What is your name?"

    def welcome_player(player_name):
        return f"\nWelcome {player_name}!\n"

    def play_question():
        return "Do you want to play?"

    def game_start(player_answer):
        if player_answer == "yes":
            return "\nSweet, let's go!\n"
        else:
            print("\nNo bother, catch you next time!\n")
            sys.exit()


class Rock_Paper_Scissors_Game:
    rounds_played = 0
    human_wins = 0
    computer_wins = 0
    options = {1: "rock", 2: "paper", 3: "scissors"} 

    def __init__(self, player_name):
        self.player_name = player_name

    def start_game(self):
        print("*" * 80)
        for choice, option in self.options.items():
            print(f"\nChoice: {choice} --- Option: {option.title()}")
        print("\n", "*" * 80)
        return f"\n{self.player_name}, What's your move?\n\nEnter number of move: "
    
    def player_and_computer_choices(self, player_choice):
        computer_chosen = random.randint(1,3)
        player_chosen = self.options[int(player_choice)]
        computer_chosen = self.options[computer_chosen]
        print("*" * 80)
        print(f"\nYou have chosen: {player_chosen.title()}\nComputer has chosen {computer_chosen.title()}\n")
        return player_chosen, computer_chosen
    
    def winner_logic(self, player_hands):
        player_hand = player_hands[0]
        computer_hand = player_hands[1]

        if player_hand == computer_hand:
                return "draw"
        elif player_hand == "rock":
            if computer_hand == "scissors":
                return "player wins"
            elif computer_hand == "paper":
                return "computer wins"
        elif player_hand == "paper":
            if computer_hand == "rock":
                return "player wins"
            elif computer_hand == "scissors":
                return "computer wins"
        elif player_hand == "scissors":
            if computer_hand == "paper":
                return "player wins"
            elif computer_hand == "rock":
                return "computer wins"
        
    def announce_winner(self, result):
        if result == "player wins":
            print("Player wins!\n")
        elif result == "computer wins":
            print("Computer wins!\n")
        elif result == "draw":
            print("It's a tie!\n")

    def update_score(self, result):
        self.rounds_played += 1
        if result == "player wins":
            self.human_wins += 1
        elif result == "computer wins":
            self.computer_wins += 1

    def display_score(self):
        print(f"Rounds Played: {self.rounds_played}\nHuman Wins: {self.human_wins}\nComputer Wins: {self.computer_wins}\n")
        print("\n","*" * 80)

    def play_again(self, response):
        if response == "yes":
            print("\nGreat, let's go again!")
        else:
            sys.exit()

### ### ###

def main():

    # Welcome user, take name, ask if they want to play

    print(Welcome.greet_player())
    player_name = input()
    print(Welcome.welcome_player(player_name))
    print(Welcome.play_question())
    player_answer = input()
    print(Welcome.game_start(player_answer))

    ### ### ###

    # Start game
    game = Rock_Paper_Scissors_Game(player_name)

    while True:
        print(game.start_game())
        player_choice = input().lower()

        # Getting User and Computer Moves
        player_hands = game.player_and_computer_choices(player_choice)

        # Working Out Winner
        result = game.winner_logic(player_hands)

        # Showing Result

        game.announce_winner(result)

        # Update Scoreboard

        game.update_score(result)
        game.display_score()

        # Play Again?
        response = input("\nWant to play again? ")
        game.play_again(response)

main()

# Challenge 6 - Bookshelf and Books
class Book:
    def __init__(self, title, author, publisher, pub_year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pub_year = pub_year

    def __str__(self):
        return f"Book title: {self.title}\nAuthor name: {self.author}\nPublisher: {self.publisher}\nYear published: {self.pub_year}"

class BookShelf:
    def __init__(self, current_cap=0, list_of_books=[], max_cap=3):
        self.current_cap = current_cap
        self.list_of_books = list_of_books
        self.max_cap = max_cap

    def __str__(self):
        return f"Bookshelf Current Capacity: {self.current_cap}\nList of Books: {self.list_of_books}"

    def add_book(self, book):
        self.list_of_books.append(book)
        if self.current_cap < self.max_cap:
            self.current_cap += 1
            print(f"The book {book.title} has been added to the bookshelf!\n")
        else:
            return "Capacity is full!"

    def remove_book(self, book):
        self.list_of_books.remove(book)
        print(f"The book {book.title} has been removed from the library")

    def find_book_by_title(self, book):
        searchable_title = book.title
        titles = []
        for book in self.list_of_books:
            titles.append(book.title)
        if searchable_title in titles:
            print(f"\nThe book {book.title} is in library\n")
        else:
            print(f"\nIt ain't there!")

    def find_book_by_author(self, book):
        searchable_author = book.author
        authors = []
        for book in self.list_of_books:
            authors.append(book.author)
        if searchable_author in authors:
            print(f"\nThe author {book.author} is in the library\n")
        else:
            print(f"\nThey ain't there!")

# Just some ASCII Art

book = ("                  \n"
"     ______ ______      \n"
"   _/      Y      \_    \n"  
"  // ~~ ~~ | ~~ ~  \\   \n"
" // ~ ~ ~~ | ~~~ ~~ \\  \n"   
"//________.|.________\\ \n"    
"`----------`-'----------\n")

print(book, "\nWelcome to the library! What would you like to do?\n")
print("*" * 80, "\n")

# Creating Books

book1 = Book("the shock doctrine", "naomi klein", 2007, "Knopf Canada")
book2 = Book("through the looking glass", "lewis carroll", 1871, "Macmillan & Co")
book3 = Book("buddhism", "steven hagen", 1997, "penguin")
book4 = Book("clean code", "robert martin", 2008, "pearson")

# Creating Bookshelf

new_bookshelf = BookShelf(current_cap=0, max_cap=3)

# Adding Books to Bookshelf
new_bookshelf.add_book(book1)
new_bookshelf.add_book(book2)

# Removing a book and proving it isn't there
new_bookshelf.remove_book(book1)
new_bookshelf.find_book_by_title(book1)

# Searching for book that is there
new_bookshelf.find_book_by_author(book2)
