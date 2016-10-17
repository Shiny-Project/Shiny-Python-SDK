import json, collections, hashlib
import requests
import config


class ShinyError(Exception):
    def __init__(self, message):
        self.message = message


def add(spider_name, level, data=None, hash=False):
    if data is None:
        data = {}

    url = config.API_HOST + '/Data/add'

    payload = {"api_key": config.API_KEY, "api_secret_key": config.API_SECRET_KEY}

    event = {"level": level, "spiderName": spider_name}

    if hash:
        event["hash"] = hash
    else:
        m = hashlib.md5()
        m.update(json.dumps(collections.OrderedDict(sorted(data.items()))).encode('utf-8'))
        event["hash"] = m.hexdigest()

    sha1 = hashlib.sha1()
    sha1.update(json.dumps(data).encode('utf-8'))
    payload["sign"] = sha1.hexdigest()
    event["data"] = data
    payload["event"] = event
    print(payload)
    response = requests.post(url, json=payload)
    print(response.text)

    if response.status_code != 200:
        raise ShinyError('Network error:' + str(response.status_code))

