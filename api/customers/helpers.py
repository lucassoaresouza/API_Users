from decimal import Decimal
import re
from typing import Tuple


def phone_to_E164(phone: str, country_code: int = 55):
    """
    Makes the parse of a phone number to E164 patthern.
    :param phone: String with the phone number to be parsed.
    :param country_code: Code defines the phone country.
    :returns: A string with the parsed number.
    """
    groups = re.findall(r'\d', phone)
    number = ''.join(group for group in groups)
    e164_number = f'+{country_code}{number}'
    return e164_number


def is_in_rectangle(
    bottom_left: Tuple[Decimal],
    top_right: Tuple[Decimal],
    point: Tuple[Decimal]
) -> bool:
    """
    Checks if a point is inside of a rectangle.
    :param bottom_left: (maxlon, minlat) point.
    :param top_right: (minlon, maxlat) point.
    :param point: (longitude, latitude) point to be checked.
    :returns: True if the point is in rectangle otherwise False.
    """
    if (
        point[0] > bottom_left[0] and point[0] < top_right[0] and
        point[1] > bottom_left[1] and point[1] < top_right[1]
    ):
        return True
    return False
