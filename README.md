![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-3776AB?logo=matplotlib)
![MIT License](https://img.shields.io/badge/License-MIT-green)

# Sentinel Copilot

**Live demo:** [sentinel-copilot.streamlit.app](https://sentinel-copilot.streamlit.app)  
**GitHub repo:** [github.com/tesherakimbrough/sentinel-copilot](https://github.com/tesherakimbrough/sentinel-copilot)

---

## Why I Built This

Security logs can be overwhelming and time-consuming to analyze, especially when you’re under pressure. I built Sentinel Copilot to make log analysis more approachable—something that feels modern and actually helps you get real answers fast.  
I wanted a tool that would let me upload a log file, explore it, filter and search, get visual feedback, and see an incident summary—all in one place.  
This project is what I wish I’d had when I was learning security operations and wanted to move faster and learn more from my data.

---

## Features

- 🗃️ **Drag-and-drop CSV log upload** (or use a sample instantly)
- 📉 **Summary metrics:** total events, unique IPs, event types
- 🚦 **Top offenders:** highlights most frequent event and noisiest source IP
- 🔍 **Powerful filters:** search, multi-select for events/IPs, date range slider
- 📊 **Charts:** event frequency, top source IPs, (line graph for multi-day logs)
- 🤖 **AI-generated incident summaries** (mocked or live API ready)
- 💾 **Export:** download filtered logs or a full incident report
- 🌙/☀️ **Dark/light mode toggle**

---

## Quick Start

1. **Upload** a CSV log file (or click “Load Sample Data”)
2. **Explore** summary stats and data preview
3. **Filter** by keyword, event type, source IP, or date
4. **Visualize** the patterns in your logs
5. **Read** an instant AI summary
6. **Export** filtered data or an incident report

---

## Screenshot

![Sentinel Copilot Dashboard](screenshot.png)

---

## Architecture Overview

```
User Uploads Log File
|
▼
Log Parser (Python/pandas)
|
▼
AI Summary (mock/table, ready for OpenAI integration)
├─► Visualizations (matplotlib/Streamlit)
└─► Downloadable Report
```


*Each step is modular and easy to extend with your own logic, APIs, or AI models.*

---

## Built With

- [Python](https://python.org)
- [Pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/)

---

## Want to Connect?

I built Sentinel Copilot to make security analysis more direct and useful for people like me who want to get better at security engineering and data analysis.  
If you want to talk security, collaboration, or career opportunities,  
**connect with me on [LinkedIn](https://www.linkedin.com/in/tesherakimbrough/)**

---

[GitHub Repo](https://github.com/tesherakimbrough/sentinel-copilot)
