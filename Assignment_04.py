# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:56:33 2024

@author: vitug
"""

"""Q1:  Create a class called BankAccount that has four attributes:
bankname, firstname, lastname, and balance.The default balance should be set to 0.
In addition, create a method called deposit() that allows the user to make deposits
into their balance. A method called withdrawal() that allows the user to withdraw from
their balance. Withdrawal may not exceed the available balance. Hint: consider a
conditional argument in your withdrawal() method. Use the __str__() method in order to
display the bank name, owner name, and current balance. Make a series of deposits and
withdrawals to test your class."""

class BankAccount:
    def __init__(self, bankname, firstname, lastname, balance):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = 0
      

      	def __str__(self):
   return "Bank name is: {self.bankname}, customer name is {self.firstname}, {self.lastname}"
    
        def getBalance(self):
    print("Balance: $ ", self.balance)
 
     def deposit(self):
         amount=float(input("Enter amount to be deposited: "))
         self.balance += amount
         print("\n Amount Deposited:",amount)
         
    def withdrawal(self):
        amount = float(input("Enter amount to be withdrawn: "))
             if self.balance>=amount:
                 self.balance-=amount
                 print("\n You Withdrew:", amount)
             else:
                 print("\n Insufficient balance  ")
                 
    def display(self):
        print("\n Net Available Balance=",self.balance)

s = BankAccount()
s.__str__()
s.getBalance()
s.deposit()
s.withdrawal()
s.display()
"""Q2: Create a class Box that has attributes length and width that takes values for
length and width upon construction (instantiation via the constructor). In addition,
create…a method calledrender()that prints out to the screena box made with asterisks
of length and width dimensions ● A method calledinvert()that switches length and width
with each other ● Methodsget_area()andget_perimeter()that returnappropriate geometric
calculations. A method calleddouble()that doubles the size of the box.
Hint: Pay attention to return value here. Implement__eq__so that two boxes can be
comparedusing ==. Two boxes are equal if their respective lengths and widths are
identical. A methodprint_dim()that prints to screen the lengthand width details of the
box. A methodget_dim()that returns a tuple containingthe length and width of the box.
A methodcombine()that takes another box as an argumentand increases the length and
width by the dimensions of the box passed in. A methodget_hypot()that finds the length
of thediagonal that cuts through the middle. Instantiate 3 boxes of dimensions5,10 ,
3,4 and 5,10 and assign to variablesbox1, box2 and box3respectively
Print dimension info for each usingprint_dim().
Evaluate ifbox1 == box2, and also evaluate ifbox1== box3, printTrueorFalseto 
the screen accordingly ● Combinebox3intobox1(i.e. box1.combine()) ● Double the size of
box2 ● Combinebox2intobox1"""

class Box:
    def __init__(self, length, width):
        self.length(self) = length
        self.width(self) = width  
        
    def calledrender(self):
        for row in range(length):
            for col in range(width):
         print("*"),
         print(" ")
    calledrender(7,12) 
    
    import numpy as np
    def calledinvert(self):
        print('switch lenght and Width')
    slw = np.array([lenght,width])
    print(slw)
 
    slw.shape = (width,lenght)
    print(slw)
 
if __name__ == "__calledinvert__":
    calledinvert()
    
    def Methodsget_area(self, area):
        return self.area = lenght * width
    print(self.area)
    def get_perimeter(self, perimeter):
        return self.permeter = 2 *(lenght + width)
    print(self.perimeter)
    
    def calleddouble(self):
        self.lenght = self.lenght() * 2
        self.width = self.width() * 2
        print(calleddouble())
        return self
        
    
    