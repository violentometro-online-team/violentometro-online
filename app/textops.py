import os
import requests


def get_prediction(text):
    url = os.environ["PREDICTION_URL"]
    data = {"sentence": text}

    resp = requests.post(url, json=data)

    pred = resp.json()["prediction"]

    return f"La oración tiene un {pred*100:.2f}% de presentar discurso de odio."
