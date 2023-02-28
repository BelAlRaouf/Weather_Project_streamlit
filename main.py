import streamlit as st
import plotly.express as px
from backend import get_data


st.title("You can check the weather here.")

locations = st.text_input("location: ")

days = st.slider("Select time period: ", min_value=1, max_value=5)
temperature_option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{temperature_option} or the next {days} days in {locations}")


d,t = get_data(locations, days, temperature_option)


d, t = get_date(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
