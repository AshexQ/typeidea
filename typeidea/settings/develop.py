#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 小强
# datetime： 2021/1/12 10:12 下午 
# ide： PyCharm
from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

