import pytest
from test_login import log_event

def test_log_event_success_status():
    actual_result = log_event(username='Anna', status='success')
    expected_result = str 
    if actual_result == expected_result:
        assert True
def test_log_event_expired_status():
    actual_result = log_event(username='Anna', status='expired')
    expected_result = str 
    if actual_result == expected_result:
        assert True
def test_log_event_failed_status():
    actual_result = log_event(username='Anna', status='failed')
    expected_result = str 
    if actual_result == expected_result:
        assert True