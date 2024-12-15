import numpy as np
import pandas as pd
df=pd.read_csv("diabetes.csv")
# print(df.head())
# print(df.info())
"""
+++++++++++++++++++
| Data Extraction |
+++++++++++++++++++
->exact data from dataset as per hour requirment.
1>by using condition
2>by using iloc()& loc()
3>combation of condition and loc()
"""

#using condition ,syntax : df[condition]
""" df["Age"]>50
df=df[df["Age"]>50]
# print(df[["Age","BMI"]]) """

#apply multiple condition
#in pandas we use the symbol for condition
""" df=df[(df["BloodPressure"]>70) | (df["Age"]>50)]
print(df.head(50)) """
#+++++++++
#| iloc :| i-index ,loc-location 
#+++++++++
#->we are identifying the the index location ,using the index number it is going to work.
#syntax :df.iloc[row_index,column_index] , df.iloc[[list+of_row_indexes],[list_of_column_indexes]]
#exact a singe value witn row index and column index
print(df.iloc[0,3]) #35
#exact a multiple value witn row index and column index list
""" print(df.iloc[0:5,3:9])
print(df.iloc[[0,3,5],[3,6,8]])
print(df.iloc[0]) # ger first row with all the  column,
print(df.iloc[:,0])# get all row  with  first column,
print(df.iloc[-1])#last row with all the column
# print(df.iloc[1,2,3])#error we have maintain row column by ,but multiple use list
print(df.iloc[[1,2,3],]) """

#+++++++++
#| loc :| loc-location , base on row-name or column-name
#+++++++++

#?What is the different b/w loc and iloc
"""
 -> in  loc we are exacting data from the data set use location name ,column-name ,row-name 
 ->in iloc we exact data from dataset usinh row index and column index 
   iloc[-1]#givwe last row record result
   loc[-1]#error no row name with -1 
"""
#Retriving selected row with range of columns "Glucose" to "Insulin"
# print(df.loc[[5,6,7],"Glucose":"Insulin"])
#print(df.loc[[5,6],4:5])#error no column name as 4 or 5
# print(df.loc[:,"Glucose"])#all rows with glucose column

#Index Naming
#+++++++++++++++++++++++
#set_index("columnname")#it will set the column values as index name of row,normally we provide a unique column as index
""" print(df.head(10))
df=df.set_index("DiabetesPedigreeFunction")
print(df.head(10))
print(df.loc[0.134]) """
#reset_index(): it return to th original data 

# GroupBy :
#mean concept of statictics
age50=df[df["Age"]==50]
# print(age50.head(5))
print(age50.mean())
#Value count

#value_counts 
#-Applyf fro only categorical data
#->For Each category,there respective frequency / Count
print(df.info())
print(df["Outcome"].value_counts())
print(df["Outcome"].value_counts()/len(df["Outcome"]))#percentage
# can pass argument normilize=true in value count for precentage
print(df["Outcome"].value_counts(normalize=True))
# print(df["Age"].value_counts())
