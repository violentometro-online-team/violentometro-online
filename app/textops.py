import requests
import streamlit as st


def get_prediction(text):
    url = st.secrets["predict_url"]
    data = {"sentence": text}

    resp = requests.post(url, json=data)

    pred = resp.json()["prediction"]

    return f"La oración tiene un {pred*100:.2f}% de presentar discurso de odio."
