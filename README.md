# REST API Tester

This is a simple python library for helping you on testing rest apis.

# How To use

Create a test function

```python
def testLogin():
    res = testRoute(POST, f"{server}/api/v1/login", body={
        "username": "test",
        "password": "test",
    })

    return res.hasKeys("message") and res.equals({ "message": "success" })
```

The supported methods are

```
GET
POST
PUT
PATCH
DELETE
```

And the response object has 3 properties and 2 methods to help you checking the response

```python
class Response:
    def __init__(self, res):
        self.raw     = res
        self.status  = res.status_code
        self.headers = res.headers
        self.body    = json.loads(res.text)
    
    # check if the following keys are exist in the body
    def hasKeys(self, *keys):
        ...
    
    # check if the following keys are exist in the body and they are equals to there values
    def equals(self, keyValuePairs):
        ...
```

Then run the test and set the exit code for the test script

```python
if __name__ == "__main__":
    exitCode = runTests([
        Test("Signup Route", testSignup),
        Test("Login Route", testLogin),
    ])

    exit(exitCode)
```
