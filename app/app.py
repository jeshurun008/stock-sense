# app/app.py

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

from src.preprocessing import clean_data
from src.feature_engineering import create_features
from src.evaluation import evaluate_model
from src.inventory import calculate_reorder_point
from src.models.arima_model import train_arima
from src.models.prophet_model import train_prophet
from src.models.lstm_model import train_lstm
from src.models.ensemble import ensemble_predictions


def create_dummy_data():
    """Generate dummy sales data for 60 days."""
    dates = [datetime.today() - timedelta(days=i) for i in range(60)]
    data = {
        'date': sorted(dates),
        'sales': [max(0, 100 + i % 10 - (i // 10) * 5) for i in range(60)]
    }
    return pd.DataFrame(data)


def main():
    st.set_page_config(page_title="Stock Sense", layout="centered")
    st.title("📊 Stock Sense - Forecasting Dashboard")

    df = create_dummy_data()
    st.subheader("📦 Raw Sales Data")
    st.dataframe(df.tail(10))

    df = clean_data(df)
    df = create_features(df)

    with st.spinner("🔵 Running ARIMA..."):
        arima_forecast = train_arima(df)

    with st.spinner("🟠 Running Prophet..."):
        prophet_forecast = train_prophet(df)

    with st.spinner("🟣 Running LSTM..."):
        lstm_forecast = train_lstm(df)

    arima_vals = arima_forecast[:7].values if hasattr(arima_forecast, 'values') else arima_forecast
    prophet_vals = prophet_forecast['yhat'].values
    ensemble = ensemble_predictions(arima_vals, prophet_vals)

    st.subheader("📈 Model Forecasts")
    st.write("🔵 ARIMA:", arima_forecast.values.tolist())
    st.write("🟠 Prophet:", prophet_vals.tolist())
    st.write(f"🟣 LSTM (1 day): {round(lstm_forecast, 2)}")
    st.write("🟡 Ensemble:", ensemble.tolist())

    metrics = evaluate_model(prophet_vals, ensemble)
    st.subheader("📏 Evaluation Metrics (vs Prophet)")
    st.json(metrics)

    reorder = calculate_reorder_point(pd.Series(ensemble), lead_time=5)
    st.subheader("📦 Inventory Recommendation")
    st.success(f"Reorder Point Suggestion: {round(reorder, 2)} units")


if __name__ == "__main__":
    main()
