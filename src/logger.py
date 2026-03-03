import logging
import os
from datetime import datetime

## creating a log file
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

## join the log folder with current directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

## join cd path to newly created log file
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

##log configration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO
)