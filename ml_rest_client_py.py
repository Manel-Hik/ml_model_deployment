# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:14:54 2021

@author: acer
"""

import json
import requests

url = 'http://localhost:8000/model'

request_data = json.dumps({'age':42,'salary':50000})
response = requests.post(url,request_data)
print(response.text)