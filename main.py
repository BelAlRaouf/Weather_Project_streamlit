import math

import streamlit as st
import plotly.express as px
from backend import get_data


st.title("You can check the weather here.")

locations = st.text_input("location: ")

days = st.slider("Select time period: ", min_value=1, max_value=5)
temperature_option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{temperature_option} or the next {days} days in {locations}")

try:
    if locations:
        filtered_data = get_data(locations, days)

        if temperature_option == "Temperature":
            temperatures = [math.floor(dict["main"]["temp"]*10)/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures"})
            st.plotly_chart(figure)
        if temperature_option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            images_path = [images[condition] for condition in sky_condition]
            temperatures = [math.floor(dict["main"]["temp"]*10)/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            st.image(images_path, width=120, caption=temperatures)
except KeyError:
    st.info("Please enter Valid City Name.")
