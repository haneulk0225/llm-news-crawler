import feedparser

def search_news(keyword: str):
    
    url = f"https://news.google.com/rss/search?q={keyword}&hl=ko&gl=KR&ceid=KR:ko"

    feed = feedparser.parse(url)

    articles = []

    for item in feed.entries[:10]:

        articles.append( {
            "title": item.title,
            "link": item.link
        })

    return {
        "keyword": keyword,
        "count": len(articles),
        "articles": articles
    }