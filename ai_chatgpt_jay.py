import openai
import streamlit as st


# Streamlit Dashboard
st.markdown("<h1 style='text-align: center; color: blue;'>I am Jay! Your AI VideoBot </h1>", unsafe_allow_html=True)
#st.image("jay_standgif.gif", width = 500)
st.title("Jay's AI Bot using ChatGPT")
st.header("Start your Conversation with Jay!")
#video_bytes = video_file.read(jay_audio.mp4)
st.video('jay_audio.mp4')
st.caption("This Digital human AI Bot is created using D-ID for So.Evo")

openai.api_key = "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"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's up ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    


