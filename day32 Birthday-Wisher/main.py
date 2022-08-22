##################### Extra Hard Starting Project ######################
import random
import smtplib
import datetime as dt
import pandas as pd
import toml

REPLACE = "[NAME]"

config = toml.load(".project_config")
GMAIL = config['Email']['address']
G_PWD = config['Email']['pwd']
smtp = config['Email']['smtp']
port = config['Email']['port']


df = pd.read_csv("birthdays.csv")
# print(df)
# birthday_list = df.to_dict(orient='records')
# print(birthday_list)
today = dt.date.today()
for (index, person) in df.iterrows():
    person_birthday = dt.date(today.year, person.month, person.day)
# 2. Check if today matches a birthday in the birthdays.csv
    if person_birthday == today:
        print(f"here I am - {person['name']}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(letter) as file:
            template = file.read()
        output_text = template.replace(REPLACE, person['name'])
        
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(smtp, port=port) as connection:
        # connection = smtplib.SMTP("smtp.mail.yahoo.com", port=587) # doesn't work
            connection.starttls()
            connection.login(GMAIL, password=G_PWD)
            connection.sendmail(from_addr=GMAIL, 
                                to_addrs=person['email'], 
                                msg=f"Subject:Happy Birthday!\n\n {output_text}")
