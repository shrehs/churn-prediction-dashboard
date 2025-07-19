```markdown
# 📊 Customer Churn Prediction Dashboard

A Streamlit-powered dashboard that predicts customer churn using a trained LightGBM model and preprocessing pipeline. Upload customer data in CSV format and get instant predictions with probabilities.

<img width="1878" height="854" alt="Screenshot 2025-07-19 182103" src="https://github.com/user-attachments/assets/a39ab577-66cb-40ae-819f-ecba3a59de60" />
<img width="1892" height="859" alt="Screenshot 2025-07-19 182119" src="https://github.com/user-attachments/assets/b481e774-3c08-449c-829d-efb4d7b515ff" />

---

## 🚀 Features

- 📁 Upload customer CSV file
- 🧠 Predict churn using a trained LightGBM model
- 📉 Display churn probability for each record
- 📥 Download results as a CSV
- ✅ Modular architecture with clean pipeline and utils

---

## 🧠 Model Info

- **Model:** LightGBM Classifier
- **Preprocessing:** Scikit-learn pipeline with numerical & categorical encodings
- **Output:** Binary classification + probability score

---

## 📁 Project Structure

```

customer-churn-dashboard/
├── app/
│   └── churn\_dashboard.py        # Main Streamlit app
├── models/
│   └── final\_model\_lgbm.pkl      # Trained LightGBM model
├── output/
│   └── preprocessing\_pipeline.joblib  # Preprocessing pipeline
├── src/
│   ├── pipeline.py               # Function to create preprocessing pipeline
│   ├── utils.py                  # Load model, handle paths
│   └── explainability.py         # SHAP explanations
├── requirements.txt
├── .gitignore
└── README.md

````

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/customer-churn-dashboard.git
   cd customer-churn-dashboard
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   streamlit run app/churn_dashboard.py
   ```

---

## 📌 How to Use

1. Upload a `.csv` file containing customer data.
2. The app will preprocess it using the saved pipeline.
3. Predictions and churn probabilities will be shown.
4. Download the results using the download button.

---

## 🛠 Tech Stack

* **Frontend**: Streamlit
* **Backend**: LightGBM, Scikit-learn
* **Data Handling**: Pandas, NumPy
* **Model Storage**: Joblib

---

## 📤 Deployment 

You can deploy this app using [Streamlit Cloud](https://streamlit.io/cloud):

* Make sure your repo includes `requirements.txt`

---

## 👩‍💻 Author

**Shreya H S**
👩‍🔬 ML & Cloud Engineering Enthusiast
🌐 [LinkedIn](https://www.linkedin.com/in/shreyahs/) | ✨ [GitHub](https://github.com/shreyahs)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
