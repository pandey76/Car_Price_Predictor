import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("car_price_model.pkl", "rb"))

# Encoding maps (match the LabelEncoder used in training)
transmission_map = {"Manual": 1, "Automatic": 0}
fuel_map = {"Petrol": 2, "Diesel": 1, "CNG": 0}  # adjust based on your dataset encoding
owner_map = {"First": 0, "Second": 1, "Third": 2, "Fourth & Above": 3}
tyre_map = {"Tubeless": 1, "Tube": 0}

st.title("🚗 Used Car Price Predictor")

# Inputs
trans = st.radio("Transmission", list(transmission_map.keys()))
fuel = st.selectbox("Fuel Type", list(fuel_map.keys()))
owner = st.selectbox("Owner Type", list(owner_map.keys()))
tyre = st.radio("Tyre Type", list(tyre_map.keys()))

km = st.number_input("Kilometers Driven", min_value=0, step=1000)
seats = st.selectbox("Number of Seats", [2, 4, 5, 6, 7, 8])
year = st.slider("Manufacturing Year", 1990, 2025, 2018)

# Convert year to age
car_age = 2025 - year

# Encode inputs
input_data = np.array([[ 
    transmission_map[trans],
    fuel_map[fuel],
    km,
    owner_map[owner],
    seats,
    tyre_map[tyre],
    car_age
]])

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Car Price: ₹ {round(prediction, 2):,.2f}")

