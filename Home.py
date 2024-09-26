import streamlit as st 

# Titre 
st.title("Mon formulaire")

# Texte 
st.write("ceci est un formulaire de contact")

#champ de saisi 
user_input = st.text_input("Tapez votre texte : ")

st.write (user_input)

#image
st.image ("https://cdn-europe1.lanmedia.fr/var/europe1/storage/images/europe1/culture/ceremonie-douverture-des-jo-david-guetta-setonne-de-ne-pas-avoir-ete-appele-4255568/61758829-1-fre-FR/Ceremonie-d-ouverture-des-JO-David-Guetta-s-etonne-de-ne-pas-avoir-ete-appele.jpg")

#sidebar
st.sidebar.title ("Hugo Da Silva")
 
# Vidéo dans la sidebar
st.sidebar.video("https://www.youtube.com/watch?v=mu5SSkn23lY")

#Select bar 
st.selectbox ("Selectionnez votre niveau d'étude", ["Bac", "Bac+2","Bac+5"])

#Selexr slider
age = st.select_slider("Quel est votre âge ?", range(0, 99))

#Conditions en python 
if age >= age >=18; 
st.write("vous êtes majeur")
else
st.write("Vous êtes mineur")

