# src/feature_engineering.py

def create_features(df):
    """Generate lag, rolling, and date-based features."""
    df = df.copy()
    df['dayofweek'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['lag_1'] = df['sales'].shift(1)
    df['rolling_mean_3'] = df['sales'].rolling(window=3).mean()
    df.dropna(inplace=True)
    return df
