#!/usr/bin/env python
# -*- coding: utf-8 -*-

# application/urls.py

from .views import view as applications_views
from .apis import api as application_apis

blueprints = [
  application_apis,
  applications_views,
]