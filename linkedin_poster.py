import os
from datetime import datetime
import requests

def save_draft(content):
    if not os.path.exists("drafts"):
        os.makedirs("drafts")

    filename = f"drafts/post_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved draft: {filename}")

def post_to_linkedin(content):
    access_token = "YOUR_ACCESS_TOKEN"  # Replace with your LinkedIn API access token
    url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    payload = {
        "author": "urn:li:person:YOUR_PERSON_URN",  # Replace with your LinkedIn person URN
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Post successfully created on LinkedIn.")
    else:
        print("Failed to create post:", response.status_code, response.text)