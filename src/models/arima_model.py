# src/models/arima_model.py

from statsmodels.tsa.arima.model import ARIMA

def train_arima(df, order=(5,1,0)):
    """Train ARIMA model and return predictions."""
    df = df.set_index('date')
    model = ARIMA(df['sales'], order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=7)  # Example: 7-day forecast
    return forecast
