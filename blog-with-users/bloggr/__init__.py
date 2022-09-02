import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import toml

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True )
    app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

    ##CONNECT TO DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # Register init-db cli command from the model (flask tutorial)
    from . import models
    models.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_file(".project_config", load=toml.load, silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

    

