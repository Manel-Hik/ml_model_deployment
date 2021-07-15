# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 21:27:31 2021

@author: acer
"""

import json
import requests

url = 'http://localhost:8000/model'

request_data = json.dumps({'model':'knn'})
response = requests.post(url,request_data)
print(response.text)