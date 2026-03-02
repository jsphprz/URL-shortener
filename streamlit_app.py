import streamlit as st
from PIL import Image
import qrcode
import pyshorteners
import os
import io
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
                
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=30,
                    border=4,
                )
                qr.add_data(url)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                buf = io.BytesIO()
                img.save(buf, format="PNG")
                buf.seek(0)
                
                st.image(buf, caption="QR Code")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")