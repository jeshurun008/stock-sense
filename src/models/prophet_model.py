# src/models/prophet_model.py

from prophet import Prophet
import pandas as pd

def train_prophet(df, periods=7):
    """Train Prophet model and return forecast."""
    prophet_df = df[['date', 'sales']].rename(columns={'date': 'ds', 'sales': 'y'})
    model = Prophet(daily_seasonality=True)
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']].tail(periods)