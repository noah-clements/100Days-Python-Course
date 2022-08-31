from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
# from sqlalchemy import IntegrityError

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Rh32u0hw3r!rGMc%'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['UPLOAD_FOLDER'] = "static/files"


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
        
    
#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        form = request.form
        user = User(
            name = form['name'],
            email = form['email'],
            password = generate_password_hash(form['password'], method='pbkdf2:sha256',
                                              salt_length=8) 
        )
        try:
            db.session.add(user)
            db.session.commit()
            login_user(user)
        except:
            flash(f"You already signed up with that email, log in instead!")
            return redirect(url_for('login')) 
        else:
            return redirect(url_for('secrets', name=user.name))
    else:
        return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        form = request.form
        user = User.query.filter_by(email=form['email']).first()
        if user is None:
            flash("That email does not exist, please try again.")
        else:
            if check_password_hash(user.password, form['password']):
                login_user(user)
                flash('You were successfully logged in.')
                return redirect(url_for('secrets'))
            else:
                flash("Password incorrect, please try again.")

    return render_template("login.html")


@app.route('/secret')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('home'))



@app.route('/download')
@login_required
def download():
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], 
                               path='cheat_sheet.pdf', 
                               as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
