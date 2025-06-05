# AI engine for natural language summary
def analyze_logs(log_df):
    # MOCK AI OUTPUT (no OpenAI API required)
    summary = """
| Event           | Severity | Explanation                                        |
|-----------------|----------|----------------------------------------------------|
| login_failure   | High     | Multiple failed logins detected from 10.0.0.5.     |
| login_success   | Low      | Normal successful login from 192.168.1.1.          |
"""
    return summary
