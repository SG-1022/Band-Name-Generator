import streamlit as st

st.title("Band Name Generator")

with st.form(key="Band Name Generator"):

    city = st.text_input("Enter your city")
    pet_name = st.text_input("Enter your pet name")


    submit_button = st.form_submit_button(label="Submit")


if submit_button:
    if city and pet_name:
        f"Your band name could be: "
        st.code(f"{city} {pet_name} Rockstars".title())
        st.balloons()
    else:
        st.warning("Please fill in all of the fields.")
