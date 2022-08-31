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

class Test:
    def __init__(self, title, function):
        self.title = title
        self.function = function

    def run(self):
        res = self.function()
        resMessage = "success" if res else "failed"
        
        print(f"{self.title}:\t {resMessage}")
        
        return res

def runTests(tests):
    testsCount = 0
    successCount = 0

    for test in tests:
        if test.run():
            successCount += 1
        testsCount += 1

    failedCount = testsCount - successCount
    print(f"\nRun {testsCount} tests, {successCount} are success and {failedCount} are failed")

    return 0 if failedCount == 0 else 1
