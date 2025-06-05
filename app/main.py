# Streamlit Frontend
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.ensemble import IsolationForest

# Dummy AI summary, replace with your own logic if needed
def analyze_logs(df):
    # Simple example, can be replaced with OpenAI/spaCy later
    if df.empty:
        return pd.DataFrame([{"Summary": "No logs to analyze.", "Severity": "Low"}])
    events = df["event_type"].value_counts().to_dict()
    summary = f"Top event types: {events}"
    severity = "High" if any('fail' in k.lower() for k in events) else "Low"
    return pd.DataFrame([{"Summary": summary, "Severity": severity}])

st.set_page_config(page_title="Sentinel Copilot", layout="wide")
st.title("Sentinel Copilot")

# Theme toggle is NOT native to Streamlit, so just go with system preference via config.toml

# --- File upload & sample ---
st.write("Upload your log file (CSV) or try a sample log file instantly.")
col1, col2 = st.columns([2, 1])
uploaded_file = col1.file_uploader("Choose a log file", type=["csv"], label_visibility="collapsed")
load_sample = col2.button("Load Sample Data")
sample_path = "sample_logs/example_log.csv"

logs = None
filename = None
if uploaded_file:
    logs = pd.read_csv(uploaded_file)
    filename = uploaded_file.name
elif load_sample:
    logs = pd.read_csv(sample_path)
    filename = "example_log.csv"
    st.success("Loaded sample log data!")

# --- Filtering & features ---
if logs is not None:
    st.write(f"**Parsed Logs:** ({filename})")

    with st.expander("🗃️ Preview: First 5 Log Entries (Raw Data)", expanded=False):
        st.dataframe(logs.head(), use_container_width=True, hide_index=True)

    st.subheader("📉 Summary Stats")
    total_events = len(logs)
    unique_ips = logs["source_ip"].nunique() if "source_ip" in logs else 0
    unique_events = logs["event_type"].nunique() if "event_type" in logs else 0
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Events", total_events)
    c2.metric("Unique Source IPs", unique_ips)
    c3.metric("Unique Event Types", unique_events)

    most_event = logs["event_type"].value_counts().idxmax() if "event_type" in logs else "-"
    most_event_count = logs["event_type"].value_counts().max() if "event_type" in logs else "-"
    noisiest_ip = logs["source_ip"].value_counts().idxmax() if "source_ip" in logs else "-"
    noisiest_ip_count = logs["source_ip"].value_counts().max() if "source_ip" in logs else "-"
    st.info(f"🚦 **Most Frequent Event:** {most_event} ({most_event_count} times)\n\n"
            f"🛑 **Noisiest Source IP:** {noisiest_ip} ({noisiest_ip_count} events)")

    # --- INTERACTIVE FILTERS ---
    st.subheader("🔍 Search & Filter Logs")
    filter_col1, filter_col2, filter_col3, filter_col4 = st.columns([3, 2, 2, 1])
    search_term = filter_col1.text_input("Search logs for keyword (case-insensitive):", "")
    event_types = logs["event_type"].dropna().unique().tolist() if "event_type" in logs else []
    src_ips = logs["source_ip"].dropna().unique().tolist() if "source_ip" in logs else []
    selected_events = filter_col2.multiselect("Filter by Event Type", event_types, default=event_types)
    selected_ips = filter_col3.multiselect("Filter by Source IP", src_ips, default=src_ips)
    clear_filters = filter_col4.button("Clear All Filters")

    if clear_filters:
        selected_events = event_types
        selected_ips = src_ips
        search_term = ""

    st.subheader("📅 Filter by Date Range")
    if "timestamp" in logs.columns:
        logs["timestamp"] = pd.to_datetime(logs["timestamp"])
        min_date, max_date = logs["timestamp"].min().date(), logs["timestamp"].max().date()
        if min_date < max_date:
            date_start, date_end = st.slider(
                "Select date range (UTC):",
                min_value=min_date, max_value=max_date,
                value=(min_date, max_date),
                format="YYYY-MM-DD"
            )
        else:
            date_start = date_end = min_date
            st.info(f"All logs are from a single day: {min_date}. No date range to select.")
    else:
        date_start = date_end = None

    # Apply filters
    filtered = logs.copy()
    if search_term.strip():
        filtered = filtered[
            filtered.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        ]
    if selected_events and "event_type" in filtered.columns:
        filtered = filtered[filtered["event_type"].isin(selected_events)]
    if selected_ips and "source_ip" in filtered.columns:
        filtered = filtered[filtered["source_ip"].isin(selected_ips)]
    if date_start and date_end and "timestamp" in filtered.columns:
        filtered = filtered[(filtered["timestamp"].dt.date >= date_start) & (filtered["timestamp"].dt.date <= date_end)]

    # --- Export filtered logs ---
    st.download_button(
        label="Download Filtered Logs (CSV)",
        data=filtered.to_csv(index=False).encode("utf-8"),
        file_name="filtered_logs.csv",
        mime="text/csv"
    )

    st.dataframe(filtered, use_container_width=True, hide_index=True)

    # --- VISUALIZATIONS ---
    st.subheader("📊 Log Visualizations")
    if "event_type" in filtered.columns and not filtered.empty:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        filtered["event_type"].value_counts().plot(kind="bar", ax=ax, color="#4D8CF4")
        ax.set_title("Event Type Frequency")
        ax.set_xlabel("Event Type")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    if "source_ip" in filtered.columns and not filtered.empty:
        fig2, ax2 = plt.subplots(figsize=(6, 3.5))
        filtered["source_ip"].value_counts().head(10).plot(kind="bar", ax=ax2, color="#C162F7")
        ax2.set_title("Top Source IPs")
        ax2.set_xlabel("Source IP")
        ax2.set_ylabel("Count")
        st.pyplot(fig2)
    if "timestamp" in filtered.columns and len(filtered["timestamp"].dt.date.unique()) > 1:
        fig3, ax3 = plt.subplots(figsize=(7, 3))
        filtered.set_index("timestamp").resample("D").size().plot(ax=ax3, marker='o')
        ax3.set_title("Events per Day")
        ax3.set_xlabel("Date")
        ax3.set_ylabel("Count")
        st.pyplot(fig3)

    # --- 🧠 ANOMALY DETECTION (NEW) ---
    st.subheader("🧠 Anomaly Detection (Machine Learning)")
    if not filtered.empty:
        feature_cols = []
        if "source_ip" in filtered.columns:
            filtered["ip_int"] = filtered["source_ip"].apply(lambda ip: int(''.join(['{:03}'.format(int(x)) for x in ip.split('.')])) if isinstance(ip, str) and ip.count('.') == 3 else 0)
            feature_cols.append("ip_int")
        if "event_type" in filtered.columns:
            filtered["event_type_code"] = filtered["event_type"].astype("category").cat.codes
            feature_cols.append("event_type_code")
        if "timestamp" in filtered.columns:
            filtered["timestamp_int"] = filtered["timestamp"].astype(np.int64) // 10**9
            feature_cols.append("timestamp_int")
        if feature_cols:
            clf = IsolationForest(contamination=0.08, random_state=42)
            preds = clf.fit_predict(filtered[feature_cols])
            filtered["anomaly"] = preds
            anomalies = filtered[filtered["anomaly"] == -1]
            normal = filtered[filtered["anomaly"] == 1]
            st.write(f"Flagged **{len(anomalies)} potential anomalies** (out of {len(filtered)}) using Isolation Forest ML.")
            if not anomalies.empty:
                st.dataframe(anomalies.drop(columns=["ip_int", "event_type_code", "timestamp_int", "anomaly"], errors="ignore"), 
                             use_container_width=True, hide_index=True)
            else:
                st.info("No anomalies detected in filtered logs.")
            st.write("Distribution (anomalies in red):")
            fig, ax = plt.subplots(figsize=(5, 2))
            ax.scatter(filtered.index, [1]*len(filtered), c=['red' if a == -1 else 'blue' for a in filtered["anomaly"]], s=12)
            ax.set_yticks([])
            ax.set_xlabel("Log Entry Index")
            ax.set_title("Anomaly Detection: Red = Flagged Event")
            st.pyplot(fig)
        else:
            st.info("Not enough data for anomaly detection. Make sure your logs include IP and event type columns.")
    else:
        st.info("No data to analyze for anomalies.")

    # --- AI SUMMARY ---
    st.subheader("🤖 AI Summary")
    summary = analyze_logs(filtered)
    def highlight_high_severity(row):
        color = "background-color: #FF6F6F; font-weight: bold" if row.get("Severity") == "High" else ""
        return [color if col == "Severity" else "" for col in row.index]
    styled_summary = summary.style.apply(highlight_high_severity, axis=1)
    st.write(styled_summary)

    # --- INCIDENT REPORT DOWNLOAD ---
    report_text = f"""Sentinel Copilot Incident Report
Date: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC

Log Analysis Summary:
{summary.to_string(index=False)}
"""
    st.download_button(
        label="Download Incident Report",
        data=report_text,
        file_name=f"sentinel_report_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )

else:
    st.info("Upload a CSV log file or click 'Load Sample Data' to get started.")

# --- FOOTER ---
st.markdown("""
---
Built by [Teshera Kimbrough](https://www.linkedin.com/in/tesherakimbrough/)  
[GitHub](https://github.com/tesherakimbrough/sentinel-copilot)
""")
