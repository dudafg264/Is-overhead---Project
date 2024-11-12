# ISS Notifier Project

This is a Python-based project that sends an email notification when the International Space Station (ISS) is passing over a specific location (latitude and longitude) during the night time.

## Project Overview

The script runs continuously, checking the position of the ISS and the local sunrise and sunset times for a given latitude and longitude. If the ISS is passing nearby and it is nighttime, an email notification is sent to the user.

## Features
- Tracks the real-time position of the ISS.
- Determines the local sunrise and sunset times using the **Sunrise-Sunset API**.
- Checks if the ISS is within a 5-degree radius of a specific location.
- Sends an email notification if the ISS is visible at night.
- The script runs in a loop and checks the position every minute.


## How It Works

1. **Fetch ISS Position**: The script fetches the current latitude and longitude of the ISS from the **Open Notify API**.
   
2. **Fetch Sunrise and Sunset Times**: The script also fetches the local sunrise and sunset times from the **Sunrise-Sunset API** for the specified location (latitude and longitude).

3. **Check Conditions**:
   - The script checks if the ISS is within a 5-degree range of the specified location.
   - It then checks if the current time is during the night (i.e., after sunset or before sunrise).

4. **Send Notification**: If both conditions are met (ISS is passing by and it’s nighttime), the script sends an email notification to the specified email address.

5. **Loop**: The script repeats the process every 60 seconds to ensure real-time updates.
