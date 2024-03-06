# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:58:28 2024

@author: Victor H Torres
"""

"""Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner
Then using if statements and else statements print the user a message recommending a
 meal. For example, if the meal was breakfast, you could say something like,
 “How about some bacon and eggs?”
The user may enter something else in, but you only have to respond to breakfast
, lunch, or dinner."""
meals = input("please select a meal(breakfast, lunch, dinner): ")

if meals == "breakfast":
    print("How about some yogurt and fruits?")
elif meals == "lunch":
    print("I recommend chicken or steak.")
elif meals == "dinner":
    print("you can have pizza or burger.")
else:
    print("Sorry, wrong choice.")


"""Q2: The mailroom has asked you to design a simple payroll program that calculates
 a student employee’s gross pay, including any overtime wages. If any employee works
 over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay
 rate for all hours over 20. You should take in the user’s input for the number of
 hours worked, and their rate of pay."""

worked_hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly rate: "))

if worked_hours <= 20:
    regular_rate = worked_hours * pay_rate
    overtime = 0
else:
    regular_rate = 20 * pay_rate
    overtime = worked_hours - 20
    overtime = overtime * 1.5 * pay_rate

gross_pay = regular_rate + overtime

print(f"Regular Pay: ${regular_rate:.2f}")
print(f"Overtime Pay: ${overtime:.2f}")
print(f"Total Gross Pay: ${gross_pay:.2f}")


"""Q3: Write a function named times_ten. The function should accept an argument and
 display the product of its argument multiplied times 10."""
 def times_ten(arg):
  print(arg*10)
  
times_ten(10)


"""SQ4: Find the errors, debug the program, and then execute to show the output."""
"""def main()

  Calories1 = input( "How many calories are in the first food?")
  Calories2 = input( "How many calories are in the first food?")
  showCalories(calories1, calories2)
def showCalories()
print(“The total calories you ate today”, format(calories1 + calories2,.2f))"""
# first change is to add colon at the end of argument
def main():
#I added a separation after the question mark to make the question look better   
  Calories1 = input("How many calories are in the first food? ")
  Calories2 = input("How many calories are in the second food? ")
# I added and int argument for the input.  
  showCalories(int(Calories1), int(Calories2))
# I added arguments to the showCalories function to accept calories1 and calories2
# Capitalized arguments, Python is case sensitive
def showCalories(Calories1,Calories2):
# I fixed colons to go in the right place
#I replaced the format method({:.2f}) to obtain the total calories
   print("The total calories you ate today {:.2f}".format(Calories1 + Calories2))
# call the main funtion to execute the program
main()


"""Q5: Write a program that uses any loop (while or for) that calculates the total
 of the following series of numbers:
         1/30 + 2/29 + 3/28 ............. + 30/1"""
         
 def suma_of (min,max):
  suma = 0

  for x in range(min,max+1):

    suma += (x)/(max-(x-1))

  return suma

min = 1
max = 30

    suma = suma_of(min,max)
print(suma)

print(round(suma,2))


"""Q6: Write a function that computes the area of a triangle given its base and
 height.The formula for an area of a triangle is:
AREA = 1/2 * BASE * HEIGHT
For example, if the base was 5 and the height was 4, the area would be 10.
triangle_area(5, 4)   # should print 10"""
def tri_area(base = 0,height = 0):
    if base == 0 and height == 0:
      base = float(input("Please enter the base of triangle: "))
      height = float(input("Please enter the height of triangle: "))
    area = (1/2)*base*height
    print(f"A {base} by {height} triangle has an area of {area}")

tri_area(5,4)
tri_area()
