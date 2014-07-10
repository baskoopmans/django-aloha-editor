====================
Django Aloha Editor
====================

The Django Aloha Editor is a WYSIWYG editor for all your Django powered websites
By default it always uses the latest version of Aloha Editor http://aloha-editor.org/

Dependencies
============
- simplejson

How it works
============
Django Aloha Editor checks the user permissons, wraps the content with an aloha editor div and
saves the edited content with an ajax call.

Installation
============

#. Add the `aloha_editor` directory to your Python path.

   Or use pip install django-aloha-editor

#. Add the following middleware to your project's `settings.py` file:

	``'aloha_editor.middleware.AlohaEditorMiddleware',``
   
#. Add ``aloha_editor`` to your ``INSTALLED_APPS`` setting so Django can find the
   template files and tags associated with Aloha Editor.


Example
=============
``
{% load aloha_editor %}
<html>
<head>
{% if user.is_authenticated %}
{% include "aloha_editor/css.html" %}
{% include "aloha_editor/js.html" %}
{% endif %}
</head>
<body>
{% aloha_editor object.field %}
</body>
</html>
``

TODOs and BUGS
==============
See: http://github.com/baskoopmans/django-aloha-editor/issues
