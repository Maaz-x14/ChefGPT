from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def build_menu_chain(llm):
    prompt = PromptTemplate(
        input_variables=["restaurant_name", "cuisine"],
        template=(
            "Create a menu for a {cuisine} restaurant named '{restaurant_name}'. "
            "Organize dishes under categories like Appetizers, Main Course, and Desserts. "
            "Include short, creative descriptions and prices in {cuisine} currency."
        ),
    )
    return prompt | llm | StrOutputParser()
