import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv('API_KEY')
LATITUDE=os.getenv('LATITUDE')
LONGITUDE=os.getenv('LONGITUDE')

response=requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}")
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data["list"][:4]
will_rain=False
for hour_data in weather_slice:
    condition_code=(hour_data["weather"][0]["id"])
    if int(condition_code<700):
        will_rain=True
if will_rain:
    print("Bring Umberela")
else:
    print("No Need to Bring Umberela")
