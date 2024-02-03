#!/usr/bin/env python
# coding: utf-8

# #Assignment-1-Baby Steps Control Structures

# In[15]:


print("Welcome to Assignment-1")


# In[16]:


Num1 = 10
Num2 = 30
Add = 40
print("Num1= ", Num1)
print("Num2= ", Num2)
print ("Add= ", Add)


# #Body Mass Index
# Underweight: BMI less than 18.5
# Normal weight: BMI of 18.5 to 24.9
# Overweight: BMI of 25 to 29.9
# Very OverWeight: BMI of 30 or higher

# In[17]:


BMIIndex = float(input("Enter the BMI Index: "))
if BMIIndex <= 18.5:
    print("Under Weight")
elif (BMIIndex > 18.5 and BMIIndex <= 24.9):
    print("Normal Weight")
elif (BMIIndex > 24.9 and BMIIndex <= 29.9):
    print("OverWeight")
else:
    print("Very OverWeight")

