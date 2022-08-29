from dataclasses import dataclass
from flask import Flask, jsonify, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

REQD_API_KEY = "TopSecretAPIKey"

##Cafe TABLE Configuration
@dataclass(init=False) 
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) 
                for column in self.__table__.columns}

    def __repr__(self):
        return { 'cafe': self.to_dict()}
 
    def __str__(self) -> str:
        return f"{self.__repr__()}"

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random')
def random():
    cafe = db.session.query(Cafe).order_by(func.random()).first()
    print(cafe)
    # jsonify does not work with the string representation of the dict
    return jsonify(cafe=cafe.to_dict())

@app.route('/all')
def all():
    all_cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])    

@app.route('/search')
def method_name():
    location = request.args.get("loc")
    local_cafes = Cafe.query.filter(Cafe.location == location).all()
    if len(local_cafes) > 0:
        return jsonify(cafes=[cafe.to_dict() for cafe in local_cafes])
    else:
        return jsonify(error={
            'Not Found': "sorry, we don't have a cafe at that location."
            })

## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    cafe = Cafe()
    cafe.name = request.form.get('name')
    cafe.map_url = request.form.get('map_url')
    cafe.img_url = request.form.get('img_url')
    cafe.location = request.form.get('location')
    cafe.seats = request.form.get('seats')
    cafe.has_toilet = (request.form.get('has_toilet') == 'True')
    cafe.has_wifi = (request.form.get('has_wifi') == 'True')
    cafe.has_sockets = (request.form.get('has_sockets') == 'True')
    cafe.can_take_calls = (request.form.get('can_take_calls') == 'True')
    cafe.coffee_price = request.form.get('coffee_price')

    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={'success': 'Successfully added the new cafe'})
    

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe is None:
        return jsonify(error={'Not Found': 
            'Sorry, a cafe with that id was not found in the database.'})
    else:
        cafe.coffee_price = request.args.get('new_price')
        db.session.commit()
        return jsonify(response={'success': 'Successfully updated the price.'})


## HTTP DELETE - Delete Record

@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    if not request.args.get('api-key') == REQD_API_KEY:
        # abort does not return the json. If I put the json first, status is 200
        # abort(403, jsonify(error={ 'Forbidden': "Sorry, that's not allowed." \
        #                "Make sure you have the correct api-key."}))
        return jsonify(error={ 'Forbidden': "Sorry, that's not allowed." \
                       "Make sure you have the correct api-key."}), 403
        
    cafe = Cafe.query.get(cafe_id)
    if cafe is None:
        return jsonify(error={'Not Found': 
            'Sorry, a cafe with that id was not found in the database.'}), 404
    else:
        name = cafe.name
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={'success': 
            f'Successfully deleted {name} from the list.'})

if __name__ == '__main__':
    app.run(debug=True)
