import numpy as np
import pandas as pd
# a=np.arange(0,100,10)
# print(a)
"""
++++++++
| DATA |
+++++++|
       |----> 1.) Cross sectional data (Not related to Time)
       |         |->a) contineous Data (Numeric,have decimal)
       |         |->b) Discreate Data
       |                 |->1.Discrete Count(only Numeric,no decimal)
       |                 |->2.Discrete Cateorical
       |                          |->i.  Nominal Discrete Categorical (There is no natural sequence between them,ex colors,(all are equal)))
       |                          |->ii. Ordinal Discreate Categorical (If theere is a natural Sequence then,ex-grade,small<medium<large(all are not equal))
       |---> 2.) TimeSeries Data (time is import parameter to predit)
"""
#->column,variable,feature are the data level name, ml-feature,syatics-variable
# Contineous Data : if Decimal value is possible
# Count data : if decimal value is not possible then it is called as count data

#df.dtypes : it will show all the data type of columns

df=pd.read_csv("diabetes.csv")
# print(df)
# print(df.dtypes)
#Data Understanding: Understanding Each Variable Name Clearly
#DataSet Understanding : Number of Record/Row, No.of feature/Column ,no.of categorical data ,contineous data,descrete count dat like you have to observe

#Q)Predect whether a person has liver problem or not
# 1st step)  Business Understanding
# print(df.head()) #give first 5 record of dataset
# print(df.tail()) #give las 5 record of dataset
# print(df.shape) # give you the shape of DataSet (row,colums)
# print(df.size) # give you the size of DataSet (roow*colums)
#print(df.columns) # gives you all the column name
#print(df.keys) # gives the keys of the dataframe
#print(df.type) # gives you all types of columns

# print(df.info()) # all the information will come in one short

#?how to check the missing value,

# print(df.isnull())
# print(df.isnull().sum())#return all null data sum
#print(df.isna().sum())#return all null data sum

#? How to access a single column
# print(df["Glucose"])
# print(df.Glucose)
# print(df["Glucose"].values)#return the specific value as array

#? How to access a multiple column
# print(df.info())
# print(df[["Glucose","Age"]]) #list of column name

#?How to drop a perticular row
""" df1=df.drop(767,axis=0)#index to be deleted ,axis=0 row-wise,
print(df1.tail())
#multiple delete
df1=df.drop([0,1,2],axis=0)
print(df1.head()) """

#?How to drop a perticular colume 
# print(df.info())
""" df3=df.drop("Outcome",axis=1)#is search the colname in  columns if avaliable delete that asix=1 colum,multple colun ,add list of column name
print(df3.head()) """

#?How to Add A new Column
#df['coulum']=value
# df['DOB']=2024-df["Age"]
# print(df.head())
#drop and save colunm
# df=df.drop("DOB",axis=1)
# print(df)
# df.drop("Age",axis=1,inplace=True)
# print(df.head())

##Sort the values of columns
print(df.head())
df=df.sort_values(by="Age",ascending=False)
print(df.head())
