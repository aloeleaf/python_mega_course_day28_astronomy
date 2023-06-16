import streamlit as st
import requests

st.set_page_config(layout="wide")

# set parameters for request nasa api
api = "mqqWKKUXLL9fWVyUHNokL4ujxvFkMpwWOiQtckif"
url = "https://api.nasa.gov/planetary/apod?"  \
      f"api_key={api}"

response = requests.get(url)
content = response.json()
img = response.content["url"]

with open("image.jpg", "+rb") as img:
    file.write(img)



#st.header("Nasa pictures")
#st.image(content["url"])
st.write(content["explanation"])



