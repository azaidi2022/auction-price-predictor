# Auction Profit Decision System

## Overview
This project is an end-to-end machine learning system designed to estimate vehicle resale value and support purchase decisions in car auctions.

Instead of only predicting price, the system helps determine whether a vehicle is worth buying by estimating potential profit and risk.

---

## Problem
Car dealers and auction buyers operate under uncertainty:

- Vehicle prices vary based on condition, mileage, and region  
- Repair costs and resale values are difficult to estimate  
- Poor purchase decisions can lead to significant losses  
- Most existing tools provide only price estimates and do not assist with decision-making  

---

## Solution
This system combines machine learning with simple financial modeling to provide actionable insights:

- Predicts resale value using historical auction data  
- Models uncertainty using quantile regression  
- Estimates profit based on purchase price and repair cost  
- Outputs a buy/pass recommendation  

---

## Approach

### Target Definition
Instead of predicting raw price, the model predicts: spread = selling_price - mmr


This improves generalization across different price ranges.

---

### Model
- CatBoost Regressor  
- Chosen for strong performance on tabular data  

---

### Uncertainty Modeling
- P10: conservative estimate  
- P50: expected estimate  
- P90: optimistic estimate  

---

## Decision Framework
total_investment = purchase_price + repair_cost
profit = predicted_resale - total_investment



Outputs:
- Expected profit  
- Profit range  
- Buy / Pass recommendation  

---

## Application
A Streamlit web application allows users to:

- Input vehicle details  
- Enter purchase price and repair cost  
- Receive real-time predictions and recommendations  

---

## Tech Stack
- Python  
- Pandas, NumPy  
- CatBoost  
- scikit-learn  
- Streamlit  

---

## Project Structure
auction-price-predictor/
│── data/
│── model/
│── app/
│── notebooks/
│── requirements.txt
│── README.md



---

## How to Run

```bash
git clone https://github.com/azaidi2022/auction-price-predictor.git
cd auction-price-predictor
pip install -r requirements.txt
streamlit run app/streamlit_app.py
