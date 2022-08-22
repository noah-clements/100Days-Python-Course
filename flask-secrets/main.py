from flask import Flask, render_template
import toml
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    config = toml.load('.project_config')
    secret_key = config['WTF']['secret-key']
    app.config['SECRET_KEY'] = secret_key
    return app

class LoginForm(FlaskForm):
    email = StringField(label='Email', 
                        validators=[DataRequired(), 
                                    Email(message='Please enter a valid email address',
                                        check_deliverability=True),
                                    Length(min=6, max=30)])
    password = PasswordField(label='Password', 
                             validators=[DataRequired(), Length(min=8, max=30)])
    submit = SubmitField('Login')

app = create_app()

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)