# import toml
import requests
import datetime as dt
import os
from zoneinfo import ZoneInfo


# config = toml.load(".python_config")

APP_ID = os.environ['NT_APP_ID']
N_KEY = os.environ['NT_API_KEY']



nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : N_KEY,
    "x-remote-user-id": "0"
}

query = input("Tell me which exercises you did: ")

params = {
    "query" : query,
    "gender" : "male",
    "weight_kg" : "111",
    "height_cm" : "190.5",
    "age" : "53"
}

response = requests.post(url=nutri_endpoint, headers=headers, json=params)
response.raise_for_status()
exercises = response.json()['exercises']
# print(response.text)

sheety_endpoint = "https://api.sheety.co/6e554546d51ae434c4a518b2f69806bd/myWorkouts/workouts"

sheet_headers = {
    "Authorization": os.environ['Sheety_Auth']
}

datetime = dt.datetime.now()
datetime.astimezone(tz=ZoneInfo("America/New_York"))
date = datetime.strftime("%d/%m/%Y")
time = datetime.strftime("%X")

for exercise in exercises:
    sheet_params = {
        "workout" : {
            "date" : date,
            "time" : time,
            "exercise" : exercise['name'].title(),
            "duration" : exercise['duration_min'],
            "calories" : exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_params, headers=sheet_headers)
    sheet_response.raise_for_status()
    print(sheet_response.text)