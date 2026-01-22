# 📉 Reduce Customer Churn with Predictive Analytics

## 🎯 Business Problem
In the telecom industry, acquiring new customers is significantly more expensive than retaining existing ones.
Identifying subscribers at high risk of churn enables proactive retention strategies and prevents substantial revenue loss.

How can we detect at‑risk customers before they leave the company?

## 💡 Proposed Solution
This project develops a full end‑to‑end predictive pipeline to identify customers likely to churn and support targeted retention actions.

### Key steps:

- Data cleaning and exploratory data analysis (EDA)
- Development of predictive models (Logistic Regression, XGBoost)
- Threshold optimization to maximize Recall (from 0.53 → 0.80)
- Model interpretability using SHAP to highlight the most influential features
- Deployment of an interactive Streamlit application for real‑time predictions

The final model achieves 76% accuracy and 81% Recall, making it highly effective at detecting true churners — the most critical metric for telecom retention teams.
SHAP analysis reveals the main drivers of churn, such as contract type, internet service, and customer tenure, enabling targeted and cost‑efficient retention campaigns.

## 🛠️ Technologies
Python • Pandas • Scikit‑learn • XGBoost • Logistic Regression • Matplotlib • Seaborn • SHAP • Streamlit

## 🚀 Business Impact

- Cost reduction: fewer lost customers → lower acquisition costs
- Improved customer experience: personalized retention offers for high‑risk profiles
- Data‑driven decision‑making: clear insights into churn drivers

## 📊 Model Results

### Final Performance

### Confusion Matrix

### SHAP Interpretability

## 🤖 Streamlit Application

#### 🔗 Live demo:  
https://laffineur-telco-churn.streamlit.app/ (laffineur-telco-churn.streamlit.app in Bing)

<img width="1581" height="827" alt="str" src="https://github.com/user-attachments/assets/410022ff-663e-40c2-8af2-8b70522557a5" />
