from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange
import requests
import toml

config = toml.load('.project_config')
tmdb_bearer = config['TMDB']['bearer_token']
headers = {
    "Authorization": f"Bearer {tmdb_bearer}"
}
tmdb_url = "https://api.themoviedb.org/3/"
tmdb_img_url = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SECRET_KEY'] = config['WTF']['secret_key']
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)

    def add_from_tmdb_json(self, movie_data:dict):
        self.title = movie_data['title']
        self.year = movie_data['release_date'][:4]
        self.description = movie_data['overview']
        self.img_url = tmdb_img_url + movie_data['poster_path']
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return '<Movie %r>' % self.title

class EditForm(FlaskForm):
    rating = DecimalField(label='Your Rating Out of 10 e.g. 7.5', 
                         validators=[DataRequired(),
                                     NumberRange(min=0, max=10)])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")



@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    ranking = len(all_movies)
    for movie in all_movies:
        movie.ranking = ranking
        # print(ranking)
        ranking -= 1

    # teacher has a commit here to write the ranking to the DB
    # is there any point to doing this when we recalculate everytime?
    # db.session.commit()
        
    return render_template("index.html", movies=all_movies)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        # print(tmdb_url+title)
        # No worry - the requests library url-encodes the string for us
        resp = requests.get(tmdb_url+"search/movie?query="+title, 
                            headers=headers).json()
        results = resp['results']
        # print(resp)
        return render_template('select.html', movies=results)
    else:
        if id := request.args.get('tmdb_id'):
            resp = requests.get(tmdb_url+"movie/"+id, headers=headers).json()
            movie = Movie()
            movie.add_from_tmdb_json(resp)
            return redirect(url_for('edit', id=movie.id))
        else:
            return render_template('add.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    movie = Movie.query.get_or_404(id)
    form = EditForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    else:
        form.rating.render_kw={"placeholder":f"{movie.rating}"}
        form.review.render_kw={"placeholder":f"{movie.review}"}
        return render_template('edit.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))
   

if __name__ == '__main__':
    app.run(debug=True)
