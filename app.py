import streamlit as st
import pandas as pd
import pickle 

#Loading xgboost model
import os

model_path = os.path.join(os.path.dirname(__file__), "xgboost_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

#App title
st.title("Superstore Profit Predictor")
st.write("Enter order details below to predict the expected profit.")

#User inputs
sales = st.number_input("Sales Amount ($)", min_value=0.0, value=100.0)
quantity = st.number_input("Quantity Amount", min_value=1, value=1)
discount = st.slider("Discount", min_value=0.0, max_value=1.0, value=0.0, step=0.05)

category = st.selectbox("Category", ["furniture", "office supplies", "technology"])

sub_category = st.selectbox("Sub-Category", [
    "accessories", "appliances", "art", "binders", "bookcases",
    "chairs", "copiers", "envelopes", "fasteners", "furnishings",
    "labels", "machines", "paper", "phones", "storage", "supplies", "tables"
])

region = st.selectbox("Region", ["central", "east", "south", "west"])
segment = st.selectbox("Segment", ["consumer", "corporate", "home office"])
ship_mode = st.selectbox("Ship Mode", [
    "first class", "same day", "second class", "standard class"
])

# Predict button
if st.button("Predict Profit"):

    # Build input dataframe
    input_data = pd.DataFrame([{
        'sales': sales,
        'quantity': quantity,
        'discount': discount,
        f'category_{category}': 1,
        f'sub-category_{sub_category}': 1,
        f'region_{region}': 1,
        f'segment_{segment}': 1,
        f'ship_mode_{ship_mode}': 1
    }])

    # Add missing dummy columns with 0
    model_columns = model.get_booster().feature_names
    for col in model_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    # Reorder columns to match training data
    input_data = input_data[model_columns]

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction >= 0:
        st.success(f"Predicted Profit: ${round(prediction, 2)}")
    else:
        st.error(f"Predicted Loss: ${round(prediction, 2)}")