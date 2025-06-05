import pandas as pd

def test_load_sample_csv():
    df = pd.read_csv("sample_logs/example_log.csv")
    assert not df.empty
    assert "timestamp" in df.columns
    assert "source_ip" in df.columns
    assert "event_type" in df.columns
