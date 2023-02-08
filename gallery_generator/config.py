from pathlib import Path
import logging


def logging_method(__name__):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(name)s:%(lineno)d:%(asctime)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('ImagesGenerator.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger