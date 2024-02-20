# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 01:06:49 2023

@author: Mohamed Arafa
"""

import requests 
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL,headers=headers, json=data) 

r.json()