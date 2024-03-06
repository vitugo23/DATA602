# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:13:20 2024

@author: vitug
"""

#1. Write a function to calculate the area and perimeter of a rectangle.
lenght = float(input("Please enter a number: "))
breadth = float(input("Please enter a number: "))
area = lenght * breadth
perim = 2 * (lenght * breadth)
print("Area of retangle is ", area)
print("Perimeter of retangle is ", perim)

#2. Write a function to check if a number is even or not.  
#The function should indicate to the user even or odd.
num = int(input(" Please Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even number". format(num))
else:
    print("{0} is Odd number". format(num))

#3. Write a Python function that accepts a string and calculate the number
#of upper case letters and lower case letters.
#Sample string: “CUNY sps”
# of upper case characters: 4
# of lower case characters: 3
letter = str(input("PLease enter a word: "))
lcc = 0
ucc = 0
for i in letter:
    if (i>='a'and i<='z'):
         
        lcc=lcc+1               
    if (i>='A'and i<='Z'):
         
        ucc=ucc+1
         
print('Lower case count: ',lcc)
print('Upper case count: ',ucc)


#4. Write a Python function to sum all the numbers in a list
num = [1,2,33,45,66,78,99,23,15]
suma = sum(num)
print(suma)

#5. Create a function that shows an example of global vs local variables.
#local variable
m = "my local variable"
print(m)
#global variable
n = "is this"
def myfunc():
  print("global variable " , n)

myfunc()


#6. Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number.

    import numpy    
def multiply2(*args):      
    return numpy.prod(args)  
print(multiply2(1,2,4))