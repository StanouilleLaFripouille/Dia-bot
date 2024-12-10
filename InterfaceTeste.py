import streamlit as st

st.title("Dia-bot : Chatbot pour diabètique")
st.write("Vous pouvez poser des questions sur le diabète et avoir des conseils personnalisés selon vos symptômes.")
st.write("")

# Zone de texte pour interagir avec l'utilisateur
user_input = st.text_input('Entrez votre question, par exemple : "Qu\'est-ce que le diabète de type 1 ?" ou "Je me sens fatigué, que faire ?"')

if user_input:
    # Réponse basique
    st.write(f"Vous avez dit : {user_input}")
    st.write("Le chatbot répondra ici.")
