# Copyright (c) 2023 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
import requests


def collect(url: str) -> str:
    """
    Collects the data from the given url
    """
    response = requests.get(url)
    return response.text
