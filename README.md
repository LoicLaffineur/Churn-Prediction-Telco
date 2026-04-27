# Predict & Prevent Customer Churn

Help telecom or subscription companies identify at‑risk customers before they leave.

## The Problem

In telecom and subscription‑based businesses:

- Retaining an existing customer is much cheaper than acquiring a new one  
- Losing customers quietly leads to revenue erosion  
- Teams often react too late, after the customer has already left  

By the time billing or support notice the churn, it’s often too expensive to bring them back.

## The Approach

This project builds a predictive pipeline to identify customers at high risk of churn.

Key components:

- Data cleaning and exploratory analysis  
- Predictive models: Logistic Regression and XGBoost  
- Threshold optimization to improve recall (0.53 → 0.80)  
- Model explainability with SHAP (why a customer is flagged)  
- Interactive Streamlit app for real‑time predictions  

The goal: surface at‑risk customers early so teams can act in time.

## Results

- **81% recall** → 8 out of 10 customers who will churn are identified  
- Accuracy around **76%** → acceptable balance between sensitivity and false positives  
- Threshold optimization improves recall from **0.53 to 0.80**  
- SHAP identifies key churn drivers: contract type, internet service, and customer tenure  

Translation:  
You can proactively target a large share of at‑risk customers before they leave.

## How This Can Be Used in a Company

This pipeline can be used to:

- Flag high‑risk customers in a CRM or customer dashboard  
- Trigger targeted retention campaigns (SMS, email, call)  
- Prioritize proactive outreach for high‑value or long‑tenure customers  
- Improve collaboration between analytics, marketing, and customer success  

Example:  
A telecom team can run this model weekly and prioritize offers to the top‑risk customers to reduce churn.

## Business Impact

- Reduce customer churn and associated revenue loss  
- Lower acquisition costs by focusing on retention  
- Personalize offers based on churn risk and key drivers  
- Turn churn data into proactive, not reactive, decisions  

## Tech Stack

- Python
- Pandas
- Scikit‑learn
- XGBoost
- Logistic Regression
- SHAP
- Streamlit

## Model Insights

### Performance Overview

- ![PR curves](assets/PR_Curves.png)  
  Shows how the model behaves across different thresholds.

- ![Confusion matrix](assets/Confusion_matrix.png)  
  Reveals true positives, false positives, and other outcomes.

### Explainability

- ![Global SHAP](assets/Global_SHAP.png)  
  Main features driving churn at the population level.

- ![Individual SHAP](assets/Individual_SHAP.png)  
  Why a specific customer is flagged as high‑risk.

## Streamlit Application (Interactive Demo)

**Live demo:** [https://laffineur-telco-churn.streamlit.app/](https://laffineur-telco-churn.streamlit.app/)  

- ![Streamlit prediction screen](assets/Streamlit_pred.png)  
  Real‑time prediction for a given customer profile.  

- ![Global SHAP in Streamlit](assets/Streamlit_Global_SHAP.png)  
  High‑level churn drivers.  

- ![Individual SHAP in Streamlit](assets/Streamlit_individual_SHAP.png)  
  Customer‑level explanations.

## Work With Me

I help companies predict and reduce customer churn with data and machine learning.

I can help you:
- Build churn prediction models tailored to your business  
- Identify key churn drivers and translate them into actions  
- Design dashboards or apps for teams (support, marketing, customer success)  
- Turn risk scores into targeted retention campaigns  

Available for freelance projects.
