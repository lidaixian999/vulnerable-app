# app.py
import requests

def fetch_example():
    response = requests.get("https://httpbin.org/get")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == "__main__":
    fetch_example()