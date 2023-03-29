# Task №1. Create class and do logging
import pathlib
from abc import ABC, abstractmethod
import logging.handlers
from pathlib import *


class AbstractCustomsHouse(ABC):
    """Abstract Class"""

    @abstractmethod
    def register_list_add(self, name_value, date_value):
        pass

    @abstractmethod
    def display_register_list(self):
        pass

    @abstractmethod
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


class CustomsAir(AbstractCustomsHouse):
    """Class air customs"""
    logging.info(f'Class CustomsAir instance created')

    def __init__(self):
        self.registration_list = []

    def register_list_add(self, name_value: str, date_value: int):
        """The method adds information about those who crossed the border
        Options:
                name_value: str - name of the person who crossed the border
                date_value: int - date of border crossing
        Return value:
                    None"""
        logging.info(f'Added data on crossing the air border. Name-{name_value}, date-{date_value}')
        reg_list = {'Name': name_value, 'Date': date_value}
        self.registration_list.append(reg_list)

    def display_register_list(self):
        """The method prints information about those who crossed the border"""
        logging.info(f'Viewed list of those who crossed the air border')
        print('List of people who crossed the air border')
        for i in self.registration_list:
            print(i)

    def see_date(self, border_crossing_date: int):
        """The method prints information about those who crossed the border on a specific date
        Options:
                border_crossing_date: int - date of border crossing
        Return value:
                str - number of border crossings on a given date"""
        logging.info(f'Called up a list of those who crossed the air border on the {border_crossing_date}')
        count_number_of_crossings = 0
        for i in self.registration_list:
            if i['Date'] == border_crossing_date:
                count_number_of_crossings += 1
        return f'Air border crossing date: {border_crossing_date} \n' \
               f'Number of border crossings: {count_number_of_crossings}'


class CustomsLand(AbstractCustomsHouse):
    """Class land customs"""
    logging.info(f'Class CustomsLand instance created')

    def __init__(self):
        self.registration_list = []

    def register_list_add(self, name_value: str, date_value: int):
        """The method adds information about those who crossed the land border
        Options:
                name_value: str - name of the person who crossed the border
                date_value: int - date of border crossing
        Return value:
                    None"""
        logging.info(f'Land border crossing data added. Name-{name_value}, date-{date_value}')
        reg_list = {'Name': name_value, 'Date': date_value}
        self.registration_list.append(reg_list)

    def display_register_list(self):
        """The method prints information about those who crossed the land border"""
        logging.info(f'Called up a list of those who crossed the land border')
        print('List of people who crossed the land border')
        for i in self.registration_list:
            print(i)

    def see_date(self, border_crossing_date: int):
        """The method prints information about those who crossed the land border on a specific date
        Options:
                border_crossing_date: int - date of border crossing
        Return value:
                str - number of land border crossings on a given date"""
        logging.info(f'Called up a list of those who crossed the land border on the {border_crossing_date}')
        count_of_border_crossing_date = 0
        for i in self.registration_list:
            if i['Date'] == border_crossing_date:
                count_of_border_crossing_date += 1
        return f'Land border crossing date: {border_crossing_date} \n' \
               f'Number of border crossings: {count_of_border_crossing_date}'


def example_land():
    # An example of creating an instance of a class CustomsLand and using class methods
    horgos = CustomsLand()
    horgos.register_list_add('Misha', 15)
    horgos.register_list_add('Masha', 5)
    horgos.register_list_add('Natasha', 15)
    horgos.register_list_add('Sasha', 15)
    horgos.register_list_add('Dasha', 15)
    print(horgos.display_register_list())
    print()
    print(horgos.see_date(15))
    print()
    print(horgos.see_date(5))


def example_air():
    # An example of creating an instance of a class CustomsAir and using class methods
    almaty = CustomsAir()
    almaty.register_list_add('Nastya', 11)
    almaty.register_list_add('Kristina', 25)
    almaty.register_list_add('Diana', 25)
    print(almaty.display_register_list())
    print()
    print(almaty.see_date(11))
    print()
    print(almaty.see_date(25))


example_land()
example_air()
