import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("foo.log")
stream_handler = logging.StreamHandler()

stream_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
file_formatter = logging.Formatter(
    "{'time':'%(asctime)s','name': '%(name)s','level': '%(levelname)s','message': '%(message)s'}"
)

file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info("teste")
