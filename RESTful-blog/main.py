from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from sqlalchemy import desc
from datetime import date


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def populate_from_form(self, form:CreatePostForm):
        self.title = form.title.data
        self.subtitle = form.subtitle.data
        self.author = form.author.data
        self.img_url = form.img_url.data
        self.body = form.body.data

    def create_form(self):
        form = CreatePostForm(
            title = self.title,
            subtitle = self.subtitle,
            img_url = self.img_url,
            author = self.author,
            body = self.body
        )
        return form



@app.route('/')
def get_all_posts():
    posts = BlogPost.query.order_by(desc(BlogPost.id)).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get_or_404(post_id)
    print(requested_post.body)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    requested_post = BlogPost.query.get_or_404(post_id)
    form = requested_post.create_form()
    if form.validate_on_submit():
        requested_post.populate_from_form(form)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    else:
        return render_template('make-post.html', form=form)
    

@app.route('/new-post', methods=['GET', 'POST'])
def add():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = BlogPost()
        post.populate_from_form(form)
        # add today's date
        dt = date.today()
        post.date = f'{dt:%B} {dt.day}, {dt.year}'
        # save new post
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    else:
        return render_template('make-post.html', form=form)
    
@app.route('/delete/<int:post_id>')
def delete(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)