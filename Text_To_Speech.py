
import streamlit as st
import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=os.getenv("API_KEY"))

def app():
    st.title("Text To Speech")
    st.write("This app converts text to speech using OpenAI's API.")
    text = st.text_area("Enter the text you want to convert to speech:")

    if st.button("Convert"):
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        response.stream_to_file(speech_file_path)

        with open(speech_file_path, "wb") as f:
            f.write(response.audio)
        st.audio(speech_file_path)

if __name__ == "__main__":
    app()