# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:06:55 2024

@author: vitug
"""

"""1. What are the similarities and differences between pandas and numpy? 
Include some type of example with code.
Pandas is a library written in Python that provides high-performance,
fast, easy-to-use data structures,and data analysis tools for manipulating numeric
data, with Pandas with can import data from various formats such as: SQL, Excel, etc"""
 import pandas as pd
 
height = [['Victor', 1.93, "Male"], ['Viviana', 1.78, "Female"],
       ['Diego', 1.89, "Male"], ['Fatima', 1.75, "Female"]]
 
dataf = pd.DataFrame(height, columns=['Name', 'Height', 'Gender'])

dataf
"""Numpy is the fundamental Python library, used to perform scientific computing.
It provides high-performance multidimensional arrays and tools to deal with them."""
import numpy as np
 
number_array = np.array([[7, 10, 13],
                      [23, 32, 44],
                      [19, 14, 17]])
 
print(number_array)

"""2. What is the ndarray in numPy?
ndarray is a short for N-dimensional array, and it's the main data structure in NumPy.
Ndarray must contain data of the same type, such as integers or string values."""

"""3. Create a 1D array of numbers from 0 to 9 
Desired Output: 
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"""
import numpy as np
num = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(num)


"""4. Extract all odd numbers from array1 """
import numpy as np
array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array1[array1 % 2 != 0])

"""5. Get the common items between a and b"""  
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c = np.intersect1d(a,b)

print("Common values" , c)


"6. From array a remove all items present in array b"
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
remove = np.setdiff1d(a, b)
print(remove)

"""7. Find out if iris has any missing values.""" 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
  
    from urllib.request import urlopen
    from bs4 import BeautifulSoup 
    
    url = "'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'"
    html = urlopen(url)
    
    soup = BeautifulSoup(html, 'lxml')
    type(soup)
    bs4.BeautifulSoup
    
    
"""# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])"""
