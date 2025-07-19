import joblib
import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def save_model(model, path):
    joblib.dump(model, path)

def load_model(path):
    return joblib.load(path)

def save_predictions(preds, customer_ids, output_path):
    df = pd.DataFrame({
        'CustomerID': customer_ids,
        'Churn_Prediction': preds
    })
    df.to_csv(output_path, index=False)
