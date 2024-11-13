import json

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.getLogger('').addHandler(console_handler)

try:
    with open('login.json', 'r') as file_login:
        data_login_file = json.load(file_login)

    # print(type(data_login_file))
except json.decoder.JSONDecodeError as e:
    logging.error("Failed to decode JSON: %s", e)

try:
    with open('localizations_en.json', 'r') as file_localizations:
        data_file_localization = json.load(file_localizations)

    # print(type(data_file_localization))
except json.decoder.JSONDecodeError as e:
    logging.error("Failed to decode JSON: %s", e)
try:
    with open('swagger.json', 'r') as file_swagger:
        data_file_swagger = json.load(file_swagger)

    # print(type(data_file_swagger))
except json.decoder.JSONDecodeError as e:
    logging.error("Failed to decode JSON: %s", e)




