import logging
import os

def setup_logger():
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logger = logging.getLogger()
    logger.setLevel(log_level)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

logger = setup_logger()

