#!/usr/bin/env python
# coding: utf-8

# In[84]:


import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup as bs
import pdfkit


# In[117]:


headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '^\\^Google',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://the-ken.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://the-ken.com/all-stories/',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'action': 'my_wp_login',
  'data': 'email=badalutubemsc%40gmail.com&password=utubemusic'
}
s = requests.session()
response = s.post('https://the-ken.com/wp-admin/admin-ajax.php', headers=headers, data=data)
print("logged in successfully",response)


# In[118]:


headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
}
response = s.get('https://the-ken.com/all-stories/', headers=headers)
print("stories called : ",response)


# In[119]:


soup = bs(response.content, 'html.parser')
# print(soup.prettify())


# In[120]:


articles_links=[]
articles_titles =[]
mydivs = soup.find_all("div", {"class": "stories-card"})
for text in mydivs:
    download = text.find_all('a')
    for text in download:
        hrefText = (text['href'])
        articles_links.append(hrefText)
    download = text.find_all('h3',{"class": "article-title"})
    for text in download:
#         hrefText = (text['href'])
        articles_titles.append(text.get_text())


response = s.get(articles_links[1])


# In[122]:


soup = bs(response.content, 'html.parser')

for s in soup.find_all('div',{"class": "trending-main recent-sec gray-bg"}):
    s.extract()
for s in soup.find_all('div',{"class": "comments-wrapper"}):
    s.extract()
for s in soup.find_all('div',{"class": "col-md-3 offset-md-1 footer-col-5"}):
    s.extract()
for s in soup.find_all('div',{"class": "container footer-address"}):
    s.extract()
for s in soup.find_all('div',{"class": "col-md-2 footer-col-3"}):
    s.extract()
for s in soup.find_all('div',{"class": "container-fluid footer-strip"}):
    s.extract()
for s in soup.find_all('script'):
    s.extract()
# for s in test1.find_all('nav'):
#     s.extract()
# for s in test1.find_all('meta'):
#     s.extract()

# print(test1.prettify())


# In[130]:


# html_content = (soup.prettify())
# print(html_content)


# In[132]:


pdfkit.from_string(str(soup), 'out1.pdf')


# In[ ]:
