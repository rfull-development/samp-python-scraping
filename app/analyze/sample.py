# Copyright (c) 2023 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
import bs4


def analyze(body: str) -> dict:
    """
    Analyze the HTML body and return the meta tags.
    """
    html = bs4.BeautifulSoup(body, 'html.parser')
    head = html.find('head')
    metas = head.find_all('meta')
    results = {}
    for meta in metas:
        name = meta.get('name')
        content = meta.get('content')
        results[name] = content
    return results
