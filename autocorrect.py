#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pyspellchecker')


# In[8]:


from spellchecker import SpellChecker

spell = SpellChecker()

text = "To qualify for a competitive programmingg."

dict_of_autocorrect_words = {}
for i in spell.unknown(text.split()):
    dict_of_autocorrect_words[i] = spell.correction(i)

print(f'The AUTOCORRECT suggestions are Mis-spelled words are {dict_of_autocorrect_words}')

temp = text.split()
res = []
for wrd in temp:
      
    res.append(dict_of_autocorrect_words.get(wrd, wrd))
      
res = ' '.join(res)

print(res)


# In[ ]:




