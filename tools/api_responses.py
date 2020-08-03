import requests
from json import loads

def get_response(url, params):
    request_headers = {
        "User-Agent": "2GIS pytest 0.1",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Accept-Charset": "utf-8",
        "Accept-Encoding": "compress, gzip",
        "Accept-Language": "ru, en-gb;q=0.8, en;q=0.7"
    }
    test_session = requests.Session()
    req = requests.Request('GET', url=url, headers=request_headers, params=params)
    prepare_request = req.prepare()
    response = test_session.send(prepare_request, allow_redirects=False)
    return response


def count_real_page(items, items_count, api_url):
    page = 0
    while items:
        page += 1
        params = {
            "page": page,
            "page_size": items_count
        }
        api_response = get_response(api_url, params)
        items = loads(api_response.content.decode('utf-8'))["items"]
    return page - 1