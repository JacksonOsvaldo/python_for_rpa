import logging


class LoggingManager:
    def __init__(self, name_process: str) -> None:
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(f"{name_process}.log")
        stream_handler = logging.StreamHandler()

        stream_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s %(message)s"
        )
        file_formatter = logging.Formatter(
            """{"time":"%(asctime)s","name":"%(name)s","level":"%(levelname)s","path_name":"%(pathname)s","func_name":"%(funcName)s","line_code":"%(lineno)d","message":"%(message)s"}"""
        )

        file_handler.setFormatter(file_formatter)
        stream_handler.setFormatter(stream_formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def info(self, name: str, mensage: str):
        self.logger.name = name
        self.logger.info(mensage, stacklevel=2)

    def warning(self, name: str, mensage: str):
        self.logger.warning(mensage, stacklevel=2)

    def error(self, name: str, mensage: str):
        self.logger.name = name
        self.logger.error(mensage, stacklevel=2)

    def critical(self, name: str, mensage: str):
        self.logger.name = name
        self.logger.critical(mensage, stacklevel=2)
