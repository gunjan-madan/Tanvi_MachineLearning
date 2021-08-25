# Pandas is a Python library used for working with data sets.

# It has functions for analyzing, cleaning, exploring, and manipulating data.

"""---------Intro to Pandas------------"""
print(" ")
print("*** Intro:***")

#install the pandas module
#pip install pandas

#Panda Series
# A Pandas Series is like a column in a table.

# It is a one-dimensional array holding data of any type.


import pandas as pd
a = [23, 47, 15]
myvar = pd.Series(a)
print(myvar)

#Read the data :
print()
print("***Read value in series***")
print(myvar[1])
#Create Labels

# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)
# print(myvar[y])

"""****Create a Series****"""
#Create a series 
# index  value
# US      Unites States
# UK      United Kingdom
# IN      India
# AU      Australia
# NZ      New Zealand

print()
print("***Create Series from dictionary***")
#Create Pandas Series from dictionary
#Key becomes index 


# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)

"""DIY"""
#Create a dictionary for Employee IDs as keys and Storing name 
# ID: PY001  Name: James  
# ID: PY102  Name: Alex   
# ID: PY440  Name: Keith  
# ID: PY324  Name: Susan   
# ID: PY100  Name: Michael 
