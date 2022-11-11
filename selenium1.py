#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:13:20 2022

@author: mikelin
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys,os


options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("http://127.0.0.1:5000")