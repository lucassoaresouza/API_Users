from abc import abstractmethod
from decimal import Decimal
from typing import List, Dict, Union

from customers.helpers import phone_to_E164, is_in_rectangle, string_to_key
from customers.enums import Genders, Types, Regions
from customers.models import Customer
from customers.regions import COUNTRIES_REGIONS_MAPPING
from customers.types_boundaries import BOUNDARIES_MAPPING


class BaseCustomerParser():
    """
    Class to define a base flow to parse a Customers list
    from any list of data.
    """

    def __init__(self, data: List = None):
        """
        Class constructor.
        :param data: A Dict of classified customers data.
        """
        self.rows: List = data
        self.customers: List[Customer] = []
        self.parse()

    @abstractmethod
    def parse_row(self, row: Union[Dict, List] = None) -> Customer:
        """
        Abstract class, needs to be implemented.
        Makes the parse of a data set to a new Customer.
        :param row: The data set of a unique Customer.
        :returns: A Customer model instance.
        """
        pass

    def parse(self) -> None:
        """
        Makes the parse of received data to Customers instances.
        """
        for row in self.rows:
            customer = self.parse_row(row)
            self.customers.append(customer)

    def parse_gender(self, value: str) -> Genders:
        """
        Makes the parse of received gender to Gender instance.
        :param value: string with the literal gender.
        """
        genders = dict(
            male=Genders.MALE,
            female=Genders.FEMALE
        )
        return genders[value]

    def get_type(
        self, latitude: str, longitude: str, country: str = 'BR'
    ) -> Types:
        """
        Selects the customer type according the coordinates boundaries.
        :param latitude: String with the latitude.
        :param longitude: String with the longitude.
        :param country: String with the code of customer's country.
        :returns: A Type instance.
        """
        boudaries = BOUNDARIES_MAPPING[country]
        lon = Decimal(longitude)
        lat = Decimal(latitude)
        for boundary in boudaries.get('ESPECIAL', []):
            if is_in_rectangle(
                top_right=(boundary['minlon'], boundary['maxlat']),
                bottom_left=(boundary['maxlon'], boundary['minlat']),
                point=(lon, lat)
            ):
                return Types.ESPECIAL

        for boundary in boudaries.get('NORMAL', []):
            if is_in_rectangle(
                top_right=(boundary['minlon'], boundary['maxlat']),
                bottom_left=(boundary['maxlon'], boundary['minlat']),
                point=(lon, lat)
            ):
                return Types.NORMAL

        return Types.LABORIOUS

    def get_region(self, state, country: str = 'BR') -> Regions:
        """
        Selects the customer region according the state
        and country of their location.
        :param state: String with customer's state.
        :param country: String with the code of customer's country.
        :returns: A Regions instance.
        """
        state_key = string_to_key(state)
        return COUNTRIES_REGIONS_MAPPING[country][state_key]


class CustomersFromJson(BaseCustomerParser):

    def parse_row(self, row: Union[Dict, List] = None) -> Customer:
        """
        Parses the received json to a Customer instance.
        :param row: A Dict with the customer data set.
        :returns: A Customer instance.
        """
        row['gender'] = self.parse_gender(value=row.get('gender'))
        self.parse_phones(row=row)
        self.parse_birthday(row=row)
        self.parse_registered(row=row)
        row['location']['region'] = self.get_region(
            state=row['location']['state'])
        coordinates = row['location']['coordinates']
        row['type'] = self.get_type(
            latitude=coordinates['latitude'],
            longitude=coordinates['longitude'])
        return Customer(**row)

    def parse_phones(self, row) -> None:
        """
        Removes phone and cell fields from original dict
        and set the telephone_numbers and mobile_numbers lists.
        :param row: A Dict with the customer data set.
        """
        phone = row.pop('phone')
        cell = row.pop('cell')
        row['telephone_numbers'] = [phone_to_E164(phone=phone)]
        row['mobile_numbers'] = [phone_to_E164(phone=cell)]

    def parse_birthday(self, row) -> None:
        """
        Removes the fields 'age' from 'dob'.
        :param row: A Dict with the customer data set.
        """
        birthday = row.pop('dob')
        row['birthday'] = birthday.get('date')

    def parse_registered(self, row) -> None:
        """
        Removes the fields 'age' from 'registered'.
        :param row: A Dict with the customer data set.
        """
        registered = row.pop('registered')
        row['registered'] = registered.get('date')


class CustomersFromCSV(BaseCustomerParser):

    def parse_row(self, row: Union[Dict, List] = None) -> Customer:
        """
        Parses the received list data set to a Customer instance.
        :param row: A List with the customer data set.
        :returns: A Customer instance.
        """
        data = dict(
            gender=self.parse_gender(row[0]),  # gender
            name=dict(
                title=row[1],  # name__title
                first=row[2],  # name__first
                last=row[3]  # name__last
            ),
            location=dict(
                street=row[4],  # location__street
                city=row[5],  # location__city
                state=row[6],  # location__state
                postcode=row[7],  # location__postcode
                coordinates=dict(
                    latitude=row[8],  # location__coordinates__latitude
                    longitude=row[9]  # location__coordinates__longitude
                ),
                timezone=dict(
                    offset=row[10],  # location__timezone__offset
                    description=row[11]  # location__timezone__description
                )
            ),
            email=row[12],  # email
            birthday=row[13],  # dob__date
            registered=row[15],  # registered__date
            telephone_numbers=[phone_to_E164(row[17])],  # phone
            mobile_numbers=[phone_to_E164(row[18])],  # cell
            picture=dict(
                large=row[19],  # picture__large
                medium=row[20],  # picture__medium
                thumbnail=row[21]  # picture__thumbnail
            )
        )
        data['type'] = self.get_type(latitude=row[8], longitude=row[9])
        data['location']['region'] = self.get_region(state=row[6])
        return Customer(**data)
