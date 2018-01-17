
# coding: utf-8

# In[2]:

def set_a():
    a = 10
    print 'The value of a:', a


# In[3]:

set_a()


# In[7]:

a = 20
print 'Initially, the value of a:', a
set_a()
print 'finally, the value of a:', a


# In[8]:

def scoped (first, second):
    third = second + second - first
    return third
first = 10
second = 11
third = 12
scoped(2,4)


# In[9]:

first


# In[10]:

second


# In[11]:

third


# In[ ]:



