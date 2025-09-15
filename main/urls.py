# !/usr/bin/env python
# -*- coding: utf-8 -*-

# main/urls.py

from application.urls import blueprints as application_blueprints

def register(app):
  # append sub blueprints
  modules_blueprints = [
    application_blueprints,
  ]
  # load main blueprint to app
  #app.register_blueprint(application_blueprints)
  # load sub blueprints to app
  for blueprints in modules_blueprints:
    for blueprint in blueprints:
      app.register_blueprint(blueprint)