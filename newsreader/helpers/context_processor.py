# -*- coding: utf-8 -*-
from django.conf import settings


def custom_processor(request):
    config = {
        'SITE_NAME': settings.SITE_NAME,
    }
    return config
