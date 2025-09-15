#!/usr/bin/env python
# -*- coding: utf-8 -*-

# main/middlewares.py

from functools import wraps
from flask import render_template, session, redirect, request, jsonify

def not_found(e):
  if request.method == 'GET':
    extensions_to_check = ['.css', '.js', '.woff', 'png']
    if any(ext in request.url for ext in extensions_to_check):
      return jsonify({
        'error': 'Recurso no encontrado',
        'status_code': 404,
        'url': request.url
      }), 404
    else:
      return render_template('not_found.html'), 404
  else:
    return jsonify({
      'error': 'Recurso no encontrado',
      'status_code': 404,
      'method': request.method,
      'url': request.url
    }), 404

