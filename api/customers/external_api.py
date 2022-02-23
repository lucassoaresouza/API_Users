import csv
from os import getenv
from typing import List

from requests import request
from requests.exceptions import MissingSchema, ConnectionError, HTTPError


class CustomersDownloader():
    """
    Class that make the download of Customer data sets.
    """

    def __init__(self, json_url: str = None, csv_url: str = None):
        """
        Class constructor.
        :param json_url: Url of the JSON data.
        :param csv_url: Url of the CSV data.
        """
        self.json_url: str = json_url or getenv('CUSTOMERS_JSON_URL')
        self.csv_url: str = csv_url or getenv('CUSTOMERS_CSV_URL')
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
        try:
            response = request('GET', self.json_url)
        except (MissingSchema, ConnectionError):
            print("Failed to connect to url.")
            return
        try:
            response.raise_for_status()
        except HTTPError:
            print("Fail to get the csv data.")
            return
        data = response.json()
        self.json_data = data.get('results')

    def download_csv(self) -> None:
        """
        Download the customer data set from a CSV url.
        """
        try:
            response = request('GET', self.csv_url)
        except (MissingSchema, ConnectionError):
            print("Failed to connect to url.")
            return

        try:
            response.raise_for_status()
        except HTTPError:
            print("Fail to get the csv data.")
            return
        content = response.content.decode('utf-8')
        reader = csv.reader(content.splitlines(), delimiter=',')
        data = list(reader)
        self.csv_data = data[1:]
