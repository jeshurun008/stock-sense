# Stock Sense — Smart Forecasting & Inventory Dashboard

> Built with ARIMA, Prophet, LSTM & Streamlit  
> Forecast your sales, evaluate accuracy, and get reorder point recommendations — all in one dashboard.

---

## Features

- Forecasts using:
  - ARIMA
  - Prophet
  - LSTM (deep learning)
- Ensemble model for stable predictions
- Evaluation metrics: MAE, RMSE, MAPE
- Inventory Reorder Point calculation
- Web-based Streamlit dashboard

---

## Installation

**Requirements**: Python 3.12+

```bash
git clone https://github.com/YOUR_USERNAME/stock-sense.git
cd stock-sense
pip install -r requirements.txt
```

---

## Windows Fix: Enable Long Path Support

If you get this error while installing packages like TensorFlow:

```
OSError: [Errno 2] No such file or directory: ... tensorflow/include/...
```

You need to enable long paths in Windows:

### Option 1: Manually via Registry Editor

1. Press `Win + R`, type `regedit`, and press Enter.
2. Navigate to:
   ```
   Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
   ```
3. Find `LongPathsEnabled`
4. Double-click it and set the value to `1`
5. Restart your PC

### Option 2: Using PowerShell (Admin)

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

Then restart your PC.

---

## Running the App

```bash
streamlit run app/app.py
```

Open your browser and go to:
```
http://localhost:8501
```

---

## Project Structure

```
stock-sense/
├── app/
│   └── app.py
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── evaluation.py
│   ├── inventory.py
│   └── models/
│       ├── arima_model.py
│       ├── prophet_model.py
│       ├── lstm_model.py
│       └── ensemble.py
├── requirements.txt
└── README.md
```

---