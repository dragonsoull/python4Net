#!/usr/bin/env python3

import requests
import json
url="https://fakestoreapi.com/products/1"

response = requests.get(url)
print(response.json())