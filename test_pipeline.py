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

def run_pipeline(df=None):
    # Use dummy data if none provided
    if df is None:
        df = create_dummy_data()

    df = clean_data(df)
    df = create_features(df)

    # ARIMA
    arima_forecast = train_arima(df)

    # Prophet
    prophet_forecast = train_prophet(df)

    # LSTM
    lstm_forecast = train_lstm(df)

    # Ensemble (ARIMA + Prophet)
    arima_vals = arima_forecast[:7].values if hasattr(arima_forecast, 'values') else arima_forecast
    prophet_vals = prophet_forecast['yhat'].values
    ensemble = ensemble_predictions(arima_vals, prophet_vals)

    # Evaluate
    metrics = evaluate_model(prophet_vals, ensemble)

    # Inventory Suggestion
    reorder_point = calculate_reorder_point(pd.Series(ensemble), lead_time=5)

    return arima_vals, prophet_vals, lstm_forecast, ensemble, metrics, reorder_point, df
