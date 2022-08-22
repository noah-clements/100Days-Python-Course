from flask import Flask, render_template
import random
from datetime import date
import requests
# import json
app = Flask(__name__)

@app.route('/')
def hello():
    rand_number = random.randint(1, 10)
    this_year = date.today().year
    return render_template("index.html", num=rand_number, current_year = this_year)

@app.route('/guess/<name>', methods=['GET', 'POST'])
def guess_name_info(name:str):
    age_url = f"https://api.agify.io/?name={name}"
    gender_url = f"https://api.genderize.io/?name={name}"
    resp = requests.get(age_url)
    resp.raise_for_status()
    age_json = resp.json()
    age = age_json['age']

    resp = requests.get(gender_url)
    resp.raise_for_status()
    gender_json = resp.json()
    gender = gender_json['gender']

    this_year = date.today().year

    return render_template('guess.html', name=name, age=age, gender=gender, current_year = this_year)

@app.route('/blog')
def display_blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'

    resp = requests.get(blog_url)
    resp.raise_for_status()
    # print(resp.content)
    all_posts = resp.json()

    return render_template('blog.html', posts=all_posts)
    

if __name__ == '__main__':
    app.run(debug=True)