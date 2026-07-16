from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Ensure it is defined in your .env file or as an environment variable.")

client = OpenAI(api_key=api_key)

def generate_linkedin_post(article):
    prompt = f"""
You are an AI Product Strategist.

News:
Title: {article['title']}
Summary: {article['summary']}

Write a LinkedIn post:
- Explain what happened
- Why it matters for business
- Product strategy insight
- Strong opinion
- End with discussion question

Tone: Insightful, consulting-style.
Length: 250 words.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a strategic AI product consultant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content