# -*- coding: utf-8 -*-
""" Helper for News Articles.

source:
https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/
"""
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateparse import parse_datetime
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from urllib import urlencode
from news.models import Article, Author, Source
import requests
import hashlib
import pytz


class Command(BaseCommand):
    help = 'Fetch new articles from the news api and save in database'
    sources = {}
    authors = {}

    def handle(self, *args, **options):
        self.fetch_news()

    def get_source(self, id, name):
        h = hash(id.lower())
        source = self.sources.get(h)

        if source:
            return source

        try:
            source = Source.objects.get(sid=id)
        except ObjectDoesNotExist:
            source = Source(sid=id, name=name)
            source.save()

        self.sources[h] = source
        return source

    def get_author(self, name):
        h = hash(name.lower())
        author = self.authors.get(h)
        if author:
            return author
        try:
            author = Author.objects.get(name=name)
        except ObjectDoesNotExist:
            author = Author(name=name)
            author.save()
        self.authors[h] = author
        return author

    def fetch_news(self, source_id=None, current_date=None):
        page = 1
        lang = settings.NEWS_API_LANG or 'en'
        while True:
            articles = self.fetch_api(
                page=page,
                source_id=source_id,
                current_date=current_date)

            if not articles:
                break

            for a in articles:

                if not a.get('url'):
                    continue

                article = Article.get_by_url(a.get('url'))
                if article:
                    continue

                pub_date = a.get('publishedAt')

                if pub_date:
                    pub_date = parse_datetime(pub_date)
                else:
                    pub_date = timezone.now()

                article = Article(
                    title=a.get('title'),
                    description=a.get('description'),
                    url=a.get('url').lower(),
                    url_image=a.get('urlToImage'),
                    lang=lang,
                    pub_date=pub_date)

                if a.get('source'):
                    source = a.get('source')
                    article.source = self.get_source(
                        source.get('id'),
                        source.get('name'))

                article.save()

                if a.get('author'):
                    author_names = a.get('author').split(',')
                    author_names = map(lambda x: x.strip(), author_names)
                    authors = map(self.get_author, author_names)
                    for author in authors:
                        article.authors.add(author)
                article.save()

            page += 1

    def fetch_api(self, page=1, source_id=None, current_date=None):
        articles = None

        if settings.NEWS_API_URL and settings.NEWS_API_KEY:
            print('fetching page %s...' % page)
            current_date = current_date if current_date else datetime.today()
            from_date = current_date - timedelta(days=1)
            lang = settings.NEWS_API_LANG or 'en'

            params = {
                'apiKey': settings.NEWS_API_KEY,
                'sources': source_id or settings.NEWS_API_DEFAULT_SOURCE,
                'from': from_date.strftime('%Y-%m-%d'),
                'to': current_date.strftime('%Y-%m-%d'),
                'language': lang,
                'page': page
            }

            url = '%s?%s' % (settings.NEWS_API_URL, urlencode(params))
            r = requests.get(url)
            result = r.json()
            if result['status'] == 'ok' and len(result['articles']) > 0:
                articles = result['articles']

        return articles
