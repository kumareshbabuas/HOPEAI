#!/usr/bin/env python
# coding: utf-8

# #print 0 to 20 by using range

# In[1]:


for num in range(0,20):
    print(num)


# #print range 10 to 20
# The print method takes an extra parameter end=" " to keep the pointer on the same line.
# 
# The end parameter can take certain values such as a space or some sign in the double quotes to separate the elements printed in the same line.

# In[2]:


for num in range(10,20):
    print(num,end=" ")


# #print number of items in the list by using 'len'
# To determine how many items a list has, use the len() function:

# In[3]:


lists =[10,20,14,55,43,87,76]
print(lists)
print("Number of item in the List2:", len(lists))


# In[4]:


#print words 


# In[5]:


AI = "Artificial Intelligence"
print(AI)
for w in AI:
    print(w)


# In[6]:


print("-Your Name-")
print("-Your Age-")
print("-Your Profession-")


# #print Tuples
# 
# In Python, tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses for grouping the data sequence.
# Note: Creation of Python tuple without the use of parentheses is known as Tuple Packing. 
# 
# #print this mixered datatype using Tuples

# In[7]:


tuples = [1, "Welcome", 2,  "Hope"]
print (tuple(tuples))


# #print nested tuples

# In[8]:


tuple1 = (0,1,2,3)
tuple2 = ('python', "HOPE")
tuples = (tuple1, tuple2)
print(tuples)


# #pring odd numbers in the list

# In[9]:


oddNumbers = (20,10,16,19,25,1,276,188)
print(oddNumbers)
for odd in oddNumbers:
    if(odd%2==1):
        print(odd,"is odd")


# #print Even number in the list

# In[10]:


evenNumbers = (20,10,16,19,25,1,276,188)
for even in oddNumbers:
    if(even%2==0):
        print(even,"is Even")


# In[ ]:




