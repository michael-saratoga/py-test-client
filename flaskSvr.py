#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:16:16 2022

@author: mikelin
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_word():
    return jsonify({'message' : 'Hello, World'})

if (__name__=='__main__'):
    app.run(debug=True)
    


