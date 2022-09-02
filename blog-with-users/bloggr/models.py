from sqlalchemy import desc
from sqlalchemy.orm import relationship
import requests
import click
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from datetime import datetime

from bloggr import db


##CONFIGURE TABLES

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    @staticmethod
    def get_posts(by_author:str = None) ->list['BlogPost']:
        if by_author:
            return BlogPost.query.filter_by(name=by_author).order_by(desc(BlogPost.id)).all()
        else:
            return BlogPost.query.order_by(desc(BlogPost.id)).all()
    

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = relationship("BlogPost", back_populates="author")

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
    
#Lines below only required once, when creating DB. 
# db.drop_all()
# db.create_all()

# import some blog posts
def load_posts():
    db.drop_all()
    db.create_all()

    blog_url = 'https://theclementsfirm.com//wp-json/wp/v2/posts'
    resp = requests.get(blog_url)
    resp.raise_for_status()
    post_json = resp.json()

    noah = User(
        email="noahclements@gmail.com",
        name="Noah Clements",
        password=generate_password_hash("BubbaLubba1!", salt_length=8)
    )
    db.session.add(noah)
    db.session.commit()
    caroline = User(
        email="clementscaroline@yahoo.com",
        name="Caroline Clements",
        password=generate_password_hash("BubbaLubba2!", salt_length=8)
    )
    db.session.add(noah)
    db.session.commit()

    authors = {
        caroline.name: caroline,
        noah.name: noah
    }
    
    for post in post_json:
        img = post['uagb_featured_image_src']['full']
        if img:
            img_0 = img[0]
        else:
            img_0 = ''

        if (subtitle:=post['uagb_excerpt']) is None:
            subtitle = ""

        author = authors[post['uagb_author_info']['display_name']]
            
        blog_post = BlogPost(
            id=int(post['id']),
            author_id=author.id,
            author=author,
            title=post['title']['rendered'],
            subtitle=subtitle,
            date=datetime.strptime(post['date'], "%Y-%m-%dT%H:%M:%S").strftime("%B %d, %Y"),
            body=post['content']['rendered'],
            img_url=img_0
        )
        try:
            db.session.add(blog_post)
            db.session.commit()
        except:
            pass
# only need to do this on first load, if dropped and created tables.    
# load_posts()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    load_posts()
    click.echo('Initialized the database.')

def init_app(app):
    # app.teardown_appcontext(db.session.close_db)
    app.cli.add_command(init_db_command)