#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import response
import requests


if __name__ == "__main__":
    resonse = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
