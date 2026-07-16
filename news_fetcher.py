import feedparser

AI_FEEDS = [
    "https://openai.com/blog/rss.xml"
]

def fetch_trending_ai_news(limit=5):
    articles = []

    for feed_url in AI_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:limit]:
            articles.append({
                "title": entry.title,
                "summary": entry.summary,
                "link": entry.link
            })

    return articles[:limit]