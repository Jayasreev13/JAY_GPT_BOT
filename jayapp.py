import streamlit as st
import openai
import config
from gtts import gTTS  # new import
from io import BytesIO  # new import
from streamlit_chat import message

openai.api_key = config.api_key

messages=[ 
    {"role": "system", "content": "You are a helpful assistant."}, 
]
st.markdown("<h1 style='text-align: center; color: blue;'>I am Jay! Your AI VideoBot </h1>", unsafe_allow_html=True)

def main(): 
    st.image("jay_standgif.gif", width = 300)
    st.title("AI Videobot using GPT-3")
    st.header(" Start your Conversation with Jay!")   
if __name__ == '__main__':
    main()

st.markdown("<h3 style='text-align: center; color: blue;'>Enter a prompt and let GPT generate a response</h3>", unsafe_allow_html=True)

def text_to_speech(text):
    """
    Converts text to an audio file using gTTS and returns the audio file as binary data
    """
    audio_bytes = BytesIO()
    tts = gTTS(text=text, lang="en")
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes.read()

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message 


# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
    st.audio(text_to_speech(system_response), format="audio/wav")

if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
  
        
