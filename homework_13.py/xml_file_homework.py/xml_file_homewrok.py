import logging
import xml.etree.ElementTree as ET
tree = ET.parse('groups.xml')
root_el = tree.getroot()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)


logger = logging.getLogger()
logger.addHandler(console_handler)

for sub_el in root_el:
    for child in sub_el:
        print(child.tag)

        if child.tag == 'timingExbytes':
            print(list(child)[-1].text)
            logger.info(f"INFO message: знайдено 'timingExbytes' елемент {list(child)[-1].text}")


            
