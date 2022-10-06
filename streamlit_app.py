import streamlit as st
import bitly_api
from PIL import Image
import qrcode

<<<<<<< HEAD
#token = "49c4a71e8309dd60d68c3c4d3ad80e2c7021cf77"
c = bitly_api.Connection(access_token='49c4a71e8309dd60d68c3c4d3ad80e2c7021cf77')
#connection = bitly_api.Connection(access_token=token)
=======
c = bitly_api.Connection(access_token='7d2d5ab75fb4104d391501975235e0b3f1d55045')
>>>>>>> 50c3ef4f951413873fa6ed76c04c0ed64b5befd5

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
