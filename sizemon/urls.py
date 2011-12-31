# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('sizemon.views',
    (r'^$', 'show_home'),
)
