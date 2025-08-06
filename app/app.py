import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from test_pipeline import run_pipeline

st.set_page_config(
    page_title="Stock Sense Dashboard",
    layout="wide",
)

# ----- Custom Styling -----
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        h1, h2, h3 {
            font-family: 'Segoe UI', sans-serif;
            font-weight: 600;
        }
        .block-container {
            padding: 2rem 2rem 2rem 2rem;
        }
        .metric-box {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Stock Sense - Forecasting Dashboard")

# ----- Sidebar file uploader -----
st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

# ----- Run pipeline -----
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            user_data = pd.read_csv(uploaded_file, encoding="utf-8", engine="python")
        else:
            user_data = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error loading uploaded file: {e}")
        user_data = None
else:
    user_data = None

# ----- Run forecasting pipeline -----
arima, prophet, lstm, ensemble, eval_metrics, reorder_point, raw_data = run_pipeline(user_data)

# ----- Layout -----
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Raw Sales Data")
    st.dataframe(raw_data, use_container_width=True)

with col2:
    st.subheader("📈 Model Forecasts")
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=arima, name="ARIMA", mode="lines+markers"))
    fig.add_trace(go.Scatter(y=prophet, name="Prophet", mode="lines+markers"))
    fig.add_trace(go.Scatter(y=ensemble, name="Ensemble", mode="lines+markers"))
    fig.update_layout(height=400, margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ----- Metrics -----
col3, col4, col5, col6 = st.columns(4)

with col3:
    st.metric("LSTM Forecast (1 Day)", f"{lstm:.2f}")
with col4:
    st.metric("MAE", f"{eval_metrics['MAE']:.2f}")
with col5:
    st.metric("RMSE", f"{eval_metrics['RMSE']:.2f}")
with col6:
    st.metric("MAPE", f"{eval_metrics['MAPE']:.2f}%")

st.markdown("---")

# ----- Inventory Suggestion -----
st.subheader("📦 Inventory Recommendation")
st.success(f"Reorder Point Suggestion: {reorder_point:.2f} units")
