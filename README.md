# Heart Disease Prediction

A machine learning web application that predicts the likelihood of heart disease based on patient medical data using a Random Forest model.

## 🎯 Project Overview

This application uses a trained Random Forest model to predict heart disease risk based on various clinical parameters including:
- Demographics (age, sex)
- Clinical measurements (blood pressure, cholesterol, heart rate)
- Medical history (chest pain type, ECG results, exercise-induced angina)

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for easy data input
- **Real-time Predictions**: Instant heart disease risk assessment
- **Comprehensive Input Form**: Covers all relevant medical parameters
- **User-friendly Design**: Intuitive sliders and dropdown menus

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:8501`
   - The application will open automatically

3. **Enter patient data**
   - Fill in the demographic information
   - Input clinical measurements
   - Provide medical history details

4. **Get prediction**
   - Click "Predict" button
   - View the heart disease risk assessment

## 📊 Model Information

- **Algorithm**: Random Forest Classifier
- **Features**: 13 medical parameters
- **Training**: Cross-validation with k-fold
- **Performance**: Optimized for accuracy and interpretability

## 📁 Project Structure

```
heart-disease-prediction/
├── app.py                 # Main Streamlit application
├── sources.py             # Data processing and model training
├── random_forest_model.pkl # Trained Random Forest model
├── scaler.pkl             # Data scaler for preprocessing
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔧 Technical Details

### Input Parameters
- **Age**: Patient age (29-77 years)
- **Sex**: Gender (0=Female, 1=Male)
- **Chest Pain Type**: Type of chest pain experienced
- **Resting Blood Pressure**: Blood pressure at rest
- **Serum Cholesterol**: Cholesterol level in mg/dl
- **Fasting Blood Sugar**: Blood sugar level
- **Resting ECG**: Electrocardiographic results
- **Maximum Heart Rate**: Peak heart rate achieved
- **Exercise-Induced Angina**: Angina during exercise
- **ST Depression**: ST depression induced by exercise
- **Slope**: Slope of peak exercise ST segment
- **Major Vessels**: Number of major vessels
- **Thalassemia**: Thalassemia type

### Output
- **Prediction**: Binary classification (0=No heart disease, 1=Heart disease likely)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

---

**Note**: This is a machine learning model and should be used responsibly. The predictions are based on statistical patterns and may not be 100% accurate for all individuals. 
