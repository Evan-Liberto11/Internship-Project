#!/usr/local/bin/python3
""" Main application. """

# Imports - Python Standard Library
from typing import Dict
from typing import List

# Imports - Local
from ia_labor_rates import TableauData

def tableau_auth() -> Dict:
    """ Placeholder. """

    td = TableauData()
    response = td.auth_and_get_token()
    credentials = response.json().get("credentials")
    auth_data = {
        "header" : {
            "X-Tableau-Auth" : credentials.get("token")
        },
        "site_id": credentials["site"].get("id")
    }

    return auth_data


def tableau_rates(
        auth_data: Dict
) -> str:
    """ Placeholder. """

    td = TableauData()
    rates = td.get_rates(
        auth_header=auth_data.get('header'),
        site_id=auth_data.get('site_id')
    )

    return rates.text

def file_reader() -> List[Dict[str, str]]:
    """ Placeholder. """

    td = TableauData()
    csv_data = td.read_csv_data()

    return csv_data

def csv_filter(
        csv_data: List[Dict[str, str]]
) -> List[Dict[str, str]]:
    """ Placeholder. """

    td = TableauData()
    filtered_data = td.filter_role_data(csv_data)

    return filtered_data

def display_data(
        filtered_data: List[Dict[str, str]]
) -> None:
    """ Placeholder. """

    td = TableauData()
    td.display_role_data(filtered_data)

    return None

def main() -> None:
    """ Main application function """

    # auth_data = tableau_auth()
    # rates = tableau_rates(
    #     auth_data=auth_data
    # )

    # print(rates)

    csv_data = file_reader()
    filtered_data = csv_filter(
        csv_data
    )
    display_data(filtered_data)

    return None

if __name__ == '__main__':
    main()
