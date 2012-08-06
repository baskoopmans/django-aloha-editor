# coding: utf-8

from django import template
from django.db.models import Model
from django.utils.safestring import mark_safe


register = template.Library()

@register.tag
def aloha_editor(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, variable = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly one argument" % token.contents.split()[0])
    #if variable[0] == variable[-1] and variable[0] in ('"', "'"):
    #   raise template.TemplateSyntaxError("%r tag's argument should not be in quotes" % tag_name)
    return AlohaEditorNode(variable)

class AlohaEditorNode(template.Node):

    def __init__(self, variable):
        self.variable = variable

    def render(self, context):
        request = context['request']

        try:
            object_ref = template.Variable(self.variable.split('.')[-2])
            variable_ref = template.Variable(self.variable)
        except IndexError:
            variable_ref = template.Variable(self.variable)
    
        # Retrieve the object from the template context
        try:
            object = object_ref.resolve(context)
            assert isinstance(object, Model)
        except template.VariableDoesNotExist:
            # No context variable found
            model_name = None
        except AssertionError:
            # Variable was not a model
            model_name = None
        else:
            model_name = object._meta.app_label + '_' + object._meta.module_name

        # check user permissions for the object
        permission_name = '%s.change_%s' % (object._meta.app_label, object._meta.module_name)
        if request.user.has_perm(permission_name) or request.user.is_superuser:
            div_id = '%s-%i-%s' % (model_name, object.id, self.variable.split('.')[-1])
            div_content = variable_ref.resolve(context)
            return '<div class="aloha_editable" style="position: relative; display: inline-block inline; overflow: hidden;" id="aloha-%s">%s</div>' % (div_id, div_content)

        return variable_ref.resolve(context)