import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# лог у файл
file_handler = logging.FileHandler(
    "selenium_test.log",
    mode="w",
    encoding="utf-8"
)
file_handler.setFormatter(formatter)

# лог у консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)