import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_api_key() -> str:
    key = os.getenv("Gemini_API_Key")
    if not key:
        raise ValueError("🚨 Gemini_API_Key not found in .env file.")
    return key

def setup_page():
    st.set_page_config(page_title="ChefGPT", page_icon="🍽️", layout="centered")
    st.title("🍽️ ChefGPT")
    st.caption("Your AI sous-chef — crafting creative restaurants and menus, one cuisine at a time.")
