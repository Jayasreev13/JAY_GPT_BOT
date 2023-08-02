import streamlit as st
from gtts import gTTS  
from io import BytesIO  

st.title("Jay's AI Speech Synthesizer(Text to Speech Bot)")
st.video('jay_ai_voicebot.mp4')
st.header("Type your text to hear what you say!")

#Converts text to an audio file using gTTS and returns the audio file as binary data
def text_to_speech(response):    
    audio_bytes = BytesIO()
    tts = gTTS(text=response, lang="en")
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes.read()
    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = f"{prompt}"
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        st.audio(text_to_speech(response), format="audio/wav")
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    

