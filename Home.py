import streamlit as st

st.set_page_config(page_title="NU Tools", layout="wide")

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

st.title("Welcome to NU Tools")
st.write("This is a collection of useful tools for various tasks.")

st.header("Available Tools")
st.write("1. PDF Converter - Parse, convert, and translate PDF files")
st.write("2. [Other Tool] - Description of other tool")

st.markdown("---")
st.write("To use a tool, select it from the sidebar on the left.")