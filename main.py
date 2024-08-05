import streamlit as st
import pdftotext
import PyPDF2
from io import BytesIO
from deep_translator import GoogleTranslator
import time  # For rate limiting

st.header("PDF Parser, Converter, and Translator")
st.subheader("Created by Michael Peres 05/08/2024")

st.write("This app is used to parse, convert, and translate PDF files.")

uploaded_file = st.file_uploader("Choose a file")
password = st.text_input("PDF Password (if protected)", type="password")
translate_to_english = st.checkbox("Translate to English")


def translate_text(text, max_retries=3):
    translator = GoogleTranslator(source='auto', target='en')
    max_chunk_size = 4000  # Google Translate has a limit of about 5000 characters
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    translated_chunks = []

    for i, chunk in enumerate(chunks):
        for attempt in range(max_retries):
            try:
                translated_chunk = translator.translate(chunk)
                translated_chunks.append(translated_chunk)
                break
            except Exception as e:
                if attempt < max_retries - 1:
                    st.warning(f"Translation attempt {attempt + 1} for chunk {i + 1} failed. Retrying...")
                    time.sleep(1)  # Wait for 1 second before retrying
                else:
                    st.warning(f"Translation failed for chunk {i + 1}: {str(e)}. Displaying original text for this chunk.")
                    translated_chunks.append(chunk)

        time.sleep(1)  # Rate limit to avoid overwhelming the service

    return ' '.join(translated_chunks)


if uploaded_file is not None:
    try:
        file_bytes = uploaded_file.read()

        if password:
            pdf_reader = PyPDF2.PdfReader(BytesIO(file_bytes))
            if pdf_reader.is_encrypted:
                pdf_reader.decrypt(password)

            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        else:
            pdf = pdftotext.PDF(BytesIO(file_bytes))
            text = "\n".join(pdf)

        if text.strip():
            if translate_to_english:
                with st.spinner('Translating... This may take a moment.'):
                    text = translate_text(text)

            txt = st.text_area("Converted Text", text, height=300)
            st.success("Processing complete!")
        else:
            st.warning("No text could be extracted from the PDF. The file might be empty or contain only images.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
