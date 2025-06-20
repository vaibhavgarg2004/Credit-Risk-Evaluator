import streamlit as st
from prediction_helper import predict

# Page setup
st.set_page_config(page_title="Credit Risk Evaluator", page_icon="💳", layout="centered")

# Styled Header
st.markdown("""
    <div style="background-color:#e6f2ff; padding: 15px; border-radius: 12px; margin-bottom: 20px;">
        <h1 style="color: #003366; text-align: center; margin: 0; font-size: 28px;">
            💳 Credit Risk Evaluator
        </h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("## 🔎 Enter Applicant & Loan Information:")

# Input form
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('🎂 Age', min_value=18, max_value=100, step=1, value=28)
    with col2:
        income = st.number_input('💰 Annual Income (₹)', min_value=0, value=1200000, step=50000)
    with col3:
        loan_amount = st.number_input('🏦 Loan Amount (₹)', min_value=0, value=2560000, step=50000)

    loan_to_income_ratio = loan_amount / income if income > 0 else 0
    st.markdown(f"""
    <div style="font-size:14px; padding: 6px 0;">
        <span style="color: white;"><strong>📊 Loan-to-Income Ratio:</strong></span>
        <span style="color: limegreen; font-weight: bold;">{loan_to_income_ratio:.2f}</span>
    </div>
""", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    with col4:
        loan_tenure_months = st.number_input('⏳ Loan Tenure (Months)', min_value=0, value=36, step=1)
    with col5:
        loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
    with col6:
        loan_type = st.selectbox('🏷️ Loan Type', ['Secured', 'Unsecured'])

    col7, col8, col9 = st.columns(3)
    with col7:
        avg_dpd_per_delinquency = st.number_input('📉 Avg DPD (Days Past Due)', min_value=0, value=5)
    with col8:
        delinquency_ratio = st.slider('⚠️ Delinquency Ratio (%)', min_value=0, max_value=100, value=1)
    with col9:
        credit_utilization_ratio = st.slider('📈 Credit Utilization Ratio (%)', min_value=0, max_value=100, value=60)

    col10, col11 = st.columns(2)
    with col10:
        num_open_accounts = st.number_input('📂 Open Loan Accounts', min_value=1, max_value=10, value=2)
    with col11:
        residence_type = st.selectbox('🏡 Residence Type', ['Owned', 'Rented', 'Mortgage'])

# Calculate Button
calculate = st.button("🔍 Calculate Credit Risk")

# Horizontal Result Display
if calculate:
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )
    col_r1, col_r2, col_r3 = st.columns(3)
    with col_r1:
        st.metric(label="🧮 Default Probability", value=f"{probability:.2%}")
    with col_r2:
        st.metric(label="⭐ Credit Score", value=credit_score)
    with col_r3:
        st.metric(label="🏅 Rating", value=rating)
