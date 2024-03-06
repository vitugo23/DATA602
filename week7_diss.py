# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:06:42 2024

@a"uthor: vitug"
"""

""""1. What is pandas and why use it?"""
"""Pandas is a Python library used for working with data sets. We should use pandas because
it has functions for analyzing, cleaning, exploring, and manipulating data."""

"""2. Give an example of how to import a csv file using pandas"""
import pandas as pd
df = pd.read_csv(r"C:\Users\vitug\OneDrive\Desktop\DATA_602\data.csv")

print(df)

"""3. Show how to view the first 10 rows of a dataset using pandas"""
import pandas as pd
rows = df.head(10)

print(rows)


"""4. Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]"""
import pandas as pd
ps1 = pd.Series([2, 4, 6, 8, 10])
ps2 = pd.Series([1, 3, 5, 7, 10])
print(ps1)
print(ps2)
print("Compare the elements of the two Panda Series:")
print("Equals :")
print(ps1 == ps2)
print("Greater :")
print(ps1 > ps2)
print("Not Greater :")
print(ps1 < ps2)
"""5. Change the first character of each word to upper case in each word of df1
df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])"""
import pandas as pd
df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
print (df1)
df1 = df1.str.capitalize()
print(df1)