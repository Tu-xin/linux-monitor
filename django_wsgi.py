#!/usr/bin/env python
# coding: utf-8
import os
import sys
from django.core.wsgi import get_wsgi_application,WSGIHandler

reload(sys)
sys.setdefaultencoding('utf8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Linux_form.settings")
application = get_wsgi_application()
#application = WSGIHandler()