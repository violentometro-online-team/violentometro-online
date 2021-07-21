import requests
import streamlit as st


def get_prediction(text):
    url = st.secrets["base_url"] + "/predict"
    data = {"sentence": text}

    resp = requests.post(url, json=data)

    pred = resp.json()

    return f"La oración tiene un {pred*100}% de presentar discurso de odio."
