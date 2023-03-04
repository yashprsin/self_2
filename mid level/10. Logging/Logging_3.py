import logging

logger = logging.getLogger(__name__)

# Create handler
steam_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format
steam_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
steam_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(steam_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is a error')