# Quantity Demand Forecasting (Retail)

## Project Overview
This project builds an end-to-end machine learning pipeline to forecast product demand for a small retail catalog (Synthetic Data)

The goal is to predict quantity given signals like price, product, calendar features, and lagged demand. 

## Data
- Synthetic retail dataset (1 year of daily data, ~25 products)
- Columns include:
  - `date`, `product_id`, `category`
  - `price`, `quantity`, `revenue`
  - calendar features: `week`, `day_of_week`, `month`, `is_weekend`
  - engineered features: product aggregates, lags, rolling means

## Modeling
- Target: `quantity` (demand)
- Model: `RandomForestRegressor` in a scikit-learn `Pipeline`
- Final tuned model R² ≈ 0.82 on held-out data

## Key Insights
- Price, lagged quantity, and category are strong drivers of demand.
- Weekend and monthly seasonality also impact quantity.
- The model generalizes well, with stable R² and low error across folds.

## App
A simple Streamlit app allows interactive:
- Input of product info and price
- Predicted quantity output
