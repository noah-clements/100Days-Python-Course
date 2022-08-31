import pytest
import requests

from .. import User, db

URL = "http://127.0.0.1:5000/"

@pytest.fixture()
def create_user():
    user = User(
        name='Noah',
        email='noahclemtest@gmail.com',
        password='bubba1'
    )
    yield user
    delete_user(user)

def test_register_user(create_user):
    resp = requests.post(URL + 'register', user.to_dict())
    resp.raise_for_status()
    assert create_user.name in resp.content

def delete_user(user:User):
    db_user = db.session.query.get(user.email)
    db.session.delete(db_user)
    db.session.commit()
    

