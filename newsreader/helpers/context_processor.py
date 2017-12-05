# -*- coding: utf-8 -*-
from django.conf import settings


def custom_processor(request):
    config = {
        'site_name': settings.SITE_NAME,
    }
    return config
