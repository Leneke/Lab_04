import logging.handlers
import pathlib
from pathlib import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


def path_create_logfile(path_folder, path_file):
    """Function to create a path to save the log file. It takes two parameters as input:
    1. Folder creation path and 2. File creation path."""
    path_folder.mkdir(parents=True, exist_ok=True)
    path_file.touch(exist_ok=True)
    logger_handler = logging.handlers.RotatingFileHandler(path_file, maxBytes=5000, backupCount=2)
    logger.addHandler(logger_handler)
    logger_handler.setFormatter(logger_formatter)


# Path to the main folder in the current directory
new_path_folder = Path(pathlib.Path.cwd(), "folder_log")
new_path_file = Path(new_path_folder, "logcode.log")

# Path to back up folder in home directory
new_path_folder_copy = Path(pathlib.Path.home(), "folder_log_copy")
new_path_file_copy = Path(new_path_folder_copy, "logcode_copy.log")

path_create_logfile(new_path_folder, new_path_file)
path_create_logfile(new_path_folder_copy, new_path_file_copy)
