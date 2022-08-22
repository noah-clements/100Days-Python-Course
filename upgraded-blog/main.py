from flask import Flask, render_template, request
import requests
from datetime import datetime
import toml
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

blog_url = 'https://theclementsfirm.com//wp-json/wp/v2/posts'

resp = requests.get(blog_url)
resp.raise_for_status()
post_json = resp.json()

config = toml.load(".project_config")

email = config['Email']['address']
pwd = config['Email']['pwd']
smtp = config['Email']['smtp']
port = config['Email']['port']

@app.template_filter("format_date")
def format_date(datetime_string):
    dt = datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%S")
    return dt.strftime("%B %d, %Y")

@app.route('/')
@app.route('/home')
@app.route('/index.html')
def home():
    return render_template("index.html", posts=post_json)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<int:post_id>')
def post(post_id):
    requested_post = None
    for post in post_json:
        if post_id == int(post['id']):
            requested_post = post
    return render_template("post.html", post=requested_post)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data['name'])
        print(data['email'])
        print(data['phone'])
        print(data['message'])
        email_msg = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        send_email(email_msg)
        return render_template('contact.html', userInput = data)
    else:    
        return render_template("contact.html")

def send_email(msg_content):
    # Set up email
    msg = EmailMessage()
    msg['Subject'] = "New Contact Message from Blog!"
    msg['From'] = email
    msg['bcc'] = email
    msg.set_content(msg_content)

    with smtplib.SMTP(smtp, port=port) as connection:
        connection.starttls()
        connection.login(email, password=pwd)
        connection.send_message(msg)

    


if __name__ == '__main__':
    app.run(debug=True)