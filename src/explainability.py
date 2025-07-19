import shap
import matplotlib.pyplot as plt
import pandas as pd

def explain_with_shap(model, X_val, column_names, class_index=1):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_val)
    X_val_df = pd.DataFrame(X_val, columns=column_names)

    if isinstance(shap_values, list):  # multi-class
        shap.summary_plot(shap_values[class_index], X_val_df)
    else:
        shap.summary_plot(shap_values, X_val_df)
