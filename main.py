import streamlit as st
import requests

# init web page
st.set_page_config(layout="centered")

# set parameters for request nasa api
api = "mqqWKKUXLL9fWVyUHNokL4ujxvFkMpwWOiQtckif"
url = "https://api.nasa.gov/planetary/apod?"  \
      f"api_key={api}"

# get source from api
response = requests.get(url)
# convert json form
content = response.json()
# get image url
img = requests.get(content["url"]).content
# create image
with open("image.jpg", "+wb") as file:
    file.write(img)


# create web page
st.header(content["title"])
st.image("image.jpg")
st.write(content["explanation"])



