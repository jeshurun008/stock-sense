import pandas as pd
from datetime import datetime, timedelta

# Import your modules
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

def run_pipeline():
    df = create_dummy_data()
    print("\n📦 Raw Data Sample:")
    print(df.head())

    df = clean_data(df)
    df = create_features(df)

    # ARIMA
    arima_forecast = train_arima(df)
    print(f"\n🔵 ARIMA forecast:\n{arima_forecast}")

    # Prophet
    prophet_forecast = train_prophet(df)
    print(f"\n🟠 Prophet forecast:\n{prophet_forecast}")

    # LSTM
    lstm_forecast = train_lstm(df)
    print(f"\n🟣 LSTM forecast (1 day ahead): {lstm_forecast}")

    # Ensemble (ARIMA + Prophet)
    arima_vals = arima_forecast[:7].values if hasattr(arima_forecast, 'values') else arima_forecast
    prophet_vals = prophet_forecast['yhat'].values
    ensemble = ensemble_predictions(arima_vals, prophet_vals)
    print(f"\n🟡 Ensemble forecast:\n{ensemble}")

    # Evaluate
    print("\n📏 Evaluation:")
    print(evaluate_model(prophet_vals, ensemble))

    # Inventory Suggestion
    reorder_point = calculate_reorder_point(pd.Series(ensemble), lead_time=5)
    print(f"\n📦 Reorder Point Suggestion: {reorder_point:.2f}")

if __name__ == "__main__":
    run_pipeline()
