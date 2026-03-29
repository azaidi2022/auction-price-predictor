import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.predict import predict_spread

st.set_page_config(page_title="Auction Car Spread Predictor", layout="centered")

st.title("Auction Car Spread Predictor")
st.write("Estimate auction price deviation from MMR and expected sale price.")

with st.form("prediction_form"):
    year = st.number_input("Year", min_value=1980, max_value=2030, value=2015)
    make = st.text_input("Make", value="Toyota")
    model = st.text_input("Model", value="Camry")
    trim = st.text_input("Trim", value="LE")
    body = st.text_input("Body", value="Sedan")
    transmission = st.text_input("Transmission", value="automatic")
    state = st.text_input("State", value="TX")
    odometer = st.number_input("Odometer", min_value=0.0, value=85000.0)
    condition = st.number_input("Condition", min_value=0.0, max_value=5.0, value=4.0, step=0.1)
    color = st.text_input("Color", value="white")
    interior = st.text_input("Interior", value="black")
    saledate = st.text_input("Sale Date", value="2015-01-15")
    mmr = st.number_input("MMR", min_value=0.0, value=12000.0)

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "year": year,
        "make": make,
        "model": model,
        "trim": trim,
        "body": body,
        "transmission": transmission,
        "state": state,
        "odometer": odometer,
        "condition": condition,
        "color": color,
        "interior": interior,
        "saledate": saledate,
        "mmr": mmr,
    }

    try:
        predicted_spread = predict_spread(payload)
        estimated_sale_price = mmr + predicted_spread

        st.success("Prediction complete")

        st.metric("Predicted Spread", f"${predicted_spread:,.2f}")
        st.metric("MMR", f"${mmr:,.2f}")
        st.metric("Estimated Sale Price", f"${estimated_sale_price:,.2f}")

        if predicted_spread < 0:
            st.info("This vehicle is predicted to sell below MMR.")
        elif predicted_spread > 0:
            st.info("This vehicle is predicted to sell above MMR.")
        else:
            st.info("This vehicle is predicted to sell near MMR.")

    except Exception as e:
        st.error(f"Prediction failed: {e}")