import logging
from datetime import datetime
import os


LOG_DIR = "housinglogs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# Set up basic logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
    level=logging.DEBUG
)

