from pygooglenews import GoogleNews

# top news
def top_news():
    google_news = GoogleNews(country='et')
    et_news = google_news.top_news()
    return [[news['title'],news['link']] for news in et_news['entries']]
