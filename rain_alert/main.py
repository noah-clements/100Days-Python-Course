import requests
from twilio.rest import Client
import toml

config = toml.load(".project_config")

parameters = {
    "lat": config['location']['my_lat'],
    "lon": config['location']['my_long'],
    "appid": config['owm_key'],
    "units": "imperial",
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",
                        params = parameters)
response.raise_for_status()

data = response.json()['hourly'][:12]
weather_data = [item['weather'][0]['id'] for item in data if item['weather'][0]['id'] < 700]
print(weather_data)
if len(weather_data) > 0:
    print("Bring an Umbrella")
# print(weather_data['hourly']['0']['weather']['id'])
    client = Client(config['Twilio']['account_sid'], config['Twilio']['auth_token'])

    message = client.messages \
                    .create(
                        body="It's going to rain. Remember to bring your ☔️",
                        from_=config['Twilio']['from_'],
                        to=config['Twilio']['to_']
                    )

    print(message.status)