import logging
from pathlib import Path
from pathlib import PurePath , PurePosixPath
from dotenv import load_dotenv
import os

def logging_method(__name__):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(name)s:%(lineno)d:%(asctime)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('images_generator.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

# Loading API KEY from external file
load_dotenv()
API_KEY = os.getenv("API_KEY")