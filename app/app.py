import streamlit as st
import pickle
from textops import predict


@st.cache(persist=True, allow_output_mutation=True)
def load_model():
    return pickle.load(open("final_model.sav", "rb"))


@st.cache(persist=True, allow_output_mutation=True)
def load_CV():
    return pickle.load(open("final_CV.sav", "rb"))


model = load_model()
CV = load_CV()

st.title("Violentómetro Online")
st.write("Prototipo para detectar discurso de odio en línea contra mujeres.")

sentence = st.text_area("Ingresa tu mensaje a analizar:")

if sentence:
    probability = predict(sentence, model, CV)
    st.write(probability)
