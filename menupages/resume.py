import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

annotations = []

def main():
    st.markdown('''
    <div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    Resume File
    </div>''', unsafe_allow_html=True)
    
    with open("static/resume.pdf", "rb") as f:
        pdf = f.read()
    
    st.download_button(
        label="Download resume",
        data=pdf,
        file_name="resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    
    pdf_viewer("static/resume.pdf", annotations=annotations)