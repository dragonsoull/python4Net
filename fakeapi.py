#!/usr/bin/env python3

import requests
import json
url="https://fakestoreapi.com/products/1"

response = requests.get(url)
print(response.json())
print("")
url="https://postman-echo.com/basic-auth"
response=requests.get(url,auth=("postman","password"))
print(response.json())
