import streamlit as st
import pandas as pd
from model import predict_water_usage, get_model_accuracy

# Page configuration
st.set_page_config(
    page_title="Smart Water Usage Advisor",
    page_icon="💧",
    layout="centered"
)

# Title
st.title("💧 Smart Water Usage Advisor")
st.write("AI-based system to predict daily water consumption")

st.divider()

# User inputs
people = st.number_input("Number of People", min_value=1, value=2)
showers = st.number_input("Number of Showers per Day", min_value=0, value=2)
laundry = st.number_input("Laundry Cycles per Day", min_value=0, value=1)

# Prediction button
if st.button("Predict Water Usage"):
    prediction = predict_water_usage(people, showers, laundry)

    st.subheader("📌 Prediction Result")
    st.success(f"Estimated Daily Water Usage: {prediction:.2f} liters")

    # Smart suggestions
    if prediction > 800:
        st.error("⚠️ High water usage detected! Reduce showers or laundry cycles.")
    elif prediction > 500:
        st.warning("⚠️ Moderate water usage. Try optimizing daily activities.")
    else:
        st.info("✅ Water usage is within a sustainable range.")

# Model accuracy
st.divider()
st.subheader("📈 Model Performance")
st.info(f"Model Accuracy (R² Score): {get_model_accuracy():.2f}")

# Data visualization
st.divider()
st.subheader("📊 Sample Water Usage Data")
data = pd.read_csv("water_usage_data.csv")
st.line_chart(data["usage"])
