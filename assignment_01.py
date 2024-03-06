#Assignment 1 
# Victor H Torres. 
# DATA602 
# 02/02/2024


#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
# We need to add value type (integer = int) in the input lines
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
# We need to add a third input line to fullfil the requirements of the program 
test3 = int(input('Enter the score for test 3: '))
# Calculate the average test score.
average = test1 + test2 + test3 / 3
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
# we need to change the HIGH_SCORE variable to capital letters, Phyton is case sensitive
if average >= HIGH_SCORE:
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width.
# Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
a = float(input('Enter Length of the Rectangle 1: '))
b = float(input('Enter Width of the Rectangle 1: '))

area = a * b
c = float(input('Enter Lenght of the Retangle 2: '))
d = float(input('Enter Lenght of the Retangle 2: '))

area1 = c * d

total_area = area + area1

print('Area of rectangle 1 is : ' , area)
print('Area of rectangle 2 is : ' , area1)
print('Area of both rectangles is: ', total_area)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  
name = str(input('Please enter your First Name: '))
age = int(input('Please enter your Age: '))
#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
print('Happy birthday,' , name,'!.' 'You are' ,  age ,"years old today! ")

