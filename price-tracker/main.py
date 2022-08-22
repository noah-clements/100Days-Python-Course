from bs4 import BeautifulSoup
import requests
from http.cookiejar import MozillaCookieJar
import smtplib
from email.message import EmailMessage
import toml

URL = 'https://smile.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_fod_1?pd_rd_i=B08PQ2KWHS&psc=1'
cookie_file = 'cookies.txt'

jar = MozillaCookieJar(cookie_file)
s = requests.Session()
s.cookies = jar

s.cookies.load()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0'
    'User-Agent': 'Defined'
}

resp = s.get(URL, headers=headers)
resp.raise_for_status()
soup = BeautifulSoup(resp.content, 'lxml')

price_whole = soup.find('span', class_='a-price-whole').text
price_cents = soup.find('span', class_='a-price-fraction').text
print(f'${price_whole}{price_cents}')
title = soup.find(id='productTitle').text.strip()
print(title)

LOW_PRICE = 200

# Test if price is lower than LOW
if int(price_whole.rstrip('.')) < LOW_PRICE:
    # Initialize email settings
    config = toml.load(".project_config")
    email = config['EMail']['address']
    email_pwd = config['EMail']['pwd']
    smtp = config['EMail']['smtp']
    port = config['EMail']['port']

    # Set up email
    msg = EmailMessage()
    msg['Subject'] = "Low Price for Instant Pot Pro!"
    msg['From'] = email
    msg['bcc'] = email
    msg.set_content(f"Amazon Price Alert!\n\n{title} is now ${price_whole}{price_cents}\n\n{URL}") 

    with smtplib.SMTP(smtp, port=port) as connection:
        connection.starttls()
        connection.login(user=email, password=email_pwd)
        connection.send_message(msg)   
else:
    print("no low price today. Try again later.")     

# print (soup.prettify())
