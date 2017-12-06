# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from newsreader.helpers.template import render_view
from news.models import Article


class NewsView(View):

    def get(self, request):
        is_json = request.content_type == 'application/json'
        limit = 100 if is_json else 20
        items, total = Article.get_articles(limit=limit)
        data = {
            'articles': items,
            'total': total,
            'limit': limit
        }
        return render_view(request, 'news/index.html', data)
