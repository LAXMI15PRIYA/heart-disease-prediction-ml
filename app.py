import streamlit as st
import joblib
import numpy as np

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main{
    background-color:#f4f8fb;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

h1{
    color:#d32f2f;
    text-align:center;
}

h3{
    color:#1565c0;
}

div.stButton > button{
    width:100%;
    background:#d32f2f;
    color:white;
    height:55px;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    border:none;
}

div.stButton > button:hover{
    background:#b71c1c;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/heart-with-pulse.png",
        width=80
    )

    st.title("Heart Disease App")

    st.markdown("---")

    st.subheader("Model")

    st.success("Logistic Regression")

    st.subheader("Preprocessing")

    st.info("StandardScaler")

    st.subheader("Features")

    st.write("13 Medical Features")

    st.markdown("---")

    st.caption(
        "Built using\n\n"
        "• Streamlit\n"
        "• Scikit-Learn\n"
        "• NumPy\n"
        "• Joblib"
    )

    st.markdown("---")

st.markdown("### 🔗 Project Links")

st.markdown(
    "[GitHub Repository](https://github.com/LAXMI15PRIYA/heart-disease-prediction-ml)"
)
st.markdown("---")

with st.expander("📈 Model Performance"):

    st.write("**Model:** Logistic Regression")
    st.write("**Preprocessing:** StandardScaler")
    st.write("**Features:** 13")
    st.write("**Training Accuracy:** 85.25%")

# ==========================================
# HEADER
# ==========================================

st.title("❤️ Heart Disease Prediction System")

st.markdown("""
### 🩺 AI-Powered Heart Disease Risk Assessment

This application predicts whether a patient is at risk of heart disease
using a trained **Machine Learning Logistic Regression model**.

Please enter the patient's medical information below.
""")
st.info("⚠️ This application is for educational purposes only and should not replace professional medical advice.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🤖 Model", "Logistic Regression")

with col2:
    st.metric("⚙️ Scaling", "StandardScaler")

with col3:
    st.metric("📊 Features", "13")

st.divider()

st.subheader("📝 Patient Information")

left, right = st.columns(2)
# ==========================================
# LEFT COLUMN
# ==========================================

with left:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=45,
        help="Age of the patient in years."
    )

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )
    sex = 1 if sex == "Male" else 0

    chest_pain = {
        "Typical Angina": 0,
        "Atypical Angina": 1,
        "Non-anginal Pain": 2,
        "Asymptomatic": 3
    }

    cp_name = st.selectbox(
        "Chest Pain Type",
        chest_pain.keys()
    )

    cp = chest_pain[cp_name]

    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=80,
        max_value=250,
        value=120
    )

    chol = st.number_input(
        "Serum Cholesterol (mg/dl)",
        min_value=100,
        max_value=600,
        value=200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        ["No", "Yes"]
    )

    fbs = 1 if fbs == "Yes" else 0

    ecg = {
        "Normal": 0,
        "ST-T Wave Abnormality": 1,
        "Left Ventricular Hypertrophy": 2
    }

    restecg_name = st.selectbox(
        "Resting ECG",
        ecg.keys()
    )

    restecg = ecg[restecg_name]
    # ==========================================
# RIGHT COLUMN
# ==========================================

with right:

    thalach = st.number_input(
        "Maximum Heart Rate Achieved",
        min_value=60,
        max_value=250,
        value=150
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        ["No", "Yes"]
    )

    exang = 1 if exang == "Yes" else 0

    oldpeak = st.number_input(
        "Old Peak",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    slope_dict = {
        "Upsloping": 0,
        "Flat": 1,
        "Downsloping": 2
    }

    slope_name = st.selectbox(
        "Slope",
        slope_dict.keys()
    )

    slope = slope_dict[slope_name]

    ca = st.selectbox(
        "Number of Major Vessels",
        [0, 1, 2, 3, 4]
    )

    thal_dict = {
        "Normal": 1,
        "Fixed Defect": 2,
        "Reversible Defect": 3
    }

    thal_name = st.selectbox(
        "Thal",
        thal_dict.keys()
    )

    thal = thal_dict[thal_name]
    st.divider()

if st.button("🔍 Predict Heart Disease", use_container_width=True):

    patient = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    # Scale input
    patient_scaled = scaler.transform(patient)

    # Prediction
    prediction = model.predict(patient_scaled)
    probability = model.predict_proba(patient_scaled)

    low_risk = float(probability[0][0])
    high_risk = float(probability[0][1])

    st.divider()
    st.subheader("📊 Prediction Result")

    if prediction[0] == 1:
        st.error("❤️ High Risk of Heart Disease")
    else:
        st.success("💚 Low Risk of Heart Disease")

    st.subheader("📈 Prediction Probability")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Low Risk", f"{low_risk*100:.2f}%")
        st.progress(low_risk)

    with col2:
        st.metric("High Risk", f"{high_risk*100:.2f}%")
        st.progress(high_risk)

    st.divider()

    st.subheader("💡 Health Recommendations")

    if prediction[0] == 1:
        st.warning("""
### Recommendations

- 🩺 Consult a cardiologist.
- 🥗 Follow a heart-healthy diet.
- 🚶 Exercise regularly (after medical advice).
- 🚭 Avoid smoking and alcohol.
- ❤️ Monitor blood pressure and cholesterol.
- 📅 Schedule regular health checkups.
""")
    else:
        st.success("""
### Recommendations

- 🥗 Maintain a healthy balanced diet.
- 🚶 Continue regular exercise.
- ❤️ Keep blood pressure under control.
- 😴 Get enough sleep every day.
- 💧 Stay hydrated.
- 📅 Continue regular health checkups.
""")

st.divider()

st.caption("❤️ Built with Streamlit | Scikit-Learn | NumPy | Joblib")