#!/usr/bin/env python
# -*- coding: utf-8 -*-

# main/settings.py

from flask import Flask
from flask_session import Session
from pathlib import Path
from .middlewares import not_found

# Obtén la ruta absoluta a la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent  # dos niveles arriba de settings.py

APP = Flask(
  __name__,
  static_folder=str(BASE_DIR / 'static'),        # ruta absoluta a /static
  static_url_path='/',
  template_folder=str(BASE_DIR / 'templates')   # ruta absoluta a /templates
)

# Configuraciones (tu config aquí)
APP.config['SECRET_KEY'] = 'your_secret_key'
APP.config['SESSION_TYPE'] = 'filesystem'
APP.config['SESSION_PERMANENT'] = False
APP.config['SESSION_USE_SIGNER'] = True
APP.config['SESSION_KEY_PREFIX'] = 'session:'
APP.config['JWT_SECRET_KEY'] = 'tu_clave_secreta_aqui'

Session(APP)

APP.register_error_handler(404, not_found)