import requests
from datetime import datetime
import os

# Getting environment variable
app = os.getenv("APP_ID")
api = os.getenv("API_KEY")
b_token = os.getenv("BEARER_TOKEN")

GENDER = "male"
WEIGHT = 61
HEIGHT = 167
AGE = 24

query = input("Tell me what exercise you did: ")

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/d23cd0126d7c0aacf1188f602ed2f65b/workoutTracking/workouts"

param = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

header = {
    "x-app-id": app,
    "x-app-key": api,
}

connection = requests.post(url=nutri_endpoint, json=param, headers=header)
nutrix_result = connection.json()

date = datetime.now().strftime("%d/%m/f%Y")
time =  datetime.now().strftime("%X")

headers = {
    "Authorization": f"Bearer {b_token}"
}

for exercise in nutrix_result["exercises"]:
    sheet_param = {
        "workout": {
            "date": date,
            "dime": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    cnnct = requests.post(url=sheety_endpoint, json=sheet_param, headers=headers)
    print(cnnct.json())