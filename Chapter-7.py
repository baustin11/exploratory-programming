
# coding: utf-8

# In[1]:

list("rotor")


# In[2]:

to_test = list("rotor")


# In[3]:

to_test.reverse()


# In[4]:

test = ["a", "b", "c"]
test.reverse()
test


# In[5]:

word = "hierarchy"
backlist = list(word)


# In[6]:

backlist


# In[7]:

backlist.reverse()
backlist


# In[8]:

word
list(word)


# In[9]:

def pal(word):
    backlist = list(word)
    backlist.reverse()
    word == backlist


# In[10]:

original = "Civic"
string = original.lower()
string[0]


# In[11]:

string[-1]


# In[12]:

string[0] == string[-1]


# In[13]:

right = -1
pal = True
for letter in string:
    pal = (pal and (letter == string[right]))
    right = right - 1


# In[14]:

right = -1 pal = True
for letter in string:
    pal = (pal and (letter == string[right]))
    pring letter + string[right] + ': ' + str(letter == string[right])
    right = right - 1


# In[15]:

def pal (text):
    return text.lower() == text[::-1].lower()


# In[27]:

source = open("pg1342.txt")
pride = source.read()
print pride[:1000]


# In[34]:

import re


# In[35]:

result = re.findall("[AEIOUaeiou]", pride)


# In[36]:

len(result)


# In[37]:

result


# In[38]:

result[:20]


# In[39]:

quotes = re.findall('"[^"]*\r\n\r\n|"[^"]*"', pride)


# In[40]:

len(quotes)


# In[41]:

quotes[:10]


# In[43]:

pride_words = pride.split()


# In[44]:

len(pride_words)


# In[45]:

pride_words_2 = re.findall('[A-Za-z]+', pride)
len(pride_words_2)


# In[ ]:



