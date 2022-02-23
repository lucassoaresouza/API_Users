from requests.exceptions import MissingSchema, ConnectionError
from unittest.mock import MagicMock, patch

from api.customers.external_api import CustomersDownloader


def test_customer_downloader_initialize():
    csv = 'http.teste.com/csv'
    json = 'http.teste.com/json'
    downloader = CustomersDownloader(json_url=json, csv_url=csv)
    assert downloader.json_url == json
    assert downloader.csv_url == csv
    assert downloader.csv_data == []
    assert downloader.json_data == []


@patch('api.customers.external_api.CustomersDownloader.download_csv')
@patch('api.customers.external_api.CustomersDownloader.download_json')
def test_download_method(download_json_mock, download_csv_mock):
    CustomersDownloader().download()
    download_json_mock.assert_called()
    download_csv_mock.assert_called()


@patch('api.customers.external_api.request')
def test_download_json_method_connection_error(requests_mock):
    requests_mock.side_effect = MissingSchema
    downloader = CustomersDownloader()
    downloader.download_json()
    assert downloader.json_data == []


@patch('api.customers.external_api.request')
def test_download_json_method_success(requests_mock):
    response_mock = MagicMock()
    response_mock.json.return_value = {"results": {"teste": "etset"}}
    requests_mock.return_value = response_mock
    downloader = CustomersDownloader()
    downloader.download_json()
    assert downloader.json_data == {"teste": "etset"}


@patch('api.customers.external_api.request')
def test_download_csv_method_connection_error(requests_mock):
    requests_mock.side_effect = ConnectionError
    downloader = CustomersDownloader()
    downloader.download_csv()
    assert downloader.csv_data == []


@patch('api.customers.external_api.request')
def test_download_csv_method_success(requests_mock):
    response_mock = MagicMock()
    response_mock.content = b"T,N,E,T,N,O,C\nC,O,N,T,E,N,T\n"
    requests_mock.return_value = response_mock
    downloader = CustomersDownloader()
    downloader.download_csv()
    assert downloader.csv_data == [['C', 'O', 'N', 'T', 'E', 'N', 'T']]
