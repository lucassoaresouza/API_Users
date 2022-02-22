from typing import Dict, List

from customers.models import Customer
from customers.external_api import CustomersDownload
from customers.parser import CustomersFromJson, CustomersFromCSV


def filter_customers(customers: List[Customer], country: str = 'BR') -> None:
    """
    Filters a customer by country, region and classifications.
    :param customer: A Customer model instance
    :param country: String with the code of customer's country.
    """
    filtered = {}
    for customer in customers:
        region = customer.location.region.value
        if not filtered.get(country):
            filtered[country] = {}

        if not filtered[country].get(region):
            filtered[country][region] = {}

        if not filtered[country][region].get(customer.type):
            filtered[country][region][customer.type] = []

        filtered[country][region][customer.type].append(customer)

    return filtered


def initialize() -> Dict:
    """
    Initializes the Customer data.
    Makes the steps:
        download -> parser -> filter
    :returns: Filtered Customers instances.
    """
    downloader = CustomersDownload()
    downloader.download()
    csv_customers = CustomersFromCSV(downloader.csv_data).customers
    json_customers = CustomersFromJson(downloader.json_data).customers
    all_customers = csv_customers + json_customers
    return filter_customers(all_customers)
