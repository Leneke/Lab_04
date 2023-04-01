# Task №1. Create a class and set up logging in two different folders
from datetime import datetime
from abc import ABC, abstractmethod
import logging.handlers
import my_logger

logger = logging.getLogger('my_logger')


class AbstractCustomsHouse(ABC):
    """Abstract Class"""

    @abstractmethod
    def register_list_add(self, name_value):
        pass

    @abstractmethod
    def display_register_list(self):
        pass

    @abstractmethod
    def see_date(self, border_crossing_date):
        pass


class CustomsAir(AbstractCustomsHouse):
    """Class air customs"""
    logging.info(f'Class CustomsAir instance created')

    def __init__(self):
        self.registration_list = []

    def register_list_add(self, name_value: str):
        """The method adds information about those who crossed the border
        Options:
                name_value: str - name of the person who crossed the border
                The current date is added automatically
        Return value:
                    None"""
        date_value = datetime.today().strftime("%d.%m.%Y")
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

    def register_list_add(self, name_value: str):
        """The method adds information about those who crossed the land border
        Options:
                name_value: str - name of the person who crossed the border
                The current date is added automatically
        Return value:
                    None"""
        date_value = datetime.today().strftime("%d.%m.%Y")
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
    horgos.register_list_add('Misha')
    horgos.register_list_add('Masha')
    horgos.register_list_add('Natasha')
    horgos.register_list_add('Sasha')
    horgos.register_list_add('Dasha')
    print(horgos.display_register_list())
    print()
    print(horgos.see_date('01.04.2023'))
    print()


def example_air():
    # An example of creating an instance of a class CustomsAir and using class methods
    almaty = CustomsAir()
    almaty.register_list_add('Nastya')
    almaty.register_list_add('Kristina')
    almaty.register_list_add('Diana')
    print(almaty.display_register_list())
    print()
    print(almaty.see_date('02.04.2023'))


if __name__ == '__main__':
    example_land()
    example_air()
