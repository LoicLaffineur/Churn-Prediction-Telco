# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# Load model and preprocessor
model = joblib.load("Streamlit_app/reg_log_model_churn.pkl")
scaler = joblib.load("Streamlit_app/scaler.pkl")
cols = joblib.load("Streamlit_app/features.pkl")  # List of features used in the model
X_test = joblib.load('Streamlit_app/X_test.pkl')

# App title
st.title("📉 Telco Customer Churn Prediction")

tab1, tab2, tab3 = st.tabs(["Prediction", "Individual SHAP", "Global SHAP"])

with tab1 : 
# Sidebar form
    st.sidebar.header("🧾Customer Information")
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
    MonthlyCharges = st.sidebar.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    TotalCharges = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 1500.0)
    Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
    
    # Convert to DataFrame
    input_dict = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
        'Contract': Contract,
        'InternetService': InternetService,
        'PaperlessBilling': PaperlessBilling
    }
    input_df = pd.DataFrame([input_dict])
    
    num=['tenure', 'MonthlyCharges', 'TotalCharges']
    
    # Preprocessing
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=cols, fill_value=0)
    input_scaled = input_encoded.copy()
    input_scaled[num] = scaler.transform(input_encoded[num])

    # Prediction
    proba = model.predict_proba(input_scaled)[0][1]
    st.subheader("🎯 Prediction Result")
    st.metric(label="Churn Probability", value=f"{proba*100:.2f} %")
    if proba > 0.29 : # Threshold found in the notebook
        st.warning("⚠️ This customer is at **high risk** of churn.")
    else:
        st.success("✅ This customer is at **low risk** of churn.")

with tab2 :
    
    st.title("💡 SHAP Explanation for the Selected Customer")
    st.subheader("🚨 Feature impact on churn prediction:")
    
    shap.initjs()
    
    explainer = shap.explainers.Linear(model, X_test, feature_names=cols)
    shap_values = explainer(input_scaled)
    
    # Helper function to plot
    def st_shap(plot, height=300):
        shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
        components.html(shap_html, height=height)
    
    # Old-style JS force plot (works in Streamlit)
    force_plot = shap.force_plot(
        explainer.expected_value,
        shap_values.values[0],
        input_scaled,
        matplotlib=False
    )
    
    st_shap(force_plot)

with tab3 : 
    
    st.header("🌍 Global SHAP Explanation") 
    st.subheader("📊 Feature importance across all customers")
    
    # Compute SHAP values for the whole X_test 
    
    explainer_global = shap.explainers.Linear(model, X_test, feature_names=cols) 
    shap_values_global = explainer_global(X_test) 
    
    # Display beeswarm plot 
    
    fig, ax = plt.subplots(figsize=(10, 6)) 
    shap.plots.beeswarm(shap_values_global, show=False) 
    st.pyplot(fig)
