# Streamlit Frontend
import streamlit as st
from ai_engine import analyze_logs
from log_parser import parse_logs

import pandas as pd

st.title("Sentinel Copilot")

uploaded_file = st.file_uploader("Upload your log file (CSV)", type=["csv"])
if uploaded_file:
    logs = pd.read_csv(uploaded_file)
    parsed = parse_logs(logs)
    st.write("Parsed Logs:", parsed)
    summary = analyze_logs(parsed)
    st.subheader("AI Summary")
    st.write(summary)
