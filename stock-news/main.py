import toml
import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

config = toml.load(".project_config")
# print (config['stock_api_key'])

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "apikey": config["stock_api_key"],
    "symbol": STOCK,
    "outputsize": "compact",
    "function": "TIME_SERIES_DAILY" 
}

td = timedelta(days=5)
news_params = {
    "q": COMPANY_NAME,
    "sortyBy": "publishedAt",
    "from": date.today() - td
}
news_header = {
    "X-Api-Key": config["news_api_key"]
}

stock_resp = requests.get("https://www.alphavantage.co/query", params=stock_params, headers=news_header)
stock_resp.raise_for_status()

data = stock_resp.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
close = float(data_list[0]['4. close'])
last_close = float(data_list[1]['4. close'])
dif = ((close - last_close) / last_close) * 100
up_down = None
if dif > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(dif)

if dif  > 1:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    print (date.today() - td)
    news_resp = requests.get("https://newsapi.org/v2/everything", params= news_params)
    news_resp.raise_for_status()

    articles = news_resp.json()['articles'][ :3]
    # print(news_data)



    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
    stock_header = f"{STOCK}: {up_down} {int(dif)}%"
    # create a list comprehension of texts to send
    txts = [f"{stock_header}\nHeadline: {article['title']}. \nBrief: {article['description']}" \
        for article in articles]

    client = Client(config['Twilio']['account_sid'], config['Twilio']['auth_token'])

    for txt in txts:
        message = client.messages \
                        .create(
                            body=txt,
                            from_=config['Twilio']['from_'],
                            to=config['Twilio']['to_']
                        )
        print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

