from pygooglenews import GoogleNews
from newscatcher import Newscatcher
import requests
from datetime import date

KEY = "d7e59f811066412d846f00c8217aa6c6"
today = date.today().strftime("%Y-%m-%d")
# top news
def ethio_news():
    google_news = GoogleNews(country='et')
    et_news = google_news.top_news()
    return [{'title':news['title'],'link':news['link']} for news in et_news['entries']]

# world news
def world_news():
    url = f"https://newsapi.org/v2/everything?q=world&from={today}&sortBy=popularity&apiKey={KEY}"
    news = requests.get(url).json()
    return [{'title':news['title'],'link':news['url'], 'image': news['urlToImage']} for news in news['articles']]

# africa news
def africa_news():
    url = f"https://newsapi.org/v2/everything?q=Africa&from={today}&sortBy=popularity&apiKey={KEY}"
    news = requests.get(url).json()
    return [{'title':news['title'],'link':news['url'], 'image': news['urlToImage']} for news in news['articles']]

# europe news
def europe_news():
    url = f"https://newsapi.org/v2/everything?q=europe&from={today}&sortBy=popularity&apiKey={KEY}"
    news = requests.get(url).json()
    return [{'title':news['title'],'link':news['url'], 'image': news['urlToImage']} for news in news['articles']]