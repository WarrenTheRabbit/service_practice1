"""
Defines a logger to be used by the application.
"""

import logging
import sys

logger = logging.getLogger("service1")

formatter = logging.Formatter(

    fmt="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"


stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("app1.log")

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]

logger.setLevel(logging.INFO)
