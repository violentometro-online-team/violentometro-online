import streamlit as st
from textops import get_prediction


st.title("Violentómetro Online")
st.write("Prototipo para detectar discurso de odio en línea.")

sentence = st.text_area("Ingresa tu mensaje a analizar:")

if sentence:
    probability = get_prediction(sentence)
    st.write(probability)
