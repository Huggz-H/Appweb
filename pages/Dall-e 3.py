import streamlit as st

st.title("Dall-e 3")

#Champ de saisie
user_input = st.text_input("Dall-e 3")


#La clé OpenAI
recherche_input = st.sidebar.text_input("La clé OpenAI")


#Intéraction avec OpenAI
from openai import OpenAI
client = OpenAI(api_key=recherche_input)

prompt = "A cute baby sea otter"

image = client.images.generate(
    model="dall-e-2",
    prompt=user_input,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url

st.image(image_url)
