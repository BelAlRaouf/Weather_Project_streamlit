import streamlit as st

st.title("You can check the weather here.")

location = st.text_input("location: ")

day = st.slider("Select time period: ", min_value=1, max_value=5)
temperature_option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{temperature_option} or the next {day} days in {location}")
