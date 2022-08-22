from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    pwd = request.form['pwd']
    return f"Success!\n <h1>Name: {name}, Password: {pwd}</h1>"

if __name__ == '__main__':
    app.run(debug=True)