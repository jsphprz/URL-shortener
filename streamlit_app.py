import streamlit as st
from PIL import Image
import qrcode
import pyshorteners
import os
from urllib.parse import urlparse

st.set_page_config(
    page_title="URL Shortener",
    page_icon="🔗"
)

API_KEY = st.secrets.get("BITLY_API_KEY")

st.title('URL Shortener 🔗')
st.text("URL Shortener using Bitly API")

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

with st.form('input_url'):
    url = st.text_input(label="Enter URL:")
    
    if st.form_submit_button('Confirm'):
        if not url:
            st.error("Please enter a URL")
        elif not is_valid_url(url):
            st.error("Please enter a valid URL (include http:// or https://)")
        else:
            try:
                c = pyshorteners.Shortener(api_key=API_KEY)
                shorten_url = c.bitly.short(url)
                st.success(f"Shortened URL: **{shorten_url}**")
                
                img = qrcode.make(shorten_url)
                img.save("url.jpg")
                image = Image.open("url.jpg")
                
                st.image(image, caption="QR Code", width=200)
                
                os.remove("url.jpg")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")