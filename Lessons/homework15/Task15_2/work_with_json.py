import os
import json
import logging

logging.basicConfig(
    filename="json_Turchyna.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_folder = os.path.join(BASE_DIR, "work_with_json")

print(json_folder)
print(os.path.exists(json_folder))

for file_name in os.listdir(json_folder):

    if file_name.endswith('.json'):

        file_path = os.path.join(json_folder, file_name)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json.load(file)

        except json.JSONDecodeError as error:
            logging.error(
                f'File "{file_name}" is invalid JSON. Error: {error}'
            )

print('Validation completed')