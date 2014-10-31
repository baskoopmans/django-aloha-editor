# encoding: utf-8

import os

from django.conf import settings
from django.db.models import get_model
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_protect, csrf_exempt


#@csrf_protect
@csrf_exempt
def save_editable(request):

    if request.is_ajax() and request.method == u'POST':

        # get data from request
        reference = request.POST.get('editable_reference', '')
        reference_parts = reference.split('-')[1:]

        editable_app, editable_model = reference_parts[0].split('_')
        editable_id = reference_parts[1]
        editable_field = reference_parts[2]
        editable_content = request.POST.get('editable_content', '')

        model = get_model(editable_app, editable_model)

        response_dict = {
            'reference_parts': reference_parts,
            'editable_app': editable_app,
            'editable_model': editable_model,
            'editable_id': editable_id,
            'editable_field': editable_field,
            'editable_content': editable_content,
        }

        # save data
        try:
            obj = model.objects.get(pk=editable_id)
            response_dict.update({'success': True})
        except model.DoesNotExist:
            response_dict.update({'errors': {}})
            for key, value in response_dict.values():
                if not value:
                    response_dict['errors'].update({ key: 'This field is required'})

        setattr(obj, editable_field, editable_content)
        obj.save()

    else:
        response_dict = { 'success': False }

    return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
