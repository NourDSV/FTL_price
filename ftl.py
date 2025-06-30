import pandas as pd
import streamlit as st


st.title("Analyse FTL")

# File uploader widget
uploaded_file = st.file_uploader("Met le fichier ici ", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File successfully uploaded and read!")
        st.write("### Preview of your data:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"❌ An error occurred while reading the file: {e}")