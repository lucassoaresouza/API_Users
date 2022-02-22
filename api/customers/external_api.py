import csv
from os import getenv
from typing import List

from requests import request


class CustomersDownload():
    """
    Class that make the download of Customer data sets.
    """

    def __init__(self):
        """
        Class constructor.
        """
        self.json_url: str = getenv('CUSTOMERS_JSON_URL')
        self.csv_url: str = getenv('CUSTOMERS_CSV_URL')
        self.csv_data: List = []
        self.json_data: List = []

    def download(self) -> None:
        """
        Download the Customer data sets.
        """
        self.download_json()
        self.download_csv()

    def download_json(self) -> None:
        """
        Download the customer data set from a JSON url.
        """
        response = request('GET', self.json_url)
        data = response.json()
        self.json_data = data.get('results')

    def download_csv(self) -> None:
        """
        Download the customer data set from a CSV url.
        """
        response = request('GET', self.csv_url)
        content = response.content.decode('utf-8')
        reader = csv.reader(content.splitlines(), delimiter=',')
        data = list(reader)
        self.csv_data = data[1:]
