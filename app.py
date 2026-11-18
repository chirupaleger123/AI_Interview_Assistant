import streamlit as st
from groq import Groq
st.set_page_config(page_title = "About Me", "Placement Practice" = '🤍', layout= "centered")
st.title("AI PLACEMENT ASSISTANT")
st.caption("Practice and Prepared for your Interview")
try:
  client = Groq(api_key = ["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API key is missing. Add it in Advanced setting")
  st.stop()
