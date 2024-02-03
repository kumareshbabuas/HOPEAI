#!/usr/bin/env python
# coding: utf-8

# #print 'CORRECT' if i = 10

# In[1]:


value = int(input("value: "))
if(value == 10):
    print("Correct")
else:
    print("Not Correct")


# #chck the password, using if and else

# In[2]:


pwd = input("Enter the password: ")
if (pwd == 'HOPE@123'):
    print("Your password is correct")
else:
     print("Your password is wrong")


# #Category the people by their age like children, adult, citizen, senior citizen

# In[3]:


age = int(input("age: "))

if(age < 18):
    print ("Children")
elif(age < 35):
    print ("Adult")
elif (age < 59):
    print ("Citizen")  
else:
    print("Senior Citizen")


# #Find whether given number is Positive or negative

# In[4]:


numb = float(input("Enter any number: "))
if (numb > 0):
    print("No. is positive")
else:
    print("No.is negative")


# #check whether the given number is divisible by 5

# In[5]:


numb = float(input("Enter a number to check: "))
if(numb % 5 == 0):
    print("No. is divisible by 5")
else:
    print("No. is not divisible by 5")


# In[ ]:




