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

# List Comprehension Method # Broken ATM

# new_grades = [item for item in new_grades new_grades.append(int(item)) for item in grades]


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

### Lab 6 ###