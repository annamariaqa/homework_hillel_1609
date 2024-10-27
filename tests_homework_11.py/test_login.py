
import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

def log_event(username: str, status: str):

    log_message = f"Login event - Username: {username}, Status: {status}"

    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    
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

#перевірка файлу на наявність username & status з очікуваним типом даних 
with open("login_system.log", "r", encoding="utf-8") as file:
    text = file.read()
    def check_logger_file(username, status):
        if  username == str in text:
            return username
        if status == str in text:
            return str 
        