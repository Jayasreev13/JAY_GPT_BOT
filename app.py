import streamlit as st
import openai
from gtts import gTTS  # new import
from io import BytesIO  # new import

openai.api_key = "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"
messages=[ {"role": "system", "content": "You are a helpful assistant."},]

# Streamlit Dashboard
st.markdown("<h1 style='text-align: center; color: blue;'>I am Jay! Your AI VideoBot </h1>", unsafe_allow_html=True)
#st.image("jay_standgif.gif", width = 200)
st.title("AI Videobot using GPT-3")
st.header(" Start your Conversation with Jay!")
#st.markdown("<h3 style='text-align: center; color: blue;'>Enter a prompt and let GPT generate a response</h3>", unsafe_allow_html=True)

def text_to_speech(text):
    """
    Converts text to an audio file using gTTS and returns the audio file as binary data
    """
    audio_bytes = BytesIO()
    tts = gTTS(text=text, lang="en")
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes.read()

def chatbot():
    global messages
    user_input = st.text_input("Enter a prompt: ")
    if user_input:
        messages.append({"role": "user", "content": user_input})
    searchbutton = st.button("Search")
    if searchbutton:
        response = open.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = messages
        )
        system_response=response["choices"][0]["message"]["content"]
        messages.append({"role": "system", "content": system_response})

        for message in messages:
            st.write(message["content"])
            st.audio(text_to_speech(system_response), format="audio/wav")

chatbot()                     

