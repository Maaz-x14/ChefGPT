import streamlit as st
from config.settings import setup_page
from utils.llm_loader import load_llm
from chains.restaurant_name_chain import build_restaurant_name_chain
from chains.menu_chain import build_menu_chain
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

# Setup UI
setup_page()

# Input
cuisine = st.text_input("Enter a cuisine type (e.g. Italian, Mongolian, Japanese):")

if cuisine:
    llm = load_llm()

    # Build reusable chains
    name_chain = build_restaurant_name_chain(llm)
    menu_chain = build_menu_chain(llm)

    # Build final pipeline (LCEL version of SequentialChain)
    full_chain = (
        {"cuisine": RunnablePassthrough()}
        | RunnableParallel(
            restaurant_name=name_chain,
            menu_items=lambda x: menu_chain.invoke({
                "restaurant_name": name_chain.invoke({"cuisine": x["cuisine"]}),
                "cuisine": x["cuisine"]
            })
        )
    )

    with st.spinner("Cooking up something delicious... 🍳"):
        result = full_chain.invoke({"cuisine": cuisine})

    # --- OUTPUT ---
    st.subheader("🏷️ Restaurant Name")
    st.success(result["restaurant_name"])

    st.subheader("📜 Menu")
    st.write(result["menu_items"])
