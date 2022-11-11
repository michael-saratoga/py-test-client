#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:11:13 2022

@author: mikelin
"""

import requests

resp = requests.get("http://127.0.0.1:5000")
print(resp.text)