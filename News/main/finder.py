from pygooglenews import GoogleNews
from newscatcher import Newscatcher
import requests

KEY = "d7e59f811066412d846f00c8217aa6c6"

# top news
def ethio_news():
    google_news = GoogleNews(country='et')
    et_news = google_news.top_news()
    return [{'title':news['title'],'link':news['link']} for news in et_news['entries']]

# world news
def world_news():
    url = f"https://newsapi.org/v2/everything?q=world&from=2022-05-18&sortBy=popularity&apiKey={KEY}"
    news = requests.get(url).json()
    return [{'title':news['title'],'link':news['url'], 'image': news['urlToImage']} for news in news['articles']]

# africa news
def africa_news():
    url = f"https://newsapi.org/v2/everything?q=Africa&from=2022-05-18&sortBy=popularity&apiKey={KEY}"
    news = requests.get(url).json()
    return [{'title':news['title'],'link':news['url'], 'image': news['urlToImage']} for news in news['articles']]

# europe news
def europe_news():
    url = f"https://newsapi.org/v2/everything?q=europe&from=2022-05-18&sortBy=popularity&apiKey={KEY}"
    news = requests.get(url).json()
    return [{'title':news['title'],'link':news['url'], 'image': news['urlToImage']} for news in news['articles']]