import logging
from datetime import datetime

logging.basicConfig(
    filename="hb_test.log",
    filemode="w",
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
'''logging.basicConfig(
    filename="hb_test.log",
    level=logging.WARNING,
    format="%(levelname)s - %(message)s"
)'''

logger = logging.getLogger(__name__)

KEY = "Key TSTFEED0300|7E3E|0400"

def get_filtered_log(filename):
    filtered_log = []

    with open(filename, "r") as file:
        for line in file:
            if KEY in line:
                filtered_log.append(line.strip())
    return filtered_log

def analyze_heartbeat(filename):
    filtered_log = get_filtered_log(filename)

    previous_time = None

    for line in filtered_log:
        start = line.find("Timestamp ") + len("Timestamp ")
        time_str = line[start:start + 8]

        current_time = datetime.strptime(time_str, "%H:%M:%S")

        if previous_time is not None:

            diff = (previous_time - current_time).total_seconds()

            if 31 < diff < 33:
                logger.warning(
                    f"Heartbeat {diff:.0f} sec at {time_str}"
                )

            elif diff >= 33:
                logger.error(
                    f"Heartbeat {diff:.0f} sec at {time_str}"
                )

        previous_time = current_time


if __name__ == "__main__":
    analyze_heartbeat("hblog.txt")
