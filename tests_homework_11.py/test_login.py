import pytest
import logging
import logging.config

logging.config.fileConfig('logging_config.ini')

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

def log_event(username: str, status: str):

    log_message = f"Login event - Username: {username}, Status: {status}"

    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
        )

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

    
@pytest.mark.parametrize('username, status', [('Denn', 'success'), ('Alex', 'expired'), ('Ivan', 'unknown')])
def test_logging(username, status):
    log_event(username, status)
    
    logger = logging.getLogger("log_event")
    if logger.hasHandlers():
        logger.handlers.clear()

    with open('login_system.log', 'r') as file_:
        content = file_.read()
        rows = content.split('\n')
        last_row = rows[-2]
    expected_row = f"Login event - Username: {username}, Status: {status}"
    assert expected_row in last_row