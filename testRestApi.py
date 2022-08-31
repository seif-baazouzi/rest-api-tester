import json
import requests

GET    = "GET"
POST   = "POST"
PUT    = "PUT"
PATCH  = "PATCH"
DELETE = "DELETE"

class Response:
    def __init__(self, res):
        self.raw     = res
        self.status  = res.status_code
        self.headers = res.headers
        self.body    = json.loads(res.text)

def testRoute(method, url, headers={}, body={}):
    res = requests.request(method, url=url, headers=headers, json=body)
    return Response(res)
