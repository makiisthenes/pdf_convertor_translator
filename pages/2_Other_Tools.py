import streamlit as st

st.set_page_config(page_title="Other Tool", layout="wide")

# Your existing style modifications
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

st.header("Other Tools")
st.write("This is another tool in the NU Tools collection. Can be added easily and agile.")

# Add the functionality for this tool here