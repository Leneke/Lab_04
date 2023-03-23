import pathlib
from abc import ABC
import logging
from pathlib import *

new_path = Path(pathlib.Path.home(), "folder_log")
new_path.mkdir(parents=True, exist_ok=True)
file_log = logging.FileHandler(Path(new_path, "logcode.log"))

new_path_copy = Path(pathlib.Path.cwd(), "folder_log_copy")
new_path_copy.mkdir(parents=True, exist_ok=True)
file_log_copy = logging.FileHandler(Path(new_path_copy, "logcode_copy.log"))

logging.basicConfig(handlers=(file_log, file_log_copy), level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


class CustomsHouse(ABC):
    def register_list_add(self, name_value, date_value, type_value):
        pass

    def display_register_list(self):
        pass

    def see_date(self, border_crossing_date):
        pass


class Customs(CustomsHouse):
    logging.info(f'Class instance created')

    def __init__(self):
        self.registration_list = []

    def register_list_add(self, name_value, date_value, type_value):
        logging.info(f'Border crossing data added. Name-{name_value}, date-{date_value}, customs-{type_value}')
        reg_list = {'Name': name_value, 'Date': date_value, 'Type_customs': type_value}
        self.registration_list.append(reg_list)
        return self.registration_list

    def display_register_list(self):
        logging.info(f'Called up a list of those who crossed the border')
        print('List of people who crossed the border')
        for i in self.registration_list:
            print(i)
        return ''

    def see_date(self, border_crossing_date):
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


a = Customs()
a.register_list_add('Misha', 15, 'air')
a.register_list_add('Sasha', 15, 'air')
a.register_list_add('Dasha', 15, 'land')
print(a.display_register_list())
print(a.see_date(15))
