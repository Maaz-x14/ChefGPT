from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def build_restaurant_name_chain(llm):
    prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="Suggest one creative and modern restaurant name for a {cuisine} cuisine. Output only the name, no explanation."
    )
    return prompt | llm | StrOutputParser()
