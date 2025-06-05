![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-3776AB?logo=matplotlib)
![MIT License](https://img.shields.io/badge/License-MIT-green)

![Sentinel Copilot Banner](./banner.png)

# Sentinel Copilot

**Sentinel Copilot** is a security log analysis tool designed to help you turn raw CSV logs into meaningful insights—fast. Upload your logs, explore interactive visualizations, and get instant summaries that help you spot trends or suspicious activity.

Try it live: [sentinel-copilot.streamlit.app](https://sentinel-copilot.streamlit.app/)

---

## Why I Built This

I work in security analysis and I’m teaching myself software engineering. After spending too many hours buried in log files, I wanted a tool that’s quick, visual, and actually useful—no advanced degree needed. Sentinel Copilot is my solution: upload a file, get results, and get on with your day.

---

## Quick Start

1. **Clone the repository**
    ```bash
    git clone https://github.com/tesherakimbrough/sentinel-copilot.git
    cd sentinel-copilot
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**
    ```bash
    streamlit run app/main.py
    ```

Or try it instantly on the [live Streamlit demo](https://sentinel-copilot.streamlit.app/).

---

## What Makes Sentinel Copilot Different?

- **Dark/Light Mode Toggle:** Pick your favorite theme for comfort.
- **Interactive Filtering:** Search, sort, and filter logs by IP, event type, date, or keywords.
- **Visual Summaries:** Instant charts for event frequency, source IP activity, and more.
- **Downloadable Reports:** Export summaries or filtered logs as CSV with one click.
- **No AI Hype—Just Useful Automation:** Mock “AI summary” is built in, and it’s ready for plug-and-play with OpenAI if you want to add GPT-based analysis later.
- **Open Source & Easy to Extend:** Clean codebase and modular structure. Fork away.

---

## Features at a Glance

- Upload log files (CSV)
- See top events and “noisiest” IPs right away
- Explore interactive charts and tables
- Filter logs by any field (including by date)
- Toggle between dark and light themes
- Download filtered results or summaries

---

## Architecture Overview

```text
User Uploads Log File
       ↓
Log Parser (Python/pandas)
       ↓
AI Summary (mock/table, ready for OpenAI integration)
      ├── Visualizations (matplotlib/Streamlit)
      └── Downloadable Report

```

## Sample Data

You can test Sentinel Copilot right away with the provided `sample_logs/example_log.csv`.

Preview:

| timestamp           | source_ip    | event_type    |
|---------------------|-------------|---------------|
| 2025-06-01T12:00:00Z| 192.168.1.1 | login_success |
| 2025-06-01T12:05:00Z| 10.0.0.5    | login_failure |
| 2025-06-01T13:15:00Z| 10.0.0.5    | login_failure |
| 2025-06-01T14:00:00Z| 192.168.1.1 | login_success |



<details>
<summary>Click to view raw CSV</summary>

```
timestamp,source_ip,event_type
2025-06-01T12:00:00Z,192.168.1.1,login_success
2025-06-01T12:05:00Z,10.0.0.5,login_failure
2025-06-01T13:15:00Z,10.0.0.5,login_failure
2025-06-01T14:00:00Z,192.168.1.1,login_success
```
</details>

## Screenshots

![Sentinel Copilot Dashboard](screenshot.png) <!-- Replace with your actual screenshot filename -->

---

## What’s Next?

- Plug in OpenAI for true LLM-based summaries
- Support for more log formats (JSON, syslog, etc.)
- User authentication for team use

---

## Connect & Contact

Want to chat, collaborate, or just see what else I’m working on?

[LinkedIn](https://www.linkedin.com/in/tesherakimbrough) | [GitHub](https://github.com/tesherakimbrough)

## Built With

- [Python](https://python.org)
- [Pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/)

---