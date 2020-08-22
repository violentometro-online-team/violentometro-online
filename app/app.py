import streamlit as st

st.title("Violentómetro Online")
st.write(
    "Prototipo para detectar discurso de odio contra las mujeres en medios digitales escritos."
)

sentence = st.text_input("Ingresa tu mensaje a analizar:")

if sentence:
    st.write("Este mensaje (no) contiene discurso de odio")
    # st.write(my_model.predict(sentence))
