import streamlit as st
import plotly.express as px
st.title("You can check the weather here.")

locations = st.text_input("location: ")

days = st.slider("Select time period: ", min_value=1, max_value=5)
temperature_option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{temperature_option} or the next {days} days in {locations}")


def get_date(day):
    dates = ["2023-10-03", "2023-11-13", "2023-04-20"]
    temperatures = [12, 8, 19]
    temperatures = [day*i for i in temperatures]
    return dates, temperatures


d, t = get_date(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
