# coding: utf-8

"""
URLpatterns for the aloha editor. 
These should not be loaded explicitly; the aloha editor middleware will patch this into the urlconf for the request.
"""
from django.conf.urls.defaults import *
from django.conf import settings


_PREFIX = '__aloha__'

urlpatterns = patterns('',
    url(r'^%s/save_editable/$' % _PREFIX, 'aloha_editor.views.save_editable', name='aloha_editor_save_editable'),
)
