# encoding: utf-8

from django.conf.urls import patterns, url
import django


if django.VERSION >= (1, 9, 0, ):
    from .views import save_editable
    urlpatterns = [
        url(r'save_editable/$', save_editable, name='save_editable'),
    ]
else:
    urlpatterns = patterns('',
        url(r'save_editable/$', 'aloha_editor.views.save_editable', name='save_editable'),
    )
