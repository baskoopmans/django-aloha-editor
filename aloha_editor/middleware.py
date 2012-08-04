# coding: utf-8

from django.conf import settings
from django.conf.urls.defaults import include, patterns
from django.utils.importlib import import_module

import aloha_editor.urls


class AlohaEditorMiddleware(object):
    """
    Middleware to set up Aloha Editor on incoming request.
    """
    def __init__(self):
        self.override_url = True

    def process_request(self, request):
        if self.override_url:
            urlconf = getattr(request, 'urlconf', settings.ROOT_URLCONF)
            if isinstance(urlconf, basestring):
                urlconf = import_module(getattr(request, 'urlconf', settings.ROOT_URLCONF))

            aloha_editor.urls.urlpatterns += patterns('',
                ('', include(urlconf)),
            )
            self.override_url = False
        request.urlconf = 'aloha_editor.urls'
