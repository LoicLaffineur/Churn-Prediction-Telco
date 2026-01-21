# Réduisez votre taux de désabonnement client avec l'analyse prédictive.

## 🎯 Problématique client 
Dans le secteur du télécoms, acquérir des clients est une tâche bien plus couteuse que la fidélisation d'un client déjà existant. C'est pourquoi, identifier les clients susceptibles de se désabonner (ci-après churn) permet d'agir en amont et de réduire les pertes de revenus.
Comment identifier les abonnés à risques pour réduire les pertes d'un opérateur télécom ? 

## 💡 Notre solution : 
**Ma solution** :

- Nettoyage des données et Analyse exploratoire (EDA).
- Développement d’un modèle prédictif (Régression logistique, XGBoost) pour détecter les clients susceptibles de se désabonner.
- Optimisation du **Recall** (de 0.53 a 0.8) via ajustement des seuils.
- Interprétation des résultats avec SHAP pour identifier les variables clés (type de contrat, service internet, tenure).
  
Nous avons développer un modèle prédictif basé sur l'analyse des données, un modèle de Régression logistique et un ajustement des seuils afin de s'adapter à la différence des coûts entre un Faux Positif (churn non détecté) et un Faux Négatif (faussement cibler un individu) capable d'identifier les clients à risque de désabonnement avec 76% d'accuracy et **81% de Recall** (capacité à détecter les vrais clients à risque). Notre solution permet également d'identifier les variables discriminantes dans la décision de désabonnement afin de cibler ces individus avec des offres adaptées à leurs besoins. La solution intègre également une application StreamLit utilisable pour de futurs profils.

## 🛠️ Technologies utilisées  : 
Python, Pandas, Scikit-learn, XGBoost, Logistic Regression, Matplotlib, Seaborn, SHAP

## 🚀 Résultats attendus pour l'entreprise : 
- Réduction des coûts : Moins de perte = économies sur les campagnes d'acquisition.
- Amélioration de l'expérience client : Des offres proactives et adaptées pour les clients à risque.
- Prise de décision data-driven
  
## 📊 Visualisations : 

### Résulats finaux : 

<img width="619" height="628" alt="pr_churn" src="https://github.com/user-attachments/assets/7daf1994-0bb5-4933-ae0b-626b7ede9d88" />

<img width="485" height="401" alt="res_fin_churn" src="https://github.com/user-attachments/assets/13d3dfdd-f2eb-4f74-ac2e-eb8ff104079e" />

### Matrice de confusion finale : 

<img width="507" height="455" alt="cm_rl" src="https://github.com/user-attachments/assets/b52e5083-3deb-46a2-b6c5-f312312ef4e4" />

### SHAP : 

<img width="884" height="497" alt="shap" src="https://github.com/user-attachments/assets/b0310bce-93ba-4c4d-9713-2635d6f6dd11" />

## 🤖 Application Streamlit : 

[https://churnpython-rvye97ruvtvqtgwowbdmtz.streamlit.app/](https://laffineur-telco-churn.streamlit.app/)

<img width="1581" height="827" alt="str" src="https://github.com/user-attachments/assets/410022ff-663e-40c2-8af2-8b70522557a5" />
