# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class NewsView(View):

    def get(self, request):

        return render(request, 'news/index.html')
