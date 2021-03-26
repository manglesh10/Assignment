#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to print "Hello Python"?

# In[4]:


print ("Hello Python")


# 2.	Write a Python program to do arithmetical operations addition and division.?
# 

# In[6]:


a=4
b=6
print(a+b)


# 3.	Write a Python program to find the area of a triangle?

# In[13]:


a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

s = (a + b + c) / 2
import math
area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
print("The Area of a Triangle is %0.2f" %area)
   


# 4.	Write a Python program to swap two variables?

# In[33]:


a=input("Enter number: ")
b=input("Enter second number: ")

temp = a 
a= b
b= temp
s
print("The value of a after swapping is" ,a)
print("The value of b after swapping is" ,b)


# 5.	Write a Python program to generate a random number?

# In[49]:


import random
n = random.randint(0,100)
print(n)

