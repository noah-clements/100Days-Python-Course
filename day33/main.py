# import webbrowser
import requests
import datetime as dt

MY_LAT = 41.585550
MY_LONG = -70.518260

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)
# print(iss_position)
# print(data['iss_position'])

# webbrowser.open(f'https://www.latlong.net/c/?lat={latitude}&long={longitude}')

time = dt.datetime.now()
print(time.hour)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]
sunset = data['results']['sunset'].split('T')[1].split(":")[0]
print(sunrise)
print(sunset)