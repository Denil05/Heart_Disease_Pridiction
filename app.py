import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


try:
    model = joblib.load('random_forest_model.pkl')
    scaler = joblib.load('scaler.pkl')
except FileNotFoundError:
    st.error("Model or scaler file not found. Please ensure 'random_forest_model.pkl' and 'scaler.pkl' are in the same directory as 'app.py'.")
    st.stop()


st.title('Heart Disease Prediction')

st.write('Enter patient information to predict the likelihood of heart disease.')

with st.form("patient_form"):
    st.header("Demographics")
    age = st.slider('Age', 29, 77, 54)
    sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')

    st.header("Clinical Measurements")
    trestbps = st.slider('Resting Blood Pressure (trestbps)', 94, 200, 130)
    chol = st.slider('Serum Cholesterol (chol)', 126, 564, 246)
    thalach = st.slider('Maximum Heart Rate Achieved (thalach)', 71, 202, 149)
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest (oldpeak)', 0.0, 6.2, 1.0)

    st.header("Medical History")
    cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3], format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
    fbs = st.selectbox('Fasting Blood Sugar (fbs > 120 mg/dl)', [0, 1], format_func=lambda x: 'False' if x == 0 else 'True')
    restecg = st.selectbox('Resting Electrocardiographic Results (restecg)', [0, 1, 2], format_func=lambda x: ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'][x])
    exang = st.selectbox('Exercise Induced Angina (exang)', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    slope = st.selectbox('Slope of the Peak Exercise ST Segment (slope)', [0, 1, 2], format_func=lambda x: ['Upsloping', 'Flat', 'Downsloping'][x])
    ca = st.selectbox('Number of Major Vessels (ca)', [0, 1, 2, 3, 4])
    thal = st.selectbox('Thalassemia (thal)', [0, 1, 2, 3], format_func=lambda x: ['Unknown', 'Normal', 'Fixed Defect', 'Reversible Defect'][x])

    submitted = st.form_submit_button('Predict')


input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                           columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])


scaled_input_data = scaler.transform(input_data)



if 'submitted' in locals() and submitted:
    prediction = model.predict(scaled_input_data)
    if prediction[0] == 1:
        st.write('The model predicts that this patient is likely to have heart disease.')
    else:
        st.write('The model predicts that this patient is unlikely to have heart disease.')

