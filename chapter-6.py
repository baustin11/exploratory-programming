
# coding: utf-8

# In[1]:

len ("hello world")


# In[2]:

len ("2112")


# In[3]:

len ("0")


# In[4]:

hi = "hello world"


# In[5]:

len(hi)


# In[6]:

'hello'[0]


# In[7]:

"hello world"[0:2]


# In[8]:

"2112" [0:3]


# In[9]:

'hello' [0:1]


# In[10]:

"hello world" [0:500]


# In[11]:

"hello world" [450:500]


# In[12]:

"hello world" [:3]


# In[13]:

"hello world" [1:]


# In[14]:

"hello world" [6:]


# In[15]:

"abcdefgh" [::2]


# In[16]:

"123456789" [::2]


# In[17]:

"hello world " [-2:]


# In[18]:

wyatt = "They flee from me that sometime did me seek / With naked foot, stalking in my chamber."


# In[19]:

wyatt = wyatt.lower()
wyatt


# In[20]:

for c in wyatt:
    print c


# In[21]:

for i in range(len(wyatt)):
    print wyatt[i]


# In[22]:

for i in range (len(wyatt)):
    print i, wyatt[i]


# In[23]:

for i in range(len(wyatt)):
    print wyatt[i:i+2]


# In[24]:

pair = 0
for i in range(len(wyatt)):
    if wyatt[i:i+2] == "ee":
        pair = pair + 1


# In[25]:

pair


# In[26]:

pair = 0
for i in range(len(wyatt)):
    if wyatt[i] == wyatt[i+1]:
        pair = pair + 1


# In[27]:

pair


# In[28]:

pair = 0 
for i in range(len(wyatt)-1):
    if wyatt [i] == wyatt[i+1]:
        pair = pair + 1


# In[29]:

pair


# In[ ]:



