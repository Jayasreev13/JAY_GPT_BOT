import streamlit as st
import openai
import config
from gtts import gTTS  # new import
from io import BytesIO  # new import
from streamlit_pills import pills

openai.api_key = config.api_key

messages=[ 
    {"role": "system", "content": "You are a helpful assistant."}, 
]
st.markdown("<h1 style='text-align: center; color: blue;'>I am Jay! Your AI VideoBot </h1>", unsafe_allow_html=True)

def main(): 
    st.image("jay_standgif.gif", width = 300)
    st.title("AI Videobot using GPT-3")
    st.header(" Start your Conversation with Jay!")
    selected = pills("", ["NO Streaming", "Streaming"], ["🎈", "🌈"])
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


#openai.api_key = st.secrets['api_secret']


user_input = st.text_input("You: ",placeholder = "Ask me anything ...", key="input")


if st.button("Submit", type="primary"):
    st.markdown("----")
    res_box = st.empty()
    if selected == "Streaming":
        report = []
        for resp in openai.ChatCompletion.create(model='gpt-3.5',
                                            prompt=user_input,
                                            max_tokens=120, 
                                            temperature = 0.5,
                                            stream = True):
            # join method to concatenate the elements of the list 
            # into a single string, 
            # then strip out any empty strings
            report.append(resp.choices[0].text)
            result = "".join(report).strip()
            result = result.replace("\n", "")        
            res_box.markdown(f'*{result}*')
            st.audio(text_to_speech(system_response), format="audio/wav")
                                                
            
    else:
        completions = openai.ChatCompletion.create(model='gpt-3.5',
                                            prompt=user_input,
                                            max_tokens=120, 
                                            temperature = 0.5,
                                            stream = False)
        result = completions.choices[0].text
        
        res_box.write(result)
st.markdown("----")




  
        
