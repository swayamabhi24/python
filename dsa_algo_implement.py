""" def fun(n):
 c=0
 i=0 
 while i< n :
    c=c+1
    i=i+1
 return c
print("The Complexity of the program is(O(n))",fun(100)) """

""" 
def fun(n):
 c=0
 i=0 
 while i< n :
    j=0
    while j<n:
       c=c+1
       j=j+1
    i=i+1
 return c
print("The Complexity of the program is(O(n^2))",fun(100)) """

""" 
def fun(n):
 c=0
 i=0 
 while i< n :
    j=0
    while j<n:
       k=0
       while k<n:
         c=c+1
         k=k+1 
       j=j+1
    i=i+1
 return c
print("The Complexity of the program is(O(n^3))",fun(100)) """
""" 
def fun(n):
 c=0
 i=n
 while i>0:
    c=c+1
    i=i//2
 return c
print("The Complexity of the program is(O(log(n))",fun(100))     
 """

""" 
def fun(n):
    c=0
    i=n
    while i>0:
         j=0
         while j<i:
            c=c+1
            j=j+1
         i=i//2
    return c
print("n=100,the no of insrruction of  program is(n2)",fun(100))   """

#Multipleloops in O(n)
""" def fun(n):
    c=0
    i=0
    j=0
    while i<n:
       while j<n:
         c=c+1
         j=j+1
       i+=1
    return c
print("n=100 , the number of instruction of the program is(O(n))", fun(100)) """

# print("logic Implementation")
#swap two integer possiblea
""" def swap_v1(a,b):
  a,b=b,a
  print(f'a={a}')
  print(f'b={b}')
def swap_v2(a,b):
  t=a
  a=b
  b=t
  print(f'a={a}')
  print(f'b={b}')

def swap_v3(a,b):
  a=a+b
  b=a-b
  a=a-b
  print(f'a={a}')
  print(f'b={b}')
def swap_v4(a,b):
  a=a*b
  b=a//b
  a=a//b
  print(f'a={a}')
  print(f'b={b}')

def swap_v5(a,b):
  a=a^b
  b=a^b
  a=a^b
  print(f'a={a}')
  print(f'b={b}')

print(swap_v1(9,2))
print(swap_v2(9,2))
print(swap_v3(9,2))
print(swap_v4(9,2))
print(swap_v5(9,2))
 """
 #sum of n natural number
""" def nsum1(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
def nsum2(n):
    return n*(n+1)//2
def nsum3(n):
    if n==0:
      return 0
    else:
      return n+nsum3(n-1)

print(nsum1(5))
print(nsum2(5))
print(nsum3(5))
 """
 #factroial
""" def fact(n):
    if n==0:
        return 1
    else :
          return n*fact(n-1)

def fact2(n):
    f=1
    while 0<n:
      f=f*n
      n=n-1
    return f
print(fact(9))
print(fact2(9)) """

#14. Digits Extraction
n=123
# while n>0:
#     d=n%10
#     print(d)
#     n=n//10

# n=str(n)
# for i in n[::-1]:
#     print(i)

#count digit:
""" def c(n):
    c=0
    while n!=0:
        c=c+1
        n=n//10
    return c
def c2(n):
    if n==0:
        return 0
    else:
        return 1+c2(n//10)

print(c(12303045))  
print(c2(12303045))      """

#reverse of a number
"""
exact digit
add to reverse by multiplay 10
reduce th number by divid 10
"""
""" def rev(n):
    r=0
    while n!=0:
        d=n%10
        r=r*10+d
        n=n//10
    return r
def rev2(n):
    return str(n)[::-1]
  
print(rev(10045))
print (rev2(10045)) """

#Amstrong number(sum=individual queue)
""" def isamstronf_v1(n):
   s=0
   t=n
   while n!=0:
    d=n%10
    s=s+d**3
    n=n//10
   if s==t:
    return True
   else:
    return False
print(isamstronf_v1(9))
print(isamstronf_v1(153)) """

#Strong Numer(sum =individual factorial)
""" import math
def isstrong(n):
  sf=0
  t=n
  while n!=0:
    d=n%10
    f=math.factorial(d)
    sf=sf+f
    n=n//10
  if sf==t:
    return True
  return False

print(isstrong(145))
print(isstrong(153)) """

#29. Fib sequence
#0 1 1 2 3 5 8 13 ......
""" 
def fib(n):
	L = []
	first = 0
	second = 1
	L.append(first)
	L.append(second)
	for i in range(n-2):
		next = first + second
		L.append(next)
		first = second
		second = next
	return L


print(fib(8)) #[0, 1, 1, 2, 3]

def fib2(n):
  f=0
  s=1
  print(0)
  print(1)
  while(n>2):
      next=f+s
      f=s
      s=next
      n=n-1
      print(next)

print(fib2(6)) """

#extract even numbers from a list
""" l=[1,2,3,4,5,6,7,8,9,10]
el=[i for i in l if i%2==0]
print(el) """

#get smaller elements from a list lesser then the given element x
""" def fun(l,x):
  sl=[]
  for i in l:
    if i<x:
       sl.append(i)
  return sl

print(fun([75,7,9,23,8,3],10)) """

#Generate 10 random numbers from 1 to 20 inclusive and append them to the list
""" import random
def fun(n):
 l=[]
 for i in range(n):
  l.append(random.randint(1,21))
 return l

print(fun(10)) """
#swap first and last elements in the list
""" def fun(L):
 L[0],L[-1]=L[-1],L[0]
 return L
l=[105,8,9,2]
print(fun(l)) """
#cont the numer of element greate than x in list
""" def fun(l,x):
	return len([i for i in l if i>x])
print(fun([5,6,7,2,0],5))
 """
#) Get the index of the given element
""" def fun(L,ele):
  for i in range(len(L)):
    if L[i]==ele:
      return i
  return None
print(fun([3,6,7,2,5,0],5)) """

# 30. Trib Sequence
""" def tri(n):
  f=0
  s=1
  t=2
  print(f)
  print(s)
  print(t)
  while(n!=3):
    d=f+s+t
    print(d)
    f=s
    s=t
    t=d
    n=n-1

print(tri(6)) """

#reverase a list with swapping logic:
#version1:
#---------
""" def fun(l,s,e):
	while s<=e:
		l[s],l[e]=l[e],l[s]
		s=s+1
		e=e-1

l = [1, 2, 3, 4, 5]
print(l)
fun(l,0,len(l)-1)
print(l)
 """
""" def swap_list_obj(lst,start,end):
       while(start<end):
            lst[start],lst[end]=lst[end],lst[start]
            print("--->")
            start=start+1
            end=end-1
       return lst
lst=["ram","hari",1,5,"gita"]
print(swap_list_obj(lst,0,len(lst)-1)) """
#alternate odd even index placs of a list
""" def swap_odd_even_index(l,s,e):
 for i in range(s,e,2):
        #  print(i)
         l[i],l[i+1]=l[i+1],l[i]
 return l
l=[1,2,3,4,5,6,7]
print(l)
l2=swap_odd_even_index(l,0,len(l)-1)
print(l2) """

#find the second largest number in list:
""" def second_max(l):
  m=max(l)
  sm=None
  for i in l:
        if i!=m:
          if sm==None :
             sm=i
            # print(sm)
          else :
              sm= sm if sm>i else i
  return sm
l=[1,3,9,5,45,6,9,1]
# print(max(l))
print(second_max(l)) """

#Left Rotated  a lift by one
#input  [1,2,3,4,5]
#output [2,3,4,5,1]
#metho1
""" l=[1,2,3,4,5]
l2=l[1:]+l[0:1]
print(l2) """
#method2
""" l=[1,2,3,4,5]
l.append(l.pop(0))
print(l) """
#own implement
""" def leftRotateByone(l):
  n=len(l)
  x=l[0]
  for i in range(1,n):
    l[i-1]=l[i]
  l[n-1]=x
  return l
print(leftRotateByone([1,2,3,4,5])) """

#Right Rotated  a lift by one
#input  [1,2,3,4,5]
#output [5,1,2,3,4,5,]

#methos1
""" l=[1,2,3,4,5]
l2=l[-1:-2:-1]+l[0:len(l)-1]#l[-1:-2:-1] -->exact the last element as list
print(l2) """
#methood2
""" l=[1,2,3,4,5]
l.insert(0,l.pop(-1))#remove the last element by pop () whic return the remeved element and inser the elemt at fist of list usinh insert,because append applicable for list,u are inserting a list
print(l) """
#method3 own implementation
""" def rightRotateByone(l):
   n=len(l)
   x=l[n-1]
   l2=[]
   #in the reverse manner we have to call 4,3,2,1
   for i in range(n-1,0,-1):
         print(i)
         l[i]=l[i-1]
   l[0]=x
   return l
print(rightRotateByone([1,2,3,4,5])) """

#17) left rotate a list by 'd' places
#v1
""" l=[1,2,3,4,5,6,7,8]
p=int(input("no of places to rotate:"))
l= l[p:]+l[:p]#p alcess to last
print(l) """
#v2
""" from collections import deque
l=[1,2,3,4,5,6,7,8]
d=3
dq=deque(l)
dq.rotate(-d)#-d left direction
print(list(dq)) """
#v3
""" def leftRotateNplace(L,p):
   for i in range (0,p):
    L.append(L.pop(0)) #pop(0) will remove for each iteration in list ,and append will add element every iteration
   return L
l=[1,2,3,4,5,6,7,8]
print(leftRotateNplace(l,3)) """

#17) lRight  rotate a list by 'd' places
""" l=[1,2,3,4,5,6,7,8]
p=int(input("no of places to rotate giht:"))
l= l[len(l)-p:]+l[:len(l)-p]#p alcess to last
print(l) """
#v2
""" def RightRotateNplace(L,p):

   for i in range (0,p):
    L.insert(0,L.pop(-1)) #pop() will remove last element for each iteration in list ,and insert will add element at first every iteration
   return L
l=[1,2,3,4,5,6,7,8]
print(RightRotateNplace(l,2)) """
"""
#-------------------------
#Given a list of size n and return an element's position which appears greater than n/2 times.

L = [8, 3, 4, 8, 8] ---> n=5/2=2 output: 0 or 3 or 4 --> 8
L = [8, 7, 6, 8, 6, 6, 6, 6] --> n=8/2=4 output: 2 or 4 or 5 or 6 or 7 --> 6
L = [3, 7, 4, 7, 7, 5] ----> n=6/2=3 output: -1 
"""
"""
def fun(L):
   n=len(L)
  for i in range(0,n):
    count=1
    for j in range(i+1,n):
          if L[i]==L[j]:
            # print(L[i],L[j])
            count=count+1
    #  print("c-",count)
    if count > n//2:
      return L[i]
  return -1
# L = [8, 7, 6, 8, 6, 6, 6, 6] --> n=8/2=4 output: 2 or 4 or 5 or 6 or 7 --> 6
print(fun([8, 7, 6, 8, 6, 6, 6, 6] ))     """      
