# src/models/lstm_model.py

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def train_lstm(df, epochs=10):
    """Train LSTM on sales data and return prediction."""
    scaler = MinMaxScaler()
    scaled_sales = scaler.fit_transform(df['sales'].values.reshape(-1, 1))

    X, y = [], []
    for i in range(3, len(scaled_sales)):
        X.append(scaled_sales[i-3:i, 0])
        y.append(scaled_sales[i, 0])
    
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    model = Sequential()
    model.add(LSTM(units=50, activation='relu', input_shape=(X.shape[1], 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=epochs, verbose=0)

    last_window = scaled_sales[-3:].reshape(1, 3, 1)
    prediction = model.predict(last_window)
    return scaler.inverse_transform(prediction)[0][0]
