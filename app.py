import streamlit as st
from summarizer import summarize_text
from utils import extract_text_from_pdf, extract_text_from_docx

st.set_page_config(page_title="Smart Study Notes Summarizer", page_icon="🧠")

st.title("🧠 Smart Study Notes Summarizer")
st.markdown("Upload your academic notes or research papers and get a concise AI-generated summary.")

uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])
model_choice = st.selectbox("Select summarization model", ["bart", "t5"])
summary_length = st.selectbox("Select summary length", ["short", "medium", "detailed"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_docx(uploaded_file)

    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = summarize_text(text, model_choice, summary_length)
        st.subheader("📋 Summary:")
        st.write(summary)
        st.download_button("Download Summary", summary, file_name="summary.txt")
