# Streamlit Frontend
import streamlit as st
import datetime
import pandas as pd
from ai_engine import analyze_logs
from log_parser import parse_logs

st.title("Sentinel Copilot")

uploaded_file = st.file_uploader("Upload your log file (CSV)", type=["csv"])
if uploaded_file:
    logs = pd.read_csv(uploaded_file)
    parsed = parse_logs(logs)
    st.write("Parsed Logs:", parsed)
    summary = analyze_logs(parsed)
    st.subheader("AI Summary")
    st.write(summary)

    # --- Incident Report Download Button ---
    report_text = f"""Sentinel Copilot Incident Report
Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Log Analysis Summary:
{summary}
"""
    st.download_button(
        label="Download Incident Report",
        data=report_text,
        file_name=f"sentinel_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )
