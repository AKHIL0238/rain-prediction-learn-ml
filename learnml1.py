import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🌧️ Rain Prediction App")

st.write("Enter the day's temperature values")

# Inputs
min_temp = st.number_input("Minimum Temperature (°C)", value=20.0)
max_temp = st.number_input("Maximum Temperature (°C)", value=30.0)

# Predict button
if st.button("Predict Rain"):
    input_data = np.array([[min_temp, max_temp]])
    prediction = model.predict(input_data)

    # if prediction[0] == 1:
st.success("🌧️ Rain is likely today")

        # Play rain sound
with open("rain.mp3", "rb") as f:
    st.audio(f.read(), autoplay=True)

st.markdown(
    """
    <style>
    audio { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)


    # else:
    #     st.info("☀️ No rain expected today")


