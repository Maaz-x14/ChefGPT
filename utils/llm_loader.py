from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import get_api_key

def load_llm(model_name="gemini-2.0-flash", temperature=1.0):
    api_key = get_api_key()
    return ChatGoogleGenerativeAI(model=model_name, temperature=temperature, api_key=api_key)
