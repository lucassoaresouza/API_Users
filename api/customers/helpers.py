import re


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
