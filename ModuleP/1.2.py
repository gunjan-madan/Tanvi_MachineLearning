"""---------Dataframes------------"""
print(" ")
print("*** Intro:***")

import pandas

mydataset = {
  'studentID': ["ID1", "ID2", "ID3"],
  'name': ["James", "Viraj", "Michael"]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


#Print Dataframe without index
print(myvar.to_string(index=False))

"""Task: Create a DataFrame"""
print()
#Create a dictionary with following data:
# ID: PY001  Name: James   Designation: Developer
# ID: PY102  Name: Alex   Designation: Team Lead
# ID: PY440  Name: Keith   Designation: Designer
# ID: PY324  Name: Susan   Designation: Project Manager
# ID: PY100  Name: Michael   Designation: Tester

#Convert this to a DataFrame and print it.

"""---------Add More Rows------------"""
print(" ")
print("*** Append rows:***")
#Add new rows to a DataFrame using the append function. This function will append the rows at the end.

# import pandas as pd

# df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

# df = df.append(df2)
# print(df)