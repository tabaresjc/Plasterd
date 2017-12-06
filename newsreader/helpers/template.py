# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.db.models.query import QuerySet
import json

_json_header = 'application/json'


def render_view(request, template, data=None):
    """Renders check the request type and output HTML/JSON."""

    is_json = request.content_type == 'application/json'

    if is_json:
        response = {
            'status': 'OK',
            'data': {}
        }
        for key, value in data.iteritems():
            if isinstance(value, QuerySet):
                d = serializers.serialize('json', value)
                response['data'][key] = json.loads(d)
            else:
                response['data'][key] = value
        return JsonResponse(response)
    else:
        return render(request, template, data)
