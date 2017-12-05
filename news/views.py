# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.conf import settings
import requests


class NewsView(View):

    def get(self, request):
        context = {'articles': []}
        if settings.NEWS_API_URL and settings.NEWS_API_KEY:
            url = '%s?sources=%s&apiKey=%s' % (
                settings.NEWS_API_URL,
                settings.NEWS_API_DEFAULT_SOURCE or 'techcrunch',
                settings.NEWS_API_KEY
            )
            r = requests.get(url)
            result = r.json()
            if result['status'] == 'ok':
                context['articles'] = result['articles']

        return render(request, 'news/index.html', context)
