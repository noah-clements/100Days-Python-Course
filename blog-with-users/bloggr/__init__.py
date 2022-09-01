import os
from flask import Flask
import toml

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True )
    app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_file(".project_config", load=toml.load)
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

    

