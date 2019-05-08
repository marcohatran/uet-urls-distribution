import requests


def check_ip():
    url = 'http://api.ipify.org'
    try:
        r = requests.get(url)
        # print(r.text)
        return r.text
    except requests.ConnectionError as e:
        print(isinstance(e, requests.exceptions.ConnectTimeout))  # true
    return None


def request_with_proxy_automatically():
    pass
