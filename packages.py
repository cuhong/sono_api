# ./ssh.sh
# cd sonotest
# source ./env/bin/activate

import requests
from furl import furl


def build_url(url, uri, query=None):
    query = {} if query is None else query
    f = furl(url)
    f.path.add(uri)
    for k, v in query.items():
        f.args[k] = v
    return f.url


BUSINESS_ID = "tonton_api_2"
BASE_URL = "https://sonoapi.traveland.co.kr"


def get_token(business_id):
    # 토큰검색 / PKG-001
    uri = "/api/ota/v1/token/tokens"
    query = {"businessId": business_id}
    url = build_url(BASE_URL, uri, query=query)
    headers = {
        "contents-type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response
