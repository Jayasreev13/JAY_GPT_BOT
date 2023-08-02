import openai
import streamlit as st


openai.api_key = "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"

# Streamlit Dashboard
st.title("🔍I am Jay! AI Bot powered by ChatGPT")
st.video('jay_audio.mp4')
st.caption('I am Jay! An AI Digital Human created using D-ID for So.evo')
st.header("Start your Conversation with Jay!")


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5"
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("What is up?"):
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
