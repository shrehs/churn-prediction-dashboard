# app/churn_dashboard.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import joblib
import numpy as np

from src.pipeline import create_pipeline
from src.utils import load_model
# from src.explainability import explain_prediction  

# Load artifacts
model = load_model("models/final_model_lgbm.pkl")
pipeline = joblib.load("output/preprocessing_pipeline.joblib")

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("📊 Customer Churn Prediction Dashboard")

# Upload CSV or manual entry
upload = st.file_uploader("Upload Customer CSV file", type=["csv"])

if upload is not None:
    df = pd.read_csv(upload)
    st.write("📄 Uploaded Data Preview:")
    st.dataframe(df.head())

    # Preprocess
    try:
        processed = pipeline.transform(df)
        preds = model.predict(processed)
        probs = model.predict_proba(processed)[:, 1]

        df["Churn Prediction"] = preds
        df["Churn Probability"] = probs.round(3)

        st.success("✅ Prediction Complete")
        st.dataframe(df[["Churn Prediction", "Churn Probability"]].join(df.drop(columns=["Churn Prediction", "Churn Probability"])))
        
        st.download_button("📥 Download Results", df.to_csv(index=False), file_name="churn_predictions.csv")

    except Exception as e:
        st.error(f"Processing Failed: {e}")

else:
    st.info("📌 Upload a CSV file to get started")
