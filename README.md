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

<img width="619" height="628" alt="pr_churn" src="https://github.com/user-attachments/assets/35446916-b358-461f-9889-c2ed320d995e" />

### Confusion Matrix

<img width="1454" height="690" alt="CM_churn" src="https://github.com/user-attachments/assets/756b2009-280d-40a8-ade4-36a678342a27" />

### SHAP Interpretability

<img width="884" height="497" alt="beeswarm_churn" src="https://github.com/user-attachments/assets/8185866b-df6a-4d23-a8ef-16b566436d62" />

<img width="1309" height="186" alt="force_churn" src="https://github.com/user-attachments/assets/76374e56-8f24-44fe-a34e-3c27147761bc" />

## 🤖 Streamlit Application

#### 🔗 Live demo:  

https://laffineur-telco-churn.streamlit.app/

<img width="1470" height="711" alt="Streamlit_1" src="https://github.com/user-attachments/assets/9ad144cf-6aab-4e6f-95b3-6a2eebe9052a" />

<img width="1470" height="711" alt="Streamlit_2" src="https://github.com/user-attachments/assets/ed1848cb-5e7c-4d0a-b571-f51db18355ef" />

<img width="1470" height="711" alt="Streamlit_3" src="https://github.com/user-attachments/assets/48699e58-24d2-4c46-bee2-47e31757e41d" />


