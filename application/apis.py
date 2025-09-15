#!/usr/bin/env python
# -*- coding: utf-8 -*-

# application/apis.py

from flask import Blueprint

api = Blueprint(
  'application-apis', 
  __name__
)

@api.route('/api/v1/demo', methods=['GET'])
def index():
  return 'hola mundo'