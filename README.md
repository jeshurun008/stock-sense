# Stock Sense

Stock Sense is a lightweight, AI-powered inventory forecasting app that helps you predict sales and determine optimal reorder points using time series models like ARIMA, Prophet, and LSTM. Built with Streamlit for easy deployment.

---

## Features

- Upload your own sales data in CSV or Excel format.
- Forecast sales using ARIMA, Prophet, and LSTM models.
- Visualize forecasts and evaluate model accuracy.
- Get intelligent reorder point suggestions based on lead time.
- Easy-to-use Streamlit interface for quick testing and demos.

---

## Live Demo

> Coming soon...

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/jeshurun008/stock-sense.git
cd stock-sense
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Note: If you face errors related to `prophet`, install the pre-requirements first:

```bash
pip install --upgrade pip setuptools wheel
pip install Cython
```

### 4. Enable `cmdstanpy` for Prophet (Windows Only)

If Prophet fails with Stan backend errors, run the following steps:

- Open `cmd` and type:

```bash
gpedit.msc
```

- Navigate to:

```
Computer Configuration > Administrative Templates > System > Specify settings for optional component installation
```

- Enable it, then run:

```bash
pip install prophet
```

---

## Run the App

```bash
streamlit run app/app.py
```

---

## Data Format

Your CSV/Excel file must contain two columns:

| date                | sales |
|---------------------|-------|
| 2025-08-05 21:15:12 | 100   |
| 2025-08-06 21:15:12 | 95    |
| ...                 | ...   |

- `date`: timestamp or date string
- `sales`: numeric sales data

You can test with the default dummy dataset if no file is uploaded.

---

## Customizing the Model

All the backend logic resides in `test_pipeline.py`. You can modify:

- Data cleaning
- Feature engineering
- Models used
- Evaluation metrics
- Inventory logic

This gives you full flexibility to play with different forecasting strategies.

---

## Folder Structure

```
stock_sense/
│
├── app/                    # Streamlit UI
│   └── app.py
│
├── src/                    # Core logic
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── evaluation.py
│   ├── inventory.py
│   └── models/
│       ├── arima_model.py
│       ├── prophet_model.py
│       ├── lstm_model.py
│       └── ensemble.py
│
├── input/                  # Optional user CSVs/XLSX files
├── test_pipeline.py        # Model orchestration logic
├── requirements.txt
└── README.md
```

---

## License

MIT © Jeshurun008
