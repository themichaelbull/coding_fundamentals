# Exercise:

# Open a new text file called bands.txt and add the names of 5 bands

# 1 - Read and display the names of the 1st and 4th teams in the files
# 2 - Edit the teams.txt file so that the top line is replaced with "new line"
# 3 - Print out the edited file line by line

# 1 

file = open("bands.txt", "w")
band_names = ["sleeve", "abnorm", "elephants", "anchor", "the last path"]

for band in band_names:
    newline = band + "\n"
    file.write(newline)
file.close()

file = open("bands.txt", "r")

lines = file.readlines()

file.close()

print(lines)

print(lines[0].strip()) # Removes the whitespace, good practice incase you accidently added whitespace in file
# But also! It gets rid of the newline character for us as well. That character is there as default in normal .txt files

print(lines[3].strip())

# print(repr(lines[0])) # repr function Shows string representation of what you are printing

### ### ###

#2 

file = open("bands.txt", "r")

lines = file.readlines()
file.close()

lines[0] = "this is a new line"

file = open("bands.txt", "w")

for x in range(len(lines)):
    if x == len(lines):
        file.write(lines[x]) # Checks if last line and no new line character
    else:
        file.write(lines(x).strip() + "\n")
file.close()

# 3

file = open("bands.txt", "r")

for line in file:
    print(line.strip())
file.close()

# Doesn't all work, address later

### ### ###

# Lab 7 
# Task 2 # Needs to be used with output.csv file

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