# Superstore Sales Analytics

An end-to-end retail ML pipeline built with Python and PostgreSQL — 
from raw data through to a live Streamlit app predicting order 
profitability in real time.

---

## Technologies

- Python
- PostgreSQL & SQLAlchemy
- Pandas & NumPy
- Scikit-learn & XGBoost
- Matplotlib & Seaborn
- Streamlit
- Git & GitHub

---

## Project Status

- [x] Exploratory Data Analysis
- [x] Random Forest — R² 0.68, MAE $28.80
- [ ] XGBoost + model comparison
- [ ] SHAP explainability
- [ ] Streamlit deployment

---

## Features

- **Data Pipeline:** Raw CSV loaded into PostgreSQL, cleaned and 
  transformed in Python, structured into an orders_clean table 
  that feeds every notebook
- **EDA:** Six visualisations uncovering sales distribution, 
  profit outliers, and category performance across 9,994 transactions
- **ML Model:** Random Forest Regressor predicting order profit — 
  sales volume and discount rate identified as primary drivers
- **Streamlit App:** Input order details and get a live profit 
  prediction (in progress)

---

## The Process

Firstly, I started by loading the raw Superstore CSV into a PostgreSQL 
database using SQLAlchemy, cleaning and standardising the data 
in Python before any analysis began. This meant every notebook 
pulled from a single clean source of truth rather than a flat file.

For the EDA I focused on understanding the distribution of sales 
and profit, which immediately revealed two things: a heavily 
right-skewed sales distribution and transactions with losses of 
over £6,000, suggesting discount abuse on certain orders.

For the ML model I chose Random Forest Regressor as a robust 
first model that handles mixed data types without heavy 
preprocessing. After encoding categorical variables and splitting 
the data 80/20, the baseline model achieved R² of 0.68 and MAE 
of $28.80. The feature importance chart confirmed discount rate 
as the second strongest predictor of profit after sales volume.

XGBoost and a Streamlit deployment are the next steps, the goal 
is a live app where a user can input order details and receive 
a profit prediction in real time.

---

## What I Learned

**End-to-end thinking:** Building the pipeline from PostgreSQL 
through to a trained model taught me to think about data flow 
across every stage, not just individual notebooks in isolation.

**Model interpretation matters more than accuracy:** An R² of 
0.68 is useful, but the feature importance chart, highlighting that 
discount rate is a stronger profit predictor than product category,
is what makes the model actionable for a business.

**RMSE vs MAE tell different stories:** My MAE of £28.80 looked 
strong but RMSE of $118.11 revealed the model struggles with 
extreme outlier transactions. That gap taught me more about my 
data than the model accuracy itself did.

**Virtual environments and reproducibility:** Setting up a clean 
venv, registering it as a Jupyter kernel, and maintaining a 
requirements.txt taught me how to build projects that others 
can actually run — not just notebooks that work on my machine.

---

## How Can It Be Improved?

- Apply log transformation to profit to reduce the impact of 
  extreme outliers on model performance
- Build a separate model for high-value outlier transactions
- Add time series forecasting for monthly sales trends
- Expand features — include shipping duration and regional 
  economic indicators
- Add cross-validation instead of a single train/test split 
  for more robust evaluation

---

## Setup

1. Clone the repo
2. Create a virtual environment
3. Install dependencies
4. Add a .env file with your PostgreSQL credentials
5. Run in order:
   - `data_cleaning.py` — loads raw data into PostgreSQL
   - `01_eda.ipynb` — exploratory data analysis
   - `02_profit_prediction.ipynb` — Random Forest model

---

## Video Demo

Coming soon — Streamlit app walkthrough

---

## Contact

📧 M.Adu1@Outlook.com  
💼 [LinkedIn](https://www.linkedin.com/in/marvin-adu/)
