
import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob

from gtts import gTTS
from googletrans import Translator

spoken_text = None


st.title("¿Qué meme eres según como te sientes? 🥳")
st.subheader("¿Cómo te sientes hoy?")

width, height = 200, 200

modo = st.radio("Bueno, empecemos por conocer cómo te sientes", ("Feliz", "Triste", "Enojado", "Preocupado", "Asustado"))
if modo == "Feliz":
    st.write("¡Que bien!😊")
    image = Image.open("feliz.png")
    st.image(image)
if modo == "Triste":
    st.write("NOOOO Que pesar 😔.")
    image2 = Image.open("triste.png")
    st.image(image2)
if modo == "Enojado":
    st.write("Que desafortunado 😔.")
    image3 = Image.open("enojado.png")
    st.image(image3)
if modo == "Preocupado":
    st.write("Lo lamento mucho 😔.")
    image4 = Image.open("preocupado.png")
    st.image(image4)
if modo == "Asustado":
    st.write("Esperemos que todo salga bien 😔.")
    image5 = Image.open("asustado.png")
    st.image(image5)



# AUDIO A TEXTO
stt_button = Button(label=" COMENZAR ", width=200)

st.subheader("Cuéntame más sobre la respuesta que esperas, ¿qué te gustaría ser? Una gallina sonriente, un gato enojado o tal vez homero simpson acostado en su cama...")
st.write("Apenas hundas sobre el botón, comienza a hablar:")

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        spoken_text = result.get("GET_TEXT")
        st.write("Esto es lo que nos comentaste:", spoken_text)



#RECONOCIMIENTO DE EMOCIONES
from textblob import TextBlob
import streamlit as st

st.subheader("Así interpretamos lo que dices:")
st.write("(Apenas me lo cuentes mediante el botón, lo analizaremos.")
st.write("")
st.write("Nos parece que pensamos esto:")


if spoken_text:
    blob = TextBlob(spoken_text)
    st.write('Polarity: ', round(blob.sentiment.polarity,2))
    st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
    x = round(blob.sentiment.polarity,2)
    if x >= 0.5:
        st.write( 'Es un sentimiento Positivo 😊')
    elif x <= -0.5:
        st.write( 'Es un sentimiento Negativo 😔')
    else:
        st.write( 'Es un sentimiento Neutral 😐')


st.write("")
st.write("")

#RECOMENDACIÓN
st.subheader("El meme que te asignamos el día de hoy es: ")
if modo == "Feliz":
    image6 = Image.open("feliz meme.jpg")
    st.image(image6)
if modo == "Triste":
    image7 = Image.open("tristeza meme.jpg")
    st.image(image7)
if modo == "Enojado":
    image8 = Image.open("enojo meme.jpg")
    st.image(image8)
if modo == "Preocupado":
    image9 = Image.open("preocupado meme.jpg")
    st.image(image9)
if modo == "Asustado":
    image10 = Image.open("preocupado meme.jpg")
    st.image(image10)







