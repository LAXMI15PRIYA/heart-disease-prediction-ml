<div align="center">

# ❤️ Heart Disease Prediction System

### AI-Powered Risk Assessment Web App | Machine Learning · Streamlit · Deployment

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-Educational-lightgrey)]()

**[🚀 Live Demo](https://heart-disease-prediction-ml-zewwcqrssxuzr8b3urtueg.streamlit.app)** &nbsp;|&nbsp; **[📂 Source Code](https://github.com/LAXMI15PRIYA/heart-disease-prediction-ml)**

</div>

---

## 📌 About the Project

A complete, deployed **end-to-end Machine Learning application** that predicts a patient's risk of heart disease from 13 clinical parameters, using a **Logistic Regression** model trained on the UCI Heart Disease dataset. The project covers the full pipeline: **data preprocessing → model training → evaluation → building an interactive UI → cloud deployment.**

> ⚠️ **Disclaimer:** Built for educational and portfolio purposes only. Not intended for real medical diagnosis.

---

## 🖥️ Demo

| Patient Input Form | Risk Prediction Output |
|:---:|:---:|
| ![Input](screenshots/input-screenshot.png) | ![Result](screenshots/result-screenshot.png) |

---

## 🎯 What This Project Demonstrates

- ✅ Ability to take an ML model from **training to a live, usable product**
- ✅ Clean **data preprocessing** using `StandardScaler`
- ✅ Building an **interactive, user-friendly UI** with Streamlit and custom CSS
- ✅ Working with **real-world healthcare data** and interpreting model probabilities
- ✅ **Deploying and hosting** a live ML application on Streamlit Cloud
- ✅ Writing clean, structured, well-documented Python code

---

## ✨ Features

- 🔍 Predicts heart disease risk from 13 medical features in real time
- 📊 Shows prediction confidence with Low Risk vs High Risk probability bars
- 💡 Generates personalized health recommendations based on the result
- 🎨 Clean, responsive UI with custom-styled components
- ⚡ Instant predictions powered by a pre-trained, serialized model

---

## 🧠 Model Details

| Component | Details |
|---|---|
| **Algorithm** | Logistic Regression |
| **Preprocessing** | StandardScaler |
| **Features Used** | 13 clinical parameters |
| **Training Accuracy** | 85.25% |
| **Dataset** | UCI Heart Disease Dataset (303 records) |

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python |
| **ML / Data** | Scikit-Learn, NumPy, Pandas |
| **Model Persistence** | Joblib |
| **Web App / UI** | Streamlit |
| **Deployment** | Streamlit Community Cloud |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```
heart-disease-prediction-ml/
│
├── app.py                     # Main Streamlit application
├── heart_disease_model.pkl    # Trained Logistic Regression model
├── scaler.pkl                 # Fitted StandardScaler
├── heart-disease.csv          # Dataset used for training
├── requirements.txt           # Python dependencies
├── screenshots/                # App screenshots for this README
└── README.md                  # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/LAXMI15PRIYA/heart-disease-prediction-ml.git
cd heart-disease-prediction-ml
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📝 Input Parameters

The app takes the following 13 medical features as input:

| Feature | Description |
|---|---|
| Age | Age of the patient |
| Sex | Male / Female |
| Chest Pain Type | Typical Angina, Atypical Angina, Non-anginal, Asymptomatic |
| Resting Blood Pressure | In mm Hg |
| Serum Cholesterol | In mg/dl |
| Fasting Blood Sugar | > 120 mg/dl (Yes/No) |
| Resting ECG | Normal, ST-T Abnormality, Left Ventricular Hypertrophy |
| Max Heart Rate Achieved | Numeric value |
| Exercise-Induced Angina | Yes/No |
| Old Peak | ST depression induced by exercise |
| Slope | Upsloping, Flat, Downsloping |
| Number of Major Vessels | 0–4 |
| Thal | Normal, Fixed Defect, Reversible Defect |

---

## 🔮 Future Improvements

- [ ] Add more ML models (Random Forest, XGBoost) and compare performance
- [ ] Add SHAP/feature-importance explainability for predictions
- [ ] Add unit tests for the preprocessing and prediction pipeline
- [ ] Containerize with Docker for easier deployment

---

## 👩‍💻 Author

**Lakshmi Priya**
M.Tech AI & Data Science | Aspiring AI Engineer / Data Analyst

🔗 [GitHub](https://github.com/LAXMI15PRIYA) &nbsp;|&nbsp; 🌐 [Live App](https://heart-disease-prediction-ml-zewwcqrssxuzr8b3urtueg.streamlit.app)

---

## 📄 License

This project is open source and available for educational use.

---

<div align="center">

⭐ If you found this project interesting, consider giving it a star!

</div>
