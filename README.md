# Stock Sense 📊

**Stock Sense** is a machine learning-powered sales forecasting dashboard that uses ARIMA, Prophet, LSTM, and Ensemble models to predict sales and suggest inventory reorder points. Built with Python and Streamlit, it provides a clean UI for visualization and analysis.

---

## 🔧 Features

- Clean and interactive **Streamlit** dashboard
- Time series forecasting using:
  - **ARIMA**
  - **Facebook Prophet**
  - **LSTM**
  - **Ensemble (ARIMA + Prophet)**
- Evaluation Metrics: MAE, RMSE, MAPE
- Inventory reorder point recommendation
- Upload your own sales data via `.csv` or `.xlsx`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/jeshurun008/stock_sense_v1.git
cd stock_sense_v1
```

### 2. Setup Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 If Prophet fails to install, install `Cython` first:
```bash
pip install Cython
```

---

## 🧠 Running the App

```bash
streamlit run app/app.py
```

Once running, open `http://localhost:8501` in your browser.

---

## 🗂 How to Use

- The app loads sample/mock sales data by default.
- Use the sidebar to upload your own `.csv` or `.xlsx` file.
- Your file should contain two columns: `date` and `sales`.
- Once uploaded, the models will re-run with your data.

---

## 📁 File Structure

```
stock_sense_v1/
│
├── app/                  # Streamlit UI
│   └── app.py
│
├── src/                  # Source code
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
├── test_pipeline.py      # Pipeline script (core logic)
├── requirements.txt
└── README.md
```

---

## ⚙️ For Windows Users

If you face errors running `prophet`, enable long paths in Windows Registry:

1. Press `Win + R`, type `regedit`, press Enter.
2. Navigate to:  
   `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
3. Find key `LongPathsEnabled` → Set value to `1`
4. Restart your PC.

---

## 👤 Author

**Jeshurun Pearl Daniel**  
GitHub: [@jeshurun008](https://github.com/jeshurun008)

---

## 📜 License

MIT License
