import smtplib
import datetime as dt
import random

GMAIL = "noahclemtest@gmail.com"
G_PWD = "ruqbdjzlicgplwbp"
YAHOO_EMAIL = "noahclemtest@yahoo.com"

# get day of week and test for today
# Define a list of weekday names
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Index using weekday int value

now = dt.datetime.now()
day = days[now.weekday()]
print(day)

if day == 'Wednesday':
    with open("quotes.txt") as f:
        quotes = f.readlines()

    # choose quote
    quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # connection = smtplib.SMTP("smtp.mail.yahoo.com", port=587) # doesn't work
        connection.starttls()
        connection.login(GMAIL, password=G_PWD)
        connection.sendmail(from_addr=GMAIL, 
                            to_addrs=YAHOO_EMAIL, 
                            msg=f"Subject:A little {day} motivation\n\n {quote}")
    # connection.close() #just like files, if using with will close for you

