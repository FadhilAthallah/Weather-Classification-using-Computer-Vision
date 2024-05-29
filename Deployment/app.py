# main.py

import streamlit as st
from eda import run_eda
from model_prediction import run_model_prediction

st.title("Weather Classification App by Image")
st.write("This machine can predict **cloudy**, **foggy**, **rainy**, **shine**, **sunrise**")
st.write("Model accuracy is 60% ")
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["EDA", "Model Prediction"])

    if selection == "EDA":
        run_eda()
    elif selection == "Model Prediction":
        run_model_prediction()

if __name__ == "__main__":
    main()
