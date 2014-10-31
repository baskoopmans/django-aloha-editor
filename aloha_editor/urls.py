# encoding: utf-8

from django.conf.urls import patterns, url
from django.conf import settings


urlpatterns = patterns('',
    url(r'save_editable/$', 'aloha_editor.views.save_editable', name='save_editable'),
)
