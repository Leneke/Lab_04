import logging.handlers
import pathlib
from pathlib import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Setting up logging to the main folder in the current directory
new_path_folder = Path(pathlib.Path.cwd(), "folder_log")
new_path_folder.mkdir(parents=True, exist_ok=True)
new_path_file = Path(new_path_folder, "logcode.log")
new_path_file.touch(exist_ok=True)
logger_handler = logging.handlers.RotatingFileHandler(new_path_file, maxBytes=5000, backupCount=2)
logger.addHandler(logger_handler)
logger_handler.setFormatter(logger_formatter)

# Setting up logging to a backup folder in home directory
new_path_folder_copy = Path(pathlib.Path.home(), "folder_log_copy")
new_path_folder_copy.mkdir(parents=True, exist_ok=True)
new_path_file_copy = Path(new_path_folder_copy, "logcode_copy.log")
new_path_file_copy.touch(exist_ok=True)
logger_handler = logging.handlers.RotatingFileHandler(new_path_file_copy, maxBytes=5000, backupCount=2)
logger.addHandler(logger_handler)
logger_handler.setFormatter(logger_formatter)
