import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Analyse FTL", layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Pays - Pays", "Code Postal - Code Postal"],
        icons=["globe", "map"],
        menu_icon="cast",
        default_index=0
    )

# File uploader widget
uploaded_file = st.file_uploader("Met le fichier ici ", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File successfully uploaded and read!")
        if selected == "Pays - Pays":
            st.subheader("🌍 View: Pays - Pays")
            # Show only relevant columns if exist
            cols = [col for col in df.columns if 'country' in col.lower()]
            if cols:
                st.dataframe(df[cols])
            else:
                st.dataframe(df)

        elif selected == "Code Postal - Code Postal":
            st.subheader("📮 View: Code Postal - Code Postal")
            cols = [col for col in df.columns if 'post' in col.lower()]
            if cols:
                st.dataframe(df[cols])
            else:
                st.dataframe(df)


    except Exception as e:
        st.error(f"❌ An error occurred while reading the file: {e}")