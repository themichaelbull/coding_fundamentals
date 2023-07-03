# Exercise:

# 0 - Open a new text file called bands.txt and add the names of 5 bands
# 1 - Read and display the names of the 1st and 4th teams in the files
# 2 - Edit the teams.txt file so that the top line is replaced with "new line"
# 3 - Print out the edited file line by line

# 0 - Open a new text file called bands.txt and add the names of 5 bands

file = open("bands.txt", "w")
band_names = ["sleeve", "abnorm", "elephants", "anchor", "the last path"]

for band in band_names:
    newline = band + "\n"
    file.write(newline)
file.close()

### ### ###

# 1 - Read and display the names of the 1st and 4th teams in the files

file = open("bands.txt", "r")
lines = file.readlines()
file.close()

print(lines[0].strip()) # Removes the whitespace, good practice incase you accidently added whitespace in file
# But also! It gets rid of the newline character for us as well. That character is there as default in normal .txt files

print(lines[3].strip())

# print(repr(lines[0])) # repr function Shows string representation of what you are printing

### ### ###

#2 - Edit the teams.txt file so that the top line is replaced with "new line"

file = open("bands.txt", "r")

lines = file.readlines()
file.close()

lines[0] = "this is a new line" + "\n"
print(lines)

with open("bands.txt", "w") as file:
    file.writelines(lines)

### ### ###

# 3- Print out the edited file line by line

with open("bands.txt", "r") as file:
    for x in range(0,5):
        print(file.readline())

### ### ###

# Lab 7 

# Task 1

import csv

temp_dict = {}
total_sales = 0

with open("output.csv", "r") as file:
    test = csv.reader(file)
    next(test) # skips first line of file
    for line in test:
        temp_dict[line[0]] = line[1:]
        
month_list = ["Jan 2019", "Feb 2019", "March 2019", "April 2019", "May 2019", "June 2019", "July 2019", "Aug 2019"]
total_sales = []
final_list = []

for x in range(0,8):
    for k, v in temp_dict.items():
            num = v[x].replace(",", "")
            total_sales.append((int(num)))
    final_list.append(sum(total_sales))
    total_sales = []

for x in range(0,8):
     print(f"Total car sales across all manufacturers in {month_list[x]} were: {final_list[x]}")

# Task 2

import csv

temp_dict = {}
total_sales = 0

with open("output.csv", "r") as file:
    test = csv.reader(file)
    next(test) # skips first line of file
    for line in test:
        temp_dict[line[0]] = line[1:]

for k, v in temp_dict.items():
    print(f"{k}'s total sales this year was:")
    sales = 0
    for x in v:
        x = x.replace(",", "")
        sales += int(x)
        total_sales += sales
    print(str(sales) + "\n")
print(f"Total sales this year for all manufacturers combined were: {total_sales}")

### ### ###
### ### ###
### ### ###

# Linting Lab

"""This module contains functions for ways to check specific details of your lists"""
def count(sequence, item):
    """
    This function counts how times a specific item is in a sequence.

    Just pass to function first the sequence (a list or a tuple) and then
    the item you are wanting to count the amount of.
    """
    total_count = 0
    for number in sequence:
        if number == item:
            total_count += 1
    return total_count

print(count([1,2,3,3,4,5], 3))

### This passes pylint's test

###

# Testing Lab

# Part 1

def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

print(count([1,2,3,3,4,5], 3))

def test_int():
    assert count([1,2,3,3,4,5], 3) == 2

def test_str():
    assert count(["banana", "teracotta", "banana"], "banana") == 2

# Part 2

def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels

def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

###

def test_vowels():
    assert vowels("cake") == 2

def test_list_of_squares():
    assert list_of_squares(2) == {1: 1, 2: 4}

def fact(x):
    assert fact(2) == 1

