from testRestApi import *

server = "http://127.0.0.1:3000"

def testLogin():
    res = testRoute(POST, f"{server}/api/v1/login", body={
        "username": "test",
        "password": "test",
    })

    return "message" in res.body and res.body["message"] == "success"

def testSignup():
    res = testRoute(POST, f"{server}/api/v1/signup", body={
        "username": "test",
        "password": "test",
    })

    return "message" in res.body and res.body["message"] == "success"

if __name__ == "__main__":
    exitCode = runTests([
        Test("Signup Route", testSignup),
        Test("Login Route", testLogin),
    ])

    exit(exitCode)
