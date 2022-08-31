from testRestApi import *

server = "http://127.0.0.1:3000"

def testLogin():
    res = testRoute(POST, f"{server}/api/v1/login", body={
        "username": "test",
        "password": "test",
    })

    print(res.body)

if __name__ == "__main__":
    testLogin()
