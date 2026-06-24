import logging
import logging.config


logging.config.fileConfig('logging_conf.ini')

logger = logging.getLogger('log_event')


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    success -> INFO
    expired -> WARNING
    failed -> ERROR
    """

    log_message = f"Login event - Username: {username}, Status: {status}"

    if status == "success":

        logger.info(log_message)

    elif status == "expired":

        logger.warning(log_message)

    else:

        logger.error(log_message)