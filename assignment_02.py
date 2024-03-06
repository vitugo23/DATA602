# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:30:51 2024

@author: victor H Torres
"""

"""Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])
IT WILL DISPLAY [].
 Can you debug and fix the output?  The code should return the entire list
 IN ORDER TO DISPLAY THE ENTIRE LIST WE SHOULD START WITH ZERO,
 TO PRINT THE ENTIRE LIST OR START WITH A COLON SIGN(:)"""
numbers =[1, 2, 3, 4, 5]

print(numbers[0:5])
print(numbers[:5])

"""Q2.Design a program that asks the user to enter a store’s sales
for each day of the week. The amounts should be stored in a list.
Usea loop to calculate the total sales for the week and display the result."""

sales = [int(input('Enter store sales for %s: ' % day)) for day in
  ['Sunday', 'Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday']]

totSum = sum(sales);
print("Total amount of weekly sales are: $" , totSum)


"""Q3.Create a list with at least 5 places you’d liketo travel to.
Make sure the list isn’t in alphabetical order
Print your list in its original order. 
Use the sort() function to arrange your list in order and reprint your list.
Use the sort(reverse=True) and reprint your list.""" 

places = ['Argentina', 'Spain', 'Italy', 'Japan', 'Croatia']

print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

"""Q4.Write a program that creates a dictionary containing course numbers
and the room numbers of the rooms where the courses meet.
The program should also create a dictionary containing course numbers and the names
of the instructors that teach each course. After that, 
the program should let the user enter a course number, 
then it should display the course’s room number, instructor, and meeting time.""" 

all_data = {
"room_meet" :  {'DAT602': 201, 'DAT606': 202, 'DAT607': 203},
"course_ins" : {'DAT602': 'Allan', 'DAT606': 'Brian', 'DAT607': 'Carla'},
"course_hours" : {'DAT602': '8:52', 'DAT606': '10:00', 'DAT607':'11:30'}}
inp = input("Enter a Course Number")
for value in all_data.items():
    print(value)

  

"""Q5. Write a program that keeps names and email addresses in a dictionary
as key-value pairs. The program should then demonstrate the four options:"""

note_book = {'Marco': 'mt@gmail.com', 'Bryan': 'br@hotmail.com', 'Alexa': 'al@outlook.com'}
#look up a person’s email address
lookup = note_book.get('Bryan')
print(lookup)
#add a new name and email address
note_book['Joe']= 'joe@yahoo.com'
print(note_book)
#change an existing email address
note_book.update({'Alexa': 'alex@apple.com'})
print(note_book)
# delete an existing name and email address
del note_book['Marco']
print(note_book)