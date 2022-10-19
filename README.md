# 100Days-Python-Course

This is my repository for the projects and assignments in Angela Yu's Udemy course - 100 Days of Code: The Complete Python Pro Bootcamp for 2022
Based on the quiz, I started on Day 15 Intermediate.
Many of the project days take longer than one hour, day, etc. I guess that means I got more than my 100 Days out of this.

- *Day 15* - Coffee Machine. For some reason, even though the specification said we were to ask for quarters, dimes, nickels, and pennies, the assignment did not ask to have the machine keep track of these quantities. I spent more than a day on this project.
- *Day 16* - Continued working on Coffee Machine. Created a money machine class (to keep track of the register) and a coffee maker class with different objects for coffee types. No need to create a new object each time an espresso is requested. Use a singleton for each type of coffee.  
- *Day 17* - Beginning tutorial on how Python classes and objects work. The __init__ constructor method. QuizBrain app.
- *Day 18* - Beginning a section on turtle graphics. The kind of simplistic crap that always turned me off instructional books and tutorials. For some reason, I still worked through it.
- *Day 19* - More Turtle. Turtle race and etch-a-sketch.
- *Day 20-21* - More Turtle, but this turtle comes as a snake. The snake_game. A bit more fun. Some interesting problems to work through.
- *Day 22* - pong. Whatever happened to Pong? You better believe I was listening to Frank Black and the Pixies while working on this.
- *Day 23* - turtle-crossing. Like frogger. Caroline thought it was cute.
- *Day 24* - Modified the snake game to persist scores.The day24 folder has nothing - everything in snake_game.
- *Day 25* - Pandas. perform queries on 2018 squirrel census data.
- *Day 26* - NATO-alphabet. list comprehensions and pandas.
- *Day 27* - tkinter. All the most horrible things about any gui ever. ugh.
- *Day 28* - pomodoro. More tkinter.
- *Day 29-30* - password-manager. More tkinter. add json.
- *Day 31* - flash-card app. More tkinter
- *Day 32* - Birthday-Wisher. Sends a random mail-merged birthday email to contacts
- *Day 33* - issoverhead space station notifier. Also kanye-quotes app. Using apis, kanye used tkinter. I started to use separate config file in iss, a config.py.
- *Day 34* - quizzler-app. Using trivia apis and putting on tkinter quiz app. Started to use toml as a better config loader.
- *Day 35* - rain_alert. Use openweather api and twilio app to text a rain alert.
- *Day 36* - stock-news app. Another api and json nav. Send texts with twilio. Started from extrahard. Like bragging about tying my shoes all by myself.
- *Day 37* - habit-tracker. More apis. HTTP Header authentication.
- *Day 38* - workout-tracker. More apis, using google sheet.
- *Day 39-40* - flight deals. Use Kiwi, google sheets, twilio, email.
- *Day 41-44* - web-foundation. html & css basic tutorials. A silly static page [published to pages](https://noah-clements.github.io/100-Days-site/).
- *Day 45* - 100Movies and bs4. Beautiful Soup web scraping. Top 100 movies and Ycombinator news articles.
- *Day 46* - blast-from-past. Use Beautiful Soup to scrape Billboard Top 100 Songs for a particular day in the past and use Spotify API to search for the songs and create a playlist. Cute way to tell your loved ones you were thinking of then (their birthday, anniversary, etc)
- *Day 47* - price-tracker. More soup. Scrape amazon price for st and email if below x price.
- *Day 48* - selenium. play the cookie clicker game. Manually it hurt my wrist.
- *Day 49* - selenium. Automated job-search and application (?!?!?!). I just auto-saved, then used selenium to auto-remove all saved jobs.
- *Day 50* - skipped. More selenium. I just followed teacher's code. Auto-Tinder swiping bot. You must be <del>fucking</del> kidding me. I like my wife, thank you very much.
- *Day 51* - skipped. More selenium. I just followed along with teacher's code. Automatic twitter complaint bot for internet speed.
- *Day 52* - skipped. More selenium. Again, one must question the choices of selenium automation projects. Here it is an automatic instagram follower bot.
- *Day 53* - property-search. Selenium "capstone". Finally, a project that won't cause social media (and IRL) problems. Search for properties in Zillow, scrape data, and put them into a Google Sheet
- *Day 54* - hello_flask. flask, passing and nesting functions, python decorator functions.
- *Day 55* - hello_flask. continued. guess a number game.
- *Day 56* - name-card. flask & html5up template
- *Day 57* - day57 folder. using apis in flask - age & gender guess site. blog-templating. Flask and jinja. Use fake blog data from api
- *Day 58* -  TinDog. this was kind of fun. Would love to make it dynamic. Bootstrap, CSS styling, etc.
- *Day 59-60* - upgraded blog. "Blog Capstone" Use templates, bootstrap, css, scraping. I used the json from my personal wordpress blog. Day 60, Create contact form and email info. Put in selenium unit-tests of site.
- *Day 61* - flask-secrets. Flask-WTF, Bootstrap inherited template, quickform
- *Day 62* - Coffee & Wifi. Using Bootstrap quickforms WTForms Flask-WTF, and extending the bootstrap/base.html and overloading the css. Was going to use a csv.DictWriter for the WTForm, but the csv did not have an ending "\n", so would continue the last line on the first add. I would have thought that was the point of adding keys to the DictWriter (so it could place values in the correct column), but this is not a panda. Did what the class solution suggested, no need to use csv class to write with a ",".join. Continuing using Selenium based unittests a la TDD.
- *Day 63* - library-start. Using SQLAlchemy for CRUD saving books to a library.db. The full CRUD. Discovered that WTForms are difficult to get on single line. inline type doesn't do it. Was just as easy to use flask.request. Used pytest rather than unittest.
- *Day 64* - movie-project. More SQL Alchemy and CRUD, but also using an api that returns json. Mapped json data to the Movie record object. Trying to figure out the tests for this has been much harder than the project proper. Will have to work on learning how to run tests against flask apps separately. Maybe what I had been doing with selenium tests was appropriate? Will have to work through [Miguel Grinberg's tutorial.](https://blog.miguelgrinberg.com/post/how-to-write-unit-tests-in-python-part-3-web-applications) and/or the [testdriven tutorial](https://testdriven.io/blog/flask-pytest/)
- *Day 65* - web design. The Mutiny. Design a hotel site on Canva. [Mine is here:](https://www.canva.com/design/DAFKY24CHZI/Prvrfq0PYSf1PL5L_xKw7w/view?website#1). Mobile should definitely use [scroll site](https://www.canva.com/design/DAFKY24CHZI/Prvrfq0PYSf1PL5L_xKw7w/view?website#2:home) rather than menu. Think I would need to have the colors in the photos blend in together more though.
- *Day 66* - cafe-api. Create a simple api for listing, adding, updating, and deleting cafes from a database. Used postman for testing and automatic documentation.
- *Day 67* - RESTful-blog. Create Read Update Delete (and list) blog posts in db using SQLAlchemy, WTForms, and ckeditor. Would like to refactor to separate out the model, the db, and the form. MVC and App factory patterns. Would also like to take the blog scraping from days 59-60 and do an initial import of posts. So an import function from wordpress.
- *Day 68* - flask-auth. Authentication. Weurkzeug password hashing. flask-login
- *Day 69* - blog-with-users. Adding users to allow comments on a blog. Using Authentication, etc. Added in the code from upgraded-blog to import blog posts from my wordpress site. Then I used the orm models to put the posts into database on first load.
- *Day 70* - deploy. Convert to Postgres. Got drop, create, and load db working remotely (Render would time out). Used Render instead of Heroku, since Heroku is no longer free. [Blog here.](https://bloggr-fw86.onrender.com/)
- *Day 71* - "Data science". Jupyter notebooks and pandas. Using Google Collab. Some things never change, like the need for every discipline to try to create what they see as more prestigious euphemisms for what they do. Obsfucation in the service of self-importance. "We're not simple analysts, but a-hem *scientists*!!!"
- *Day 72* - "Data science". Jupyter notebooks, pandas, matplotlib. Used VSCode jupyter, just as easy.
- *Day 73* - "Data science". More pandas, jupyter, markdown. Legos data. Big lesson for me was pandas [agg](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html) and [merge.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) See also this [stack-overflow page for merge.](https://stackoverflow.com/questions/53645882/pandas-merging-101)
- *Day 74* - "Data science". Google data trends.  More Matplotlib. Downloaded own search trend data and FRED Unemployment data, and merged to create updated analysis.
- *Day 75* - Using plotly with pandas. Analysis of Google App store trends, etc.
- *Day 76* - Numpy, linear algebra, numpy broadcasting, matrix multiplication, and Image processing. Used Matplotlib imshow. I think I went more into Pillow (PIL) than was intended.
- *Day 77* - SciPy and Seaborn. More about query/selecting rows using .loc and .query. Learned that the `[[column]]` is not really a special pandas syntax trick, but the result of passing a list of column names (even a list of one) to the single-bracket selector. This returns a dataframe rather than a Series, which you get if you just reference the column. There must be a lot more to Seaborn that we didn't get - has to be more than just a series of default themes? Also just scratched surface with SciPy linear regression.
- *Day 78* - "Nobel Prize Analysis". More involved graphing using matplotlib and plotly express. So easy to forget the apis of pandas, plotly, and matplotlib, and the documentation is not so easy to understand or navigate. Whine, moan.
    - Reviewed donut and bar charts with plotly; Pandas `.groupby()`, `value_counts()`, `.agg()`, and `.merge()`.
    - Learned chloropleth (I'm not sure I remember it now), sunburst charts (very cool), box plots, `.regplot()` and `.lmplot()` from Seaborn 

