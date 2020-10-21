#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.select('#rightdown')
print(data1)


# In[2]:


data2 = data1[0].find_all('div', {'class':'contents_box02'})


# In[3]:


data3 = data2[2].find_all('div', {'class':'ball_tx ball_yellow'})


# In[4]:


print("開出順序:",end="")
for n in range(0,6):
    print(data3[n].text,end="   ")


# In[5]:


print("\n大小順序:",end="")
for n in range(6,len(data3)):
    print(data3[n].text,end="   ")


# In[6]:


red = data2[2].find('div', {'class':'ball_red'})
print("\n特別號:{}".format(red.text))


# In[ ]:




