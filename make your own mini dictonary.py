#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
# 
# 

# In[1]:


x=input("Enter a character is: ")
dict = { }
for x in range(ord('a'),ord('z')+1):
    dict[chr(x)] = x
print(dict,end=" ") 


# In[ ]:





# In[ ]:




