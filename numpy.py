import numpy as np
#1>Write a program to add 2 lisi a=[1,2,3],b=[4,5,6]
""" a=[1,2,3]
b=[4,5,6]
s=[]
for i in range(0,3):
    s.append(a[i]+b[i])
print(s) """
#//numpy
""" import numpy as np
a=[1,2,3] 
b=[4,5,6]
print(np.array(a)+np.array(b))
np_a=np.array(a)
print(np_a )"""
#numpy is applicable for list
#numpy ment for mathematical and scintific program
# Numpy aims to array object that 50X faster than python list
#Numbpy is a n dimension array


#methods of numpy
#print dimension
""" a=np.array([0,1,2,3,4])
print(type(a))
print(a.ndim) """
#shape of dimension
#print(a.shape)#one dimension
#Two dimension ->a nested list
""" b=np.array([[1,2,3],[4,5,6]])
print(b.ndim)
print(b.shape) """

#Matrix
""" mm=[[1,2,3],[4,5,6],[7,8,9]]
my_matrix=np.array(mm)
print(my_matrix.ndim)
print(my_matrix.shape) """

#Arange
#->arange is an array value version of the built in python range function
#->syntax :np.aggange(start,end,step)
""" a=np.arange(10,20,2)
print(a) """

#linspace -oneline + equal space
#->Return evenly spaced numbers over a specified given interval
#->Syntax:np.linespace(start,end,num_of_sample)
""" print(np.linspace(1,11,3)) """
#zeros
#->Generate arrays of zeros, defult folt data type
#->syntax(np.shape)
""" print(np.zeros((4,)))
print(np.zeros((3,3))) """

#random.rantint
#->return random integer from start (inclusive) to end (exclusive)
#syntax: np.random.randint(start,end,number_of_sample)
 
""" # print(np.random.randint(1,100,15))
a=np.random.randint(1,100,15)
print(a[5:10:2]) """

#indexing in numpy array.
""" a=np.array([45,2,3,5,4,3,1,56,7,9,30])
print(a[[0,6,2]]) """
#mask inexing or fancy indexing
""" a=np.array([45,2,3,5,4,3,1,56,7,9,30])
print(a%2==0)
print(a[a%2==0]) """

#Numpy array is mutuable in Nature so we can add ,replace and remove elements
#-> replace a single value a[5]=10
#-> replace a multiple value a[[5,6]]=11
#->append value a=np.append(a,[2,5,6])
#->delete a single 
#->a=np.delete(a,2)
#->delete a multiple 
#->a=np.delete(a,[1,2]])

#-->shallow copy and deep copy also applicable for list

#============== Operations ===============
#->Flattering: converting n dimensional array into one dimensional array
#->
""" a=np.array([[1,2,3],[5,6,4]])
print(a.ravel()) """

#->Reshape array
# arr=np.arange(20)
""" print(arr)
print(arr.shape)
  #two set of bracket
a1=arr.reshape(2,10)
print(a1) """
#note while reshape the element must be in for fo noofelement=x*y
#reshape 2*3 a 2d array  to 3*2
""" a=np.array([[1,2,3],[4,5,6]])
print(a.reshape(3,2)) """
#transport array :converting the rows into column
""" a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a.T) """
#sort array along axis: axis-1 --> row,axis=0 -> column
""" a=np.array([[5,4,6],[2,8,2]])
b=np.sort(a,axis=0)
c=np.sort(a,axis=1)
print(b)
print(c) """
#digonal element
""" a=np.diag([1,2,3])
print(a) """

#Arithematics Operation
#add
# a=np.array([3,4,5,2,0])
# print(a+1)
# b=np.ones((3,3))
# print(b+1)

#simple multiply
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
# print(a*b)
m=np.matmul(a,b)
print(m)#1*5+2*7   1*6+2*8  3*5+6*7 3*6+4*8

#Comparision Operators
a=np.array([1,2,3,4])
b=np.array([5,2,2,4])
#for each element it is going to check
print(a==b)
print(a>b)
# complete arr-aywise
print(np.array_equal(a,b))

#Mathematical Different
a=np.arange(1,6)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))
