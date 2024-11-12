import time
import requests
import smtplib
from datetime import datetime

MY_LAT = 31.7714 #latitude
MY_LONG = -52.3421 #longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

my_email = "myemail@gmail.com"
password = "xxxxxxxxxxxxxxx"
to_email = "toemail@gmail.com"

while True:
    time_now = datetime.now()

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    #If the ISS is close to my current position
    if iss_latitude <= MY_LAT + 5 and iss_latitude >= MY_LAT - 5 and iss_longitude <= MY_LONG + 5 and iss_longitude >= MY_LONG - 5:
        if time_now.hour >= sunset or time_now.hour < sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=to_email,
                    msg=f"Subject: Look Up!\n\nThe International Space Station is passing by!"
                )
                print(f"Email enviado para {my_email}")

    time.sleep(60)