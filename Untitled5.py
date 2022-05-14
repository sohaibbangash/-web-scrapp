#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[5]:


page = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
page.status_code


# In[6]:


soup = BeautifulSoup(page.content,"html.parser")

print(soup. prettify) 


# In[7]:


for heading in soup.find_all(["h1","h2","h3"]):
    print(heading.name+''+heading.text.strip())


# In[8]:


h2_tags = soup.find_all("h2")
print(h2_tags)


# In[11]:


p_tags = soup.find(id="mw-content-text").find_all("p",limit=9)
p_tags


# In[18]:


all_data = {"p Tags":p_tags, "h2_Tags":h2_tags}
print(all_data)


# In[19]:


print(len(h2_tags))
print(len(p_tags))


# In[ ]:


df = pd.DataFrame(all_data)
df.to_csv

