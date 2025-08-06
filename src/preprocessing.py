# src/preprocessing.py

import pandas as pd

def clean_data(df):
    """Clean raw sales data."""
    df = df.copy()
    df.dropna(inplace=True)  # Basic example
    df = df[df['sales'] >= 0]  # Remove negative sales
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)
    return df
