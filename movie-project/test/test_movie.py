import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from main import Movie, db


class TestMovie():
    
    @pytest.mark.skip(reason='already added this movie. DB requires unique')
    def test_add_movie(self):
        movie = Movie(
                        title="Phone Booth",
                        year=2002,
                        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
                        rating=7.3,
                        ranking=10,
                        review="My favourite character was the caller.",
                        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
                        )
        db.session.add(movie)
        db.session.commit()

    def test_movie_query(self):
        all_movies = Movie.query.order_by(Movie.rating).all()
        phone_booth_there = False
        for movie in all_movies:
            if movie.title == "Phone Booth":
                phone_booth_there = True
                break
        assert phone_booth_there
        