# Credit Risk Evaluator

A smart web application developed using Streamlit that evaluates the credit risk of a loan applicant by analyzing their demographic, financial, and employment-related inputs. By leveraging a classification model, it efficiently identifies high-risk applicants, aiding in better credit approval decisions.

---

## 🌐 Live Website
You can try the tool live here: **[Credit Risk Evaluator](https://vaibhav-project-credit-risk-evaluator.streamlit.app/)**

---

## 🛠 Features  
- Visually appealing and interactive UI built with Streamlit.  
- Predicts loan default risk using various personal and financial attributes.  
- Estimates the probability that a loan applicant will default.  
- Maps predicted probability to a credit score between 300 and 900.  
- Categorizes applicants into risk tiers: Poor (300–499), Average (500–649), Good (650–749), Excellent (750–900).  
- Utilizes a pre-trained classification model for real-time predictions.  
- Handles categorical and numerical features with pre-fitted encoders and scalers.  
- Simple, fast, and deployable with no backend server required.  
- Lightweight codebase optimized for local or cloud usage.  

---

## 📂 Project Structure

```
Credit_Risk_Evaluator/
│
├── artifacts/
│   ├── model_data.joblib        # Serialized model and preprocessor 
│
├── main.py                      # Main Streamlit app logic
├── prediction_helper.py         # Logic for preprocessing and prediction
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation
```

---

## 🚀 How to Run Locally  
### Prerequisites:  
- Python 3.8+

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vaibhavgarg2004/Credit-Risk-Evaluator.git
   cd Credit-Risk-Evaluator
   ```
2. **Install dependencies**:   
   ```commandline
    pip install -r requirements.txt
   ```
5. **Run the Streamlit app**:   
   ```commandline
    streamlit run main.py
   ```

---

## 🧠 How It Works

1. **User Inputs**  
   - **Age** (years)  
   - **Annual Income**  
   - **Loan Amount**  
   - **Genetical Risk** (0 = none, 1 = low, 2 = moderate, 3 = high)  
   - **Insurance Plan** (e.g., Bronze, Silver, Gold)  
   - **Employment Status** (e.g., Salaried, Self-Employed, Unemployed)  
   - **Gender** (Male/Female)  
   - **Marital Status** (Married/Unmarried)  
   - **BMI Category** (Underweight, Normal, Overweight, Obese)  
   - **Smoking Status** (No Smoking / Smoker)  
   - **Region** (Northeast, Northwest, Southeast, Southwest)  
   - **Medical History** (No Disease / Has Disease)  

2. **Segmentation Logic**  
   - **Age <= 25** → Uses **`scaler_young.joblib`** and **`model_young.joblib`** (Linear Regression).
   - **Age > 25** → Uses **`scaler_rest.joblib`** and **`model_rest.joblib`** (XGBoost Regressor).

3. **Prediction Flow**  
   - Input data is preprocessed using the respective scaler.  
   - Features are passed to the appropriate model.  
   - The predicted premium cost is returned instantly.

---
   
## 🖼️ Application Snapshot

![Application UI](insurance_predictor_ui_mockup.png)

---

## 📄 License
This project is licensed under the **Apache License 2.0**. See the [LICENSE](./LICENSE) file for details.

---

*Don’t guess—predict. Discover your insurance premium with smart insights.*

