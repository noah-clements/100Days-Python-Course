import requests
from datetime import datetime
from main import User, BlogPost, db

blog_url = 'https://theclementsfirm.com//wp-json/wp/v2/posts'

def load_posts():
    resp = requests.get(blog_url)
    resp.raise_for_status()
    post_json = resp.json()

    author = User.query.get(1)
    for post in post_json:
        post = BlogPost(
            author_id=1,
            author=author,
            title=post['title']['rendered'],
            subtitle=post['uagb_excerpt'],
            date=datetime.strptime(post['date'], "%Y-%m-%dT%H:%M:%S").strftime("%B %d, %Y"),
            body=post['content']['rendered'],
            img_url=post['uagb_featured_image_src']['full']['0']
        )

    