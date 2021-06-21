import streamlit as st
import bitly_api
from PIL import Image
import qrcode
import cv2

#token = "49c4a71e8309dd60d68c3c4d3ad80e2c7021cf77"
c = bitly_api.Connection(access_token='49c4a71e8309dd60d68c3c4d3ad80e2c7021cf77')
d = cv2.QRCodeDetector()
#connection = bitly_api.Connection(access_token=token)

st.set_page_config(
        page_title="URL Shortener",
        page_icon="🔗"
    )

header = st.beta_container()
body = st.beta_container()

with header:
    st.title('URL Shortener 🔗')

with body:
    st.text("URL Shortener using Bitly API")

with st.form('input_url'):
    url = st.text_input(label = "Enter URL:")
    if st.form_submit_button('Confirm'):
        shorten_url = c.shorten(url)
        st.success("Shortened URL: " + "**" + shorten_url.get('url') + "**")
        col1, col2, col3, col4, col5, col6 = st.beta_columns([1,6,1,6,1,6])
        img = qrcode.make(url)
        img.save("url.jpg")
        image = Image.open("url.jpg")
        with col3:
            st.image(image, caption="QR Code", width=200, output_format='auto')