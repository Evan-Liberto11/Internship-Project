#!/usr/local/bin/python3
""" IA **REDACTED** application. """

# Imports - Python Standard Library
import csv
from typing import Dict
from typing import List
from os import getenv
import sys
import yaml

# Imports - Third-Party
from dotenv import load_dotenv
from requests import request, Response
import requests

# Imports - Local
from location_uids import RATE_CARD

# Load .env file
load_dotenv()

# Constant
API_SERVER = '**REDACTED**.com'
API_VERSION = '**REDACTED**'
BASE_URL = f'https://{API_SERVER}/api/{API_VERSION}'
AUTH_URL = f'{BASE_URL}/auth/signin'
SITE_URL = f'{BASE_URL}/sites'
BASE_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
HTTP_TIMEOUT = 3
PAT_NAME = getenv("PAT_NAME")
PAT_SECRET = getenv("PAT_SECRET")
AUTH_BODY = {
    "credentials": {
		"personalAccessTokenName": PAT_NAME,
		"personalAccessTokenSecret": PAT_SECRET,
		"site": {
			"contentUrl": ""
		}
    }
}
RATE_CARD_LUID = getenv(
    key="RATE_CARD_LUID",
    default=RATE_CARD
)

class TableauData:
    """ Placeholder. """
    def __init__(self) -> None:
        """ Class initialization method. """

        return None

    def auth_and_get_token(self) -> Response:
        """ Placeholder. """

        # Attempt HTTP request
        try:
            response = request(
                method='POST',
                url=AUTH_URL,
                headers=BASE_HEADERS,
                json=AUTH_BODY,
                timeout=HTTP_TIMEOUT
            )
        except requests.ConnectionError as error:
            # Display the error message and exit
            print(error)
            sys.exit(1)


        # Check for HTTP response errors
        response.raise_for_status()

        return response

    def get_rates(
            self,
            auth_header: Dict,
            site_id: str
    ) -> Response:
        """ Placeholder. """

        url = f'{SITE_URL}/{site_id}/views/{RATE_CARD_LUID}/data'

        # Create headers
        headers = {}
        headers.update(BASE_HEADERS)
        headers.update(auth_header)

        # Attempt HTTP request
        try:
            response = request(
                method='GET',
                url=url,
                headers=headers,
                timeout=HTTP_TIMEOUT
            )
        except requests.ConnectionError as error:
            # Display the error message and exit
            print(error)
            sys.exit(1)

        # Check for HTTP response errors
        response.raise_for_status()

        return response

    def read_csv_data(self) -> List[Dict[str, str]]:
        """ Reads CSV data into a list of dictionaries """

        csv_data = []
        with open(
            file='./app/data/mock_csv_response.csv',
            mode='rt',
            encoding='utf-8'
        ) as file:

            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                csv_data.append(row)

        return csv_data

    def load_roles(self) -> List[str]:
        """ Placeholder. """

        desired_roles = []
        with open(
            file='./app/data/roles.yml',
            mode='rt',
            encoding='utf-8'
        ) as file:
            roles_data = yaml.safe_load(file)

        desired_roles = roles_data.get('roles', [])

        return desired_roles

    def filter_role_data(
            self,
            csv_data: List[Dict[str, str]]
    ) -> List[Dict[str, str]]:
        """ Placeholder. """

        desired_roles = self.load_roles()

        necessary_information = ['Job Name', 'Currency Symbol', 'Standard Burden Cost Rate']

        filtered_data = []
        for row in csv_data:
            if row.get('Job Name') in desired_roles:
                filtered_row = {info: row.get(info) for info in necessary_information}
                filtered_data.append(filtered_row)

        return filtered_data

    def display_role_data(
            self,
            filtered_data: List[Dict[str, str]]
    ) -> None:
        """ Placeholder. """

        role_size = 30
        rate_size = 15

        print('Role'.ljust(role_size) + 'Rate'.rjust(rate_size))
        print('-' * (role_size + rate_size))

        for rate in filtered_data:
            role = rate.get('Job Name').ljust(role_size)
            rate = rate.get('Standard Burden Cost Rate').rjust(rate_size)
            print(f"{role}{rate}")

        return None
