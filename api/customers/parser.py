from typing import List

from customers.helpers import phone_to_E164
from customers.enums import Genders, Types, Regions
from customers.models import Customer


class CustomerParser():

    def __init__(self, data: List = None):
        self.rows: List = data
        self.customers: List[Customer] = []
        self.parse()

    def parse(self):
        for row in self.rows:
            self.parse_phones(row)
            self.get_customer_type(row)
            self.get_customer_region(row)
            self.parse_gender(row)
            self.parse_birthday(row)
            self.parse_registered(row)
            self.customers.append(Customer(**row))

    def parse_phones(self, row):
        phone = row.pop('phone')
        cell = row.pop('cell')
        row['telephone_numbers'] = [phone_to_E164(phone)]
        row['mobile_numbers'] = [phone_to_E164(cell)]

    def get_customer_type(self, row):
        row['type'] = Types.LABORIOUS

    def get_customer_region(self, row):
        location = row.get('location')
        if not location:
            return None
        location['region'] = Regions.MIDWEST

    def parse_gender(self, row):
        gender = row.get('gender')
        genders = dict(
            male=Genders.MALE,
            female=Genders.FEMALE
        )
        row['gender'] = genders[gender]

    def parse_birthday(self, row):
        birthday = row.pop('dob')
        row['birthday'] = birthday.get('date')

    def parse_registered(self, row):
        registered = row.pop('registered')
        row['registered'] = registered.get('date')
