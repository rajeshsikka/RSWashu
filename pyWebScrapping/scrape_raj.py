
# coding: utf-8

# ### NASA Mars News

# Dependencies
from bs4 import BeautifulSoup
import requests
from selenium import webdriver 
from splinter import Browser
import pandas as pd


def scrape():

    """ Function: Main scrape functionality

        Calls other functions

        Parameters: None

        Returns: combined mars_data dictionary """


# Defines Mars data collection in a dictionary
    mars = {}

    mars["mars_news"] = marsNewsData()

    mars["featured_image_url"] = marsFeaturedImageURL()

    mars["mars_weather_tweet"] = marsWeather()

    mars["mars_facts_table"] = marsFacts()

    mars["hemispheres_url_info"] = marsHemisphereImageURLs()

# return mars_info dict
    print("mars", mars)
    return mars
    
#-------------------------------------------------------------------
#Scarpe the Mars news website to obtain the title and description.
#-------------------------------------------------------------------

def marsNewsData():
    mars_news = {}
    news_title = []
    news_description = []

# URL of page to be scraped
    url = 'https://mars.nasa.gov/news'

# Retrieve page with the requests module
    page = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(page.content, 'html.parser')

# capture the content title from the Mars website 
    results = soup.find_all("div", class_="content_title")

# Loop through returned results

    for result in results:   
        title = result.a
        title = title.text.strip()
        news_title.append(title)

# capture the description from the Mars website 
    results = soup.find_all("div", class_="rollover_description_inner")

# Loop through returned results and do the necessary concatination for title and description

    for result in results:
        desc = result.get_text().strip()
        news_description.append(desc)
    
    for i in range(1):
        mars_news["news_title"] = news_title[i]
        mars_news["news_description"] = news_description[i]     
    
    
    return mars_news

# ### JPL Mars Space Images - Featured Image

def marsFeaturedImageURL():

    browser = Browser('chrome', headless=False)
    jpl_search_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    jpl_full_size_url = 'https://photojournal.jpl.nasa.gov/jpeg/'    


    browser.visit(jpl_search_url) 
    jpl_search_html = browser.html

# Create BeautifulSoup object; parse with 'html.parser'
    jpl_img_soup = BeautifulSoup(jpl_search_html, 'html.parser')

    img_results = jpl_img_soup.find_all("a", class_="button fancybox")

#Loop through the image results to get the actual results (in this particular case its only one)

    for image in img_results:
        featured_image = image.get('data-link')

    featured_image_url = jpl_full_size_url + featured_image
    featured_image = featured_image.split('=')
    featured_image_url = jpl_full_size_url + featured_image[1] + '.jpg'
    
    browser.quit()  

    return featured_image_url

# ### Mars Weather
def marsWeather():

    browser = Browser('chrome', headless=False)
    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(mars_weather_url) 
    mars_weather_html = browser.html

# Create BeautifulSoup object; parse with 'html.parser'
    mars_weather_soup = BeautifulSoup(mars_weather_html, 'html.parser')
    mars_weather_tweet = mars_weather_soup.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")

    tweet_message = []

    for weather_tweet in mars_weather_tweet:
        twt_msg = weather_tweet.get_text().strip()
        tweet_message.append(twt_msg)

    browser.quit()
    return tweet_message[2]

# ### Mars Facts

def marsFacts():
    url = 'http://space-facts.com/mars/'
    tables = pd.read_html(url)

# Storing the results read html table into a data frame. 
    df = tables[0]   
    mars_facts_table = df.to_html(header=False, index=False)

    return mars_facts_table

# ### Mars Hemispheres

def marsHemisphereImageURLs():

    browser = Browser('chrome', headless=False)
    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(mars_hemispheres_url) 
    mars_hemispheres_html = browser.html

# Create BeautifulSoup object; parse with 'html.parser'
    mars_hemispheres_soup = BeautifulSoup(mars_hemispheres_html, 'html.parser')

    hemispheres_url_info = []

    products = mars_hemispheres_soup.find('div', class_='result-list')
    hemispheres = products.find_all('div', class_='item') 

    for hemisphere in hemispheres: 
        title = hemisphere.find('div', class_='description')
        title_text = title.a.text
        title_text = title_text.replace(' Enhanced', '')
    
        browser.click_link_by_partial_text(title_text)                          
    
        mars_hemispheres_html  = browser.html                                    
        mars_hemispheres_soup = BeautifulSoup(mars_hemispheres_html, 'html.parser')                                 
    
        image = mars_hemispheres_soup.find('div', class_='downloads').find('ul').find('li')  
        img_url = image.a['href']
    
        hemispheres_url_info.append({'title': title_text, 'img_url': img_url}) 
    
        browser.click_link_by_partial_text('Back')                               

    browser.quit()

    return hemispheres_url_info

if __name__ == "__main__":

    print(scrape())

