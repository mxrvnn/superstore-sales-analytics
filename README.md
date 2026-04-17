# 📊 Superstore Sales Analytics

An end-to-end retail ML pipeline, from raw PostgreSQL data through 
to a live Streamlit app predicting order profitability in real time.

[Live App](https://superstore-profit-predictor.streamlit.app/) · [LinkedIn](https://www.linkedin.com/in/marvin-adu/)

---

## ✨ Technologies

- Python · Pandas · NumPy
- PostgreSQL · SQLAlchemy
- Scikit-learn · XGBoost · SHAP
- Matplotlib · Seaborn
- Streamlit · Git · GitHub

---

## 🚀 Features

- End-to-end data pipeline from raw CSV → PostgreSQL → ML model → live app
- EDA across 9,994 transactions uncovering profit drivers and loss patterns
- Two ML models trained and compared — Random Forest vs XGBoost
- SHAP explainability showing why each profit prediction was made
- Live Streamlit app for real-time profit prediction from order inputs

---

## 📊 Model Comparison

| Metric | Random Forest | XGBoost | Improvement |
|--------|--------------|---------|-------------|
| MAE    | $28.80       | $16.35  | 43%         |
| RMSE   | $118.11      | $4.04   | 97%         |
| R²     | 0.68         | 0.93    | 37%         |

XGBoost selected as the production model based on performance across all metrics.

---

## 🎯 Key Findings

- Discount rate is the second strongest profit predictor after sales volume, consistent across both models
- Sub-category copiers showed a distinct profit profile misattributed to sales volume by Random Forest
- Low value furniture orders with moderate discounts are consistently the lowest profit transactions
- SHAP analysis confirmed discount rate as the dominant factor in individual profit predictions

---

## 🔄 The Process

Started by loading the raw Superstore CSV into PostgreSQL using SQLAlchemy. 
A data cleaning script standardised column names, fixed data types, and 
engineered new features. Every notebook connects to the same `orders_clean` 
table.

EDA revealed two immediate findings: a heavily right-skewed sales distribution 
and transactions losing over $6,000, suggesting discount abuse on certain orders.

Two models were trained on an 80/20 split. Random Forest gave a solid baseline 
at R² 0.68. XGBoost improved every metric, most significantly RMSE dropped 
from $118 to $4, meaning XGBoost handles profit outliers dramatically better. 
SHAP was then applied to explain individual predictions, confirming discount 
rate as the dominant profit driver at the transaction level.

---

## 💡 What I Learned

**End-to-end thinking:** Every stage of the pipeline, from SQL table design 
to Streamlit deployment, affects every other stage. Building it all forced 
a systems-level perspective.

**Model selection is a decision:** Benchmarking Random Forest against XGBoost 
justified the additional complexity. The 97% RMSE improvement wasn't obvious 
until both models were evaluated side by side.

**Explainability matters:** SHAP turned a black-box model into a business tool. 
Showing *why* an order is predicted to lose money is more valuable than the 
prediction alone.

**Reproducibility from day one:** Clean venv, requirements.txt, structured 
Git commits, and SQL as a single source of truth meant the project could be 
rebuilt from scratch by anyone.

---

## 🔧 How Can It Be Improved?

- Log transformation on profit to reduce outlier impact on training
- Separate model for high-value outlier transactions
- Cross-validation for more robust evaluation
- Time series forecasting for monthly sales trends
- Expand Streamlit app with SHAP explanations per prediction

---

## ⚙️ Setup

1. Clone the repo
2. Create a virtual environment — `python -m venv venv`
3. Install dependencies — `pip install -r requirements.txt`
4. Add `.env` file with PostgreSQL credentials
5. Run in order:
   - `data_cleaning.py` — loads raw data into PostgreSQL
   - `01_eda.ipynb` — exploratory data analysis
   - `02_profit_prediction.ipynb` — Random Forest model
   - `03_xgboost_profit_prediction.ipynb` — XGBoost + SHAP
   - `streamlit run app.py` — launch the web app

---

## Contact

M.Adu1@Outlook.com  
[LinkedIn](https://www.linkedin.com/in/marvin-adu/)  
[GitHub](https://github.com/mxrvnn)
