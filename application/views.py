#!/usr/bin/env python
# -*- coding: utf-8 -*-

# application/views.py

from flask import Blueprint, render_template

view = Blueprint(
  'admin-view-user', 
  __name__
)

@view.route('/', methods=['GET'])
def index():
  locals = {
    'title': 'Home',
    'nav_active': 'home',
    'message': '',
  }
  return render_template('index.html', locals=locals)

