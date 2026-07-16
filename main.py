from news_fetcher import fetch_trending_ai_news
from content_generator import generate_linkedin_post
from linkedin_poster import save_draft

# Fetch articles, generate LinkedIn posts, and save drafts
articles = fetch_trending_ai_news(limit=3)

for article in articles:
    post = generate_linkedin_post(article)
    save_draft(post)


