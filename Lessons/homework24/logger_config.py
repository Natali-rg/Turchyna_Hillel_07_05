import logging


logger = logging.getLogger("cars_api")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# лог у файл
file_handler = logging.FileHandler("test_search.log", mode="a") #mode="a" - дописує логи, #mode="w" - перезаписує логи
file_handler.setFormatter(formatter)

# лог у консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)