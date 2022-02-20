from datetime import datetime
from typing import List

from pydantic import BaseModel

from customers.enums import Genders, Types, Regions, Nationalities


class Name(BaseModel):

    title: str

    first: str

    last: str


class Coordinates(BaseModel):

    latitude: str

    longitude: str


class Timezone(BaseModel):

    offset: str

    description: str


class Location(BaseModel):

    region: Regions

    street: str

    city: str

    state: str

    postcode: str

    coordinates: Coordinates

    timezone: Timezone


class Picture(BaseModel):

    large: str

    medium: str

    thumbnail: str


class Customer(BaseModel):

    type: Types

    gender: Genders

    name: Name

    location: Location

    email: str

    birthday: datetime

    registered: datetime

    telephone_numbers: List[str]

    mobile_numbers: List[str]

    picture: Picture

    nationality: Nationalities = Nationalities.BRAZILIAN
