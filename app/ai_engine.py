# AI engine for natural language summary
import pandas as pd

def analyze_logs(log_df):
    # This is just a mocked-up summary
    data = [
        {"Event": "login_failure", "Severity": "High", "Explanation": "Multiple failed logins detected from 10.0.0.5."},
        {"Event": "login_success", "Severity": "Low", "Explanation": "Normal successful login from 192.168.1.1."}
    ]
    return pd.DataFrame(data)
