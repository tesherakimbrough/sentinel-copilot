import pandas as pd
from app.log_parser import parse_logs

def test_parse_logs_handles_csv():
    df = pd.DataFrame({"event_type": ["login_success", "login_failure"]})
    parsed = parse_logs(df)
    assert not parsed.empty
