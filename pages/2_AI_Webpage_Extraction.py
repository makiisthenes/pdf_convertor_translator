import streamlit as st
import requests

JINA_BASE_URL = "https://r.jina.ai/"
st.set_page_config(page_title="AI Website Extraction", layout="wide")

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

def scrape_jina_ai(url: str) -> str:
  response = requests.get(JINA_BASE_URL + url)
  return response.text

def main():
    st.header("AI Website Extraction")
    st.subheader("This tool is used to extract key information from website, via Jina AI")
    st.write("Created by Michael Peres 12/08/2024")

    url = st.text_input("Enter Website URL")

    summarised_webcontent = scrape_jina_ai(url)

    st.text_area("Summarised Webpage", summarised_webcontent)
    st.markdown("---")


if __name__ == "__main__":
    main()