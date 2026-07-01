import xml.etree.ElementTree as ET
import logging

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_incoming_by_group_number(xml_path: str, group_number: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number')

        if number is not None and number.text == str(group_number):
            timing = group.find('timingExbytes')

            if timing is not None:
                incoming = timing.find('incoming')

                if incoming is not None:
                    logger.info(
                        f"Group {group_number} -> incoming value: {incoming.text}"
                    )
                    return incoming.text

    logger.info(f"Group {group_number} not found or no incoming value")
    return None


# приклад виклику
get_incoming_by_group_number("groups.xml", "2")