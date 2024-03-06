# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:07:15 2024

@author: vitug
"""

#1. Create a list called animals that contain the following: cat, dog, manta ray, horse, crouching tiger

animals = ['cat', 'dog', 'manta ray', 'horse', 'crouching tiger']


#2. Repeat question 1 and loop through and print each item in the animal list
# by iterating through an index number and using range().
# Set a variable len_animals to the length of the animal list.

animals = ['cat', 'dog', 'manta ray', 'horse', 'crouching tiger']
len_animals = len(animals)
print(len_animals)  
for i in range(len(animals)): 
    print(i, animals[i])
    

#3. Programmatically reorganize the countdown list below in descending order
# and return the value of the 5th element in the sorted countdown list.
#The 5th element will be stored in the variable the_fifth_element
# which currently below has a dummy value of -999.
#Remember, the index number of the 5th element is not 5
countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
countdown.sort(reverse=True)
the_fifth_element = [4]
print(countdown)
print(the_fifth_element) 


#4. Write a program to add item 7000 after 6000 in the following Python List
#Expected output:
#[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].insert(2, 7000)
print(list1)


#5. Write a program to remove all occurrences of item 20 in the following list.
list2 = [5, 20, 30, 15, 20, 30, 20]
occ_item = 20

for item in list2:
    if(item==occ_item):
        list2.remove(occ_item)
        print(list2)
    

##6. Using the following dictionary .. (Use python to solve for the answer.)

dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}
#a. What is the name of the course?
print ("the name of the course is", list(dict.values())
       [list(dict.keys()).index("Course")])
#b. Change the course to DATA602
dict.update({"Course": "DATA 602"})
print(dict)
#c. Add new information to the dictionary - "Professor" with "Schettini"
dict.update({"Professor" : "Schettini"})
print(dict)
#d. Using the len function, find how many keys there are in the dictionary. 
print(len(dict.keys()))

#7.  Write a Python program to change Brad’s salary to 7500 in the following dictionary.

sample_dict = {                             
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
    }
    sample_dict['emp3']['salary']=7500
    print(sample_dict)