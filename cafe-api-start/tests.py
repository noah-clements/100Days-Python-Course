import timeit
import pytest
import random
from sqlalchemy import func

from main import db, Cafe

def test_random_cafe_by_sql():
    cafe = db.session.query(Cafe).order_by(func.random()).first() 

def test_random_cafe_by_rand():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)

def test_random_cafe_by_offset():
    row_count = Cafe.query.count()
    # Generate a random number for skipping some records
    random_offset = random.randint(0, row_count-1)
    # Return the first record after skipping random_offset rows
    random_cafe = Cafe.query.offset(random_offset).first()

print(f"SQL : order_by(func.random()).first() {timeit.timeit(test_random_cafe_by_sql, number=10000)}")    
print(f"random.choice(query.all()) {timeit.timeit(test_random_cafe_by_rand, number=10000)}")
print(f"query.offset) {timeit.timeit(test_random_cafe_by_offset, number=10000)}")