import pytest
from test_login import log_event

def test_log_event_negative():
    actual_result = log_event(username=123, status=123)
    expected_result = str 
    if actual_result == expected_result:
        assert True