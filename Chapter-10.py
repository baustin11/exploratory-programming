
# coding: utf-8

# In[1]:

from textblob import TextBlob


# In[2]:

gravity = TextBlob("A screaming comes across the sky.")


# In[3]:

gravity.words


# In[4]:

TextBlob("A screaming comes across the sky.").words


# In[5]:

len(gravity.words)


# In[6]:

gravity.words[:3]


# In[7]:

gravity.tokens


# In[8]:

TextBlob("Can't touch this.").tokens


# In[9]:

TextBlob("Cannot touch this.").tokens


# In[10]:

pride = TextBlob("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.")


# In[11]:

pride.tags


# In[27]:

def adjs(pride):
    count = 0
    for (word, tag) in pride.tags:
        if tag == "JJ":
            count = count + 1
    return count


# In[28]:

adjs(pride)


# In[29]:

adjs(gravity)


# In[30]:

hr = TextBlob("All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.")


# In[31]:

hr.sentences


# In[32]:

len(hr.sentences)


# In[101]:

source = open("pg1342.txt")
pride = source.read()


# In[102]:

source.close()


# In[119]:

source = open("pg2701.txt")
moby = source.read()


# In[121]:

source.close()


# In[122]:

moby[:10]


# In[123]:

moby = moby[2:]


# In[124]:

moby[:10]


# In[52]:

pride[:10]


# In[53]:

prideblob = TextBlob(pride)


# In[125]:

mobyblob = TextBlob(moby)


# In[138]:

TextBlob("This movie was a great experience, and not disappointing.").sentiment


# In[139]:

TextBlob("This movie was not a great experience, and disappointing.").sentiment


# In[127]:

from textblob import Word
bank_word = Word("bank")
bank_word.synsets


# In[128]:

bank1 = bank_word.synsets[0]
bank1.lemma_names()


# In[129]:

bank_word.synsets[1].lemma_names()


# In[130]:

bank3 = bank_word.synsets[2]
bank3.lemma_names()
bank1.lemma_names() == bank3.lemma_names()


# In[131]:

bank1 == bank3


# In[132]:

from textblob.wordnet import NOUN
bank_word.get_synsets(NOUN)


# In[133]:

car_word = Word("car")
car_word.get_synsets(NOUN)


# In[134]:

car1 = car_word.get_synsets(NOUN)[0]
car1.definition()


# In[135]:

car1.hypernyms()


# In[136]:

car1.hypernyms()[0]


# In[137]:

car1hypernyms()[0].lemma_names()


# In[ ]:



