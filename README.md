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

I work in security analysis and I’m teaching myself software engineering. After spending too many hours buried in log files, I wanted a tool that’s quick, visual, and actually useful—no advanced degree needed. Sentinel Copilot is my solution: upload a file, get results, and get on with your day. With built-in anomaly detection powered by real machine learning, Sentinel Copilot helps you catch the log entries that matter most—even those traditional dashboards miss.


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
    >If you want to use machine learning features, scikit-learn is required and already included in requirements.txt

3. **Run the app**
    ```bash
    streamlit run app/main.py
    ```

Or try it instantly on the [live Streamlit demo](https://sentinel-copilot.streamlit.app/).

---

## What Makes Sentinel Copilot Different?

If you’re tired of one-size-fits-all tools, Sentinel Copilot is built for fast, real-world insights:

- **Dark/Light Mode Toggle:** Pick your favorite theme for comfort.
- **Interactive Filtering:** Search, sort, and filter logs by IP, event type, date, or keywords.
- **Visual Summaries:** Instant charts for event frequency, source IP activity, and more.
- 🧠 **Real-time anomaly detection:** Machine learning (Isolation Forest) flags suspicious log events automatically—no keys or cloud required.
- **Downloadable Reports:** Export summaries or filtered logs as CSV with one click.
- **No AI Hype—Just Useful Automation:** Mock “AI summary” is built in, and it’s ready for plug-and-play with OpenAI if you want to add GPT-based analysis later.
- **Open Source & Easy to Extend:** Clean codebase and modular structure. Fork away.




---

## Features at a Glance

- Upload log files (CSV)
- See top events and “noisiest” IPs right away
- Explore interactive charts and tables
- 🧠 Built-in machine learning anomaly detection (Isolation Forest) to surface suspicious events—no setup required
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
## 🧠 AI & Anomaly Detection

Sentinel Copilot uses Isolation Forest (scikit-learn) to automatically flag rare or suspicious log events—helping security teams focus on what matters most. It’s fully local, open source, and ready for production use or extension.

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

## Requirements

- Python 3.10+
- Works on Windows, macOS, or Linux

---

## Troubleshooting

- **Streamlit not found:**  
  Make sure you installed all requirements:  
  `pip install -r requirements.txt`

- **Port already in use:**  
  If you get an error about a port conflict, stop other Streamlit apps or change the port with:  
  `streamlit run app/main.py --server.port 8502`

- **Issues with plots or CSV files:**  
  Double-check your CSV format matches the sample. Supported columns: `timestamp`, `source_ip`, `event_type`.

---

## Credits & Inspiration

Inspired by open-source tools like Graylog, Splunk, and awesome projects from the Streamlit and InfoSec communities.

---

## Contributing

Pull requests, feedback, and suggestions are always welcome!

---

## Connect & Contact

Want to chat, collaborate, or just see what else I’m working on?

[LinkedIn](https://www.linkedin.com/in/tesherakimbrough) | [GitHub](https://github.com/tesherakimbrough)

## Built With

- [Python](https://python.org)
- [Pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/) (for machine learning anomaly detection)

---