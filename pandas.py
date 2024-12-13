import pandas as pd
import numpy as np

# print(np.arange(1,10,1.5))
############ Pandas ##################################
#Using the pandas you can create series and dataframe 
#+++++++++++
# | Series |
#+++++++++++
# In series by default the row index number is same as row index name.
#-> in panda series the value are stored in row-wise

#We ca create series in multiple way :
#1>using list
""" l=[1,"a"]
s=pd.Series(l)
print(s) """
#2>Using array
""" a=np.array([234,45,2])
s=pd.Series(a,index=["a","b","c"])
print(s) """
#3>using Dictionary
""" d={1:"a",2:"b",3:"c"}
s=pd.Series(d)
print(s) """
""" d={"a":1,"b":2,"c":3}
s=pd.Series(d,index=["a","c"])#here i am not using c index
print(s) """
""" d={"col1":[1,2,3],"col2":[4,5,6]}#the value is store in row wise and automaticall the key will store as key
s=pd.Series(d)
print(s) """

#++++++++++++++
# | Dataframe |
#++++++++++++++
# in Dataframe Values are stored in Column-wise
#-> series is 1-dimensional,dataframe is 2-dimensional
#-> we can create series by list,1-Dimension Array or dictionary ,We can create Dataframe by nested list,@-Dimension Array or Dictionary
"""
d=[[1,2,3],[4,5,6]]
df=pd.DataFrame(d)
print(df) """

# Create Dataframe using NestedList of 2D Array
""" d=[[1,2,3],[4,5,6]]
df1=pd.DataFrame(d,columns=["C1","C2","C3"])
print(df1) """

#Creating Dataframe Using 2D array
""" d=np.array([[1,2,3],[4,5,6]])
df2=pd.DataFrame(d,columns=["C1","C2","C3"])
print(df2)
print(type(df2))
print(df2.shape)
"""
#Add colum DataFrame
#->the number of value should be match the number of colum when you assign value
""" d=np.array([[1,2,3],[4,5,6]])
df2=pd.DataFrame(d,columns=["C1","C2","C3"])
print(df2)
#df2["c4"]=[4,7,6] //error  Length of values (0) does not match length of index (2)
df2["c4"]=[4,7] 
print(df2) """

#Combining DataFrame
#++++++++++++++++++
# temprature_df=pd.DataFrame({"city":["Mumbai","delhi","bangalore","hyderbad"],"temprature":[32,45,40,36]})
# humidity_df=pd.DataFrame({"city":["delhi","mumbai","bangalore","chenai"],"humidity":[68,65,75,70]})
# | opiton 1: Append() |
# print(temprature_df)
# print(humidity_df)
# df=temprature_df.append(humidity_df)
#| option2 : concat   |
""" df=pd.concat([temprature_df,humidity_df])
df=pd.concat([temprature_df,humidity_df],ignore_index=True)
df=pd.concat([temprature_df,humidity_df],axis=0,ignore_index=True)
# axis=0 row wise ,axis=1 column wise,in numpy axis=0 meam colum and axis=1 row,id axis=1 data added side by side
print(df) """

#Merging Of DataFrame
#+++++++++++++++++++++++
#-> in pandas there is merge concept and in sql there is join
#Outer->Everything
#inner->common of A,B(common add ,A data(right value null),B data(left value null))
#Left->leftside part (Left side compulsory, Right sight common merge to first one)
#Right->RightsightPart (Right  side compulsory, Left sight common merge to second one)
#
""" temprature_df=pd.DataFrame({"city":["bangalore","delhi","Mumbai","hyderbad"],"temprature":[40,45,32,36]},index=[0,1,2,3])
humidity_df=pd.DataFrame({"city":["bangalore","delhi","Mumbai","chenai"],"humidity":[75,68,65,70]},index=[5,6,7,8])

df1=pd.merge(temprature_df,humidity_df,on="city",how="outer")
print("***************** Outer ********************")
print(df1)

df2=pd.merge(temprature_df,humidity_df,on="city",how="inner")
print("***************** Inner ********************")
print(df2)

df3=pd.merge(temprature_df,humidity_df,on="city",how="left")
print("***************** Left ********************")
print(df3)

df4=pd.merge(temprature_df,humidity_df,on="city",how="right")
print("***************** Right  ********************")
print(df4) """

# df5=pd.merge(temprature_df,humidity_df,on="city",how="cross")
# print("***************** Cross  ********************")
# print(df5)
df=pd.read_csv("diabetes.csv")
print(df)
