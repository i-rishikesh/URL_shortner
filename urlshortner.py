import streamlit as st
import pyshorteners as pyst
shortener = pyst.Shortener()

st.markdown("<h1 style='text-align:center;'>URL SHORTNER</h1>", unsafe_allow_html=True)
form = st.form('name')
url = form.text_input('Enter URL')
s_btn= form.form_submit_button('Short')
if s_btn:
    short_url = shortener.tinyurl.short(url)
    st.title('Shortened URL')
    st.markdown(f"<h3>Shortened URL: {short_url}</h3>", unsafe_allow_html=True)
    st.button( "Copy", short_url)
    
