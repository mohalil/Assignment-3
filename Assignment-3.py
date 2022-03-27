#!/usr/bin/env python
# coding: utf-8

# In[1]:


def value_1(*values):
    count=0
    for i in values:
        count+=i
    return count
print(value_1(8, 2, 3, 0, 7))


# In[2]:


str = "1234abcd"
str[::-1]


# In[3]:


def letters(words):
    d={"upper":0,"lower":0}
    for c in words:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            "okay"
    print("No. of Upper case characters :",d["upper"])
    print("no. of Lower case characters :",d["lower"])
letters( 'The quick Brow Fox')


# In[ ]:




