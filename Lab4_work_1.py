# Task №1. Create class and do logging
import pathlib
from abc import ABC
import logging.handlers
from pathlib import *


class CustomsHouse(ABC):
    """Abstract Class"""

    def register_list_add(self, name_value, date_value, type_value):
        pass

    def display_register_list(self):
        pass

    def see_date(self, border_crossing_date):
        pass


# Setting up logging to the main and backup folders
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

new_path_folder_copy = Path(pathlib.Path.home(), "folder_log_copy")
new_path_folder_copy.mkdir(parents=True, exist_ok=True)
new_path_file_copy = Path(new_path_folder_copy, "logcode_copy.log")
new_path_file_copy.touch(exist_ok=True)
logger_handler = logging.handlers.RotatingFileHandler(new_path_file_copy, maxBytes=5000, backupCount=2)
logger.addHandler(logger_handler)
logger_handler.setFormatter(logger_formatter)

new_path_folder = Path(pathlib.Path.cwd(), "folder_log")
new_path_folder.mkdir(parents=True, exist_ok=True)
new_path_file = Path(new_path_folder, "logcode.log")
new_path_file.touch(exist_ok=True)
logger_handler = logging.handlers.RotatingFileHandler(new_path_file, maxBytes=5000, backupCount=2)
logger.addHandler(logger_handler)
logger_handler.setFormatter(logger_formatter)


class Customs(CustomsHouse):
    """Class customs"""

    logging.info(f'Class instance created')

    def __init__(self):
        self.registration_list = []

    def register_list_add(self, name_value: str, date_value: int, type_value: str):
        """The method adds information about those who crossed the border
        Options:
                name_value: str - name of the person who crossed the border
                date_value: int - date of border crossing
                type_value: str - type of border crossed, land or air
        Return value:
                    None"""
        logging.info(f'Border crossing data added. Name-{name_value}, date-{date_value}, customs-{type_value}')
        reg_list = {'Name': name_value, 'Date': date_value, 'Type_customs': type_value}
        self.registration_list.append(reg_list)

    def display_register_list(self):
        """The method prints information about those who crossed the border"""
        logging.info(f'Called up a list of those who crossed the border')
        print('List of people who crossed the border')
        for i in self.registration_list:
            print(i)

    def see_date(self, border_crossing_date: int):
        """The method prints information about those who crossed the border on a specific date
        Options:
                border_crossing_date: int - date of border crossing
        Return value:
                str - number of land, air and total number of border crossings on a given date"""
        logging.info(f'Called up a list of those who crossed the border on the {border_crossing_date}')
        number_of_crossings_air = 0
        number_of_crossings_land = 0
        total_number_of_crossings = 0
        for i in self.registration_list:
            if i['Date'] == border_crossing_date:
                total_number_of_crossings += 1
                if i['Type_customs'] == 'air':
                    number_of_crossings_air += 1
                if i['Type_customs'] == 'land':
                    number_of_crossings_land += 1
        return f'Border crossing date: {border_crossing_date} \n' \
               f'Number of air border crossings: {number_of_crossings_air} \n' \
               f'Number of land border crossings: {number_of_crossings_land} \n' \
               f'Total number of border crossings: {total_number_of_crossings}'


def example():
    # An example of creating an instance of a class and using class methods
    a = Customs()
    a.register_list_add('Misha', 15, 'air')
    a.register_list_add('Masha', 5, 'land')
    a.register_list_add('Natasha', 15, 'land')
    a.register_list_add('Sasha', 15, 'air')
    a.register_list_add('Dasha', 15, 'land')
    print(a.display_register_list())
    print()
    print(a.see_date(15))
    print()
    print(a.see_date(5))


example()
