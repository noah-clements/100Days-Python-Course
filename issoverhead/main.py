import requests
from datetime import datetime, timezone
import smtplib
import time
import config

MY_LAT = 41.585550  # Your latitude
MY_LONG = -70.518260  # Your longitude


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

 #Your position is within +5 or -5 degrees of the ISS position.
def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return ((MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and
            (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5))


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc)
    return time_now.hour >= sunset or time_now.hour <= sunrise

while True:
    #If the ISS is close to my current position and it is currently dark
    if is_iss_close() and is_night():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(config.GMAIL, password=config.G_PWD)
            connection.sendmail(from_addr=config.GMAIL, 
                                to_addrs=config.YAHOO_EMAIL, 
                                msg="Subject:Look up!\n\n" + 
                                "The International Space Station is visible right now!")
# # BONUS: run the code every 60 seconds.
    time.sleep(60)



