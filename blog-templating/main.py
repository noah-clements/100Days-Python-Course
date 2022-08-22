from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
posts = []
blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'

resp = requests.get(blog_url)
resp.raise_for_status()
post_json = resp.json()

for entry in post_json:
    posts.append(Post(entry['id'], entry['title'], entry['subtitle'], entry['body']))

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:post_id>')
def read_post(post_id):
    requested_post = None
    for post in posts:
        if post.id == post_id:
            requested_post = post
            break
    return render_template('post.html', post=requested_post)
    

if __name__ == "__main__":
    app.run(debug=True)
