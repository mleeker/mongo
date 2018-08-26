
# coding: utf-8

# NASA Mars News

# In[1]:


from splinter import Browser
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[2]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[5]:


news_title = soup.find("div", class_="content_title").text
news_para = soup.find("div", class_="article_teaser_body")
print(f"Title: {news_title}")
print(f"Para: {news_para}")


# JPL Mars Space Images - Featured Image

# In[6]:


image_url ="https://jpl.nasa.gov/spaceimages/?"
browser.visit(image_url)


# In[7]:


from urllib.parse import urlsplit
base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(image_url))
print(base_url)


# In[8]:


img_path = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"


# In[9]:


results = browser.find_by_xpath(img_path)
img = results[0]
img.click()


# In[11]:


image_html = browser.html
soup = BeautifulSoup(image_html, "html.parser")
img_url = soup.find("img", class_="fancybox-image")["src"]
full_image_url = base_url + img_url
print(full_image_url)


# Mars Weather Twitter

# In[12]:


twitter_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(twitter_url)


# In[13]:


twitter_html = browser.html
soup = BeautifulSoup(twitter_html, "html.parser")
weather_tweet = soup.find("p", class_="js-tweet-text").text
print(weather_tweet)


# Mars Facts

# In[14]:


facts_url = 'https://space-facts.com/mars/'


# In[15]:


facts_table = pd.read_html(facts_url)
facts_table[0]


# In[16]:


mars_table_df = facts_table[0]
mars_table_df.columns = ["Parameter", "Values"]
mars_table_df


# In[17]:


mars_table_html = mars_table_df.to_html()
mars_table_html = mars_table_html.replace("\n", "")
mars_table_html


# Mars Hemispheres

# In[18]:


hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemisphere_url)


# In[19]:


hemisphere_url = browser.html
soup = BeautifulSoup(hemisphere_url, "html.parser")

results = soup.find('div', class_="collapsible results")
hemispheres = results.find_all('a')

hemisphere_image_urls = []

for a in hemispheres:
    title = a.h3
    link = "http://astrogeology.usgs.gov" + a["href"]
    
    browser.visit(link)
    
    image_page = browser.html
    results = BeautifulSoup(image_page, "html.parser")
    image_link = results.find("div", class_="downloads").find('li').a['href']
    
    image_dict = {}
    image_dict["title"] = title
    image_dict['image_url'] = image_link
    
    hemisphere_image_urls.append(image_dict)
print(hemisphere_image_urls)

