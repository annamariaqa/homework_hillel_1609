import pytest
import logging
import logging.config

logging.config.fileConfig('logging_config.ini')

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

def log_event(username: str, status: str):
    pass
    
@pytest.mark.parametrize('username, status', [('Denn', 'success'), ('Alex', 'expired'), ('Ivan', 'unknown')])
def test_logging(username, status):
    log_event(username, status)
    
    logger = logging.getLogger("log_event")
    if logger.hasHandlers():
        logger.handlers.clear()

    log_message = f"Login event - Username: {username}, Status: {status}"
    
    logger = logging.getLogger("log_event")
    file_handler = logging.FileHandler('login_system.log')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

    

    with open('login_system.log', 'r') as file_:
        content = file_.read()
        rows = content.split('\n')
        last_row = rows[-2]
        expected_row = log_message
        assert expected_row in last_row