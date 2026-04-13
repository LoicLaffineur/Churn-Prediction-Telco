# Reduce Customer Churn with Predictive Analytics

## Business Problem

In the telecom industry, acquiring new customers is significantly more expensive than retaining existing ones.
Identifying subscribers at high risk of churn enables proactive retention strategies and prevents substantial revenue loss.

How can we detect at-risk customers before they leave?

## Proposed Solution

Full end-to-end predictive pipeline to identify customers likely to churn and support targeted retention actions.

**Key steps:**

- Data cleaning and exploratory data analysis (EDA)
- Predictive models: Logistic Regression, XGBoost
- Threshold optimization to maximize Recall (0.53 → 0.80)
- Model interpretability with SHAP — key churn drivers identified
- Deployment as an interactive Streamlit app for real-time predictions

## Results

| Metric | Score |
|--------|-------|
| Accuracy | 76% |
| Recall | 81% |
| Threshold optimization | 0.53 → 0.80 recall |

SHAP analysis identifies the main churn drivers: contract type, internet service, customer tenure.

## Technologies

Python · Pandas · Scikit-learn · XGBoost · Logistic Regression · SHAP · Streamlit · Matplotlib · Seaborn

## Business Impact

- Fewer lost customers → lower acquisition costs
- Personalized retention offers for high-risk profiles
- Actionable insights into churn drivers for marketing teams

## Model Results

### Final Performance

<img width="619" height="628" alt="pr_churn" src="assets/PR_Curves" />

### Confusion Matrix

<img width="1454" height="690" alt="CM_churn" src="assets/Confusion_Matrix" />

### SHAP Interpretability

<img width="884" height="497" alt="beeswarm_churn" src="assets/Global_SHAP" />

<img width="1309" height="186" alt="force_churn" src="assets/Individual_SHAP" />

## Streamlit Application

**Live demo:** https://laffineur-telco-churn.streamlit.app/

<img width="1470" height="711" alt="Streamlit_1" src="assets/Streamlit_pred" />

<img width="1470" height="711" alt="Streamlit_2" src="assets/Streamlit_Global_SHAP" />

<img width="1470" height="711" alt="Streamlit_3" src="assets/Streamlit_individual_SHAP" />
