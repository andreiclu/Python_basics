#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.storia.ro/vanzare/casa/iasi/iasi/?search%5Bfilter_float_price%3Ato%5D=150000")
c = r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div",{"class":"offer-item-details"})


all[0].find("li",{"class":"offer-item-price"}).text.replace("\n","").replace(" ","")

last_page = soup.find("ul", {"class": "pager"})
li = soup.find('ul', class_='pager')
pages = [a.text for a in li.find_all('li')]
l_page = pages[-2]
print (l_page)


# In[2]:


l = []
base_url = "https://www.storia.ro/vanzare/casa/iasi/iasi/?search%5Bfilter_float_price%3Ato%5D=150000&search%5Border%5D=created_at_first%3Adesc&page="
for page in range(1, int(l_page+1)):
    print(base_url+str(page))
    r=requests.get(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c, "html.parser")
    all = soup.find_all("div",{"class":"offer-item-details"})
    for item in all:
        d = {}
        d["Price"] = item.find("li",{"class":"offer-item-price"}).text.replace("\n","").replace(" ","")
        d["Description"] = item.find_all("span",{"class", "offer-item-title"})[0].text
        d["Rooms"] = item.find("li",{"class", "offer-item-rooms hidden-xs"}).text
        try:
            d["Build Area"] = item.find_all("li", {"class", "hidden-xs offer-item-area"})[0].text
        except:
            d["Build Area"] = None
        try: 
            d["Land Area"] = item.find_all("li", {"class", "hidden-xs offer-item-area"})[1].text
        except:
            d["Land Area"] = None
        for column_group in item.find_all("p", {"class": "text-nowrap"}):
            d["Location"] = (column_group.text)

        l.append(d)
    
    


# In[3]:


import pandas
df = pandas.DataFrame(l)
df

