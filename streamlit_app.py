import streamlit as st
import bitly_api

token = "49c4a71e8309dd60d68c3c4d3ad80e2c7021cf77"
connection = bitly_api.Connection(access_token=token)

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
        shorten_url = connection.shorten(url)
        st.success("Shortened URL: " + "**" + shorten_url.get('url') + "**")