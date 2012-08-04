====================
Django Aloha Editor
====================

The Django Aloha Editor is a WYSIWYG editor for all your Django powered websites
it works easy yust
more details about the panel's content.

Dependencies
============
- Aloha Editor http://aloha-editor.org/
- simplejson

How it works
============
Django Aloha Editor checks the user permissons, wraps the content with a aloha editor div and
saves the edited content with an ajax call

Installation
============

#. Add the `aloha_editor` directory to your Python path.

    Or use pip install git+git://github.com/baskoopmans/django-aloha-editor.git

#. Add the following middleware to your project's `settings.py` file:

	``'aloha_editor.middleware.AlohaEditorMiddleware',``
   
#. Add `aloha_editor` to your `INSTALLED_APPS` setting so Django can find the
   template files associated with Aloha Editor.

   Alternatively, add the path to the aloha editor templates
   (``'path/to/aloha_editor/templates'`` to your ``TEMPLATE_DIRS`` setting.)


Example
=============

{% load aloha_editor %}
<html>
<head>
{% include "aloha_editor/css.html" %}
{% include "aloha_editor/js.html" %}
</head>
<body>
{% aloha_editor object.field %}
</body>
</html>


TODOs and BUGS
==============
See: http://github.com/baskoopmans/django-aloha-editor/issues
