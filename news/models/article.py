# -*- coding: utf-8 -*-
""" Model for News Articles.

Use the Django ORM library to build the md.

source:
https://docs.djangoproject.com/en/1.11/intro/overview/#design-your-model
"""
from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models as md
from author import Author
from source import Source
from datetime import datetime


class Article(md.Model):
    title = md.CharField(max_length=200)
    description = md.TextField()
    url = md.CharField(max_length=512, unique=True)
    url_image = md.CharField(max_length=512, null=True)
    lang = md.CharField(max_length=10, default='en')
    authors = md.ManyToManyField(Author)
    source = md.ForeignKey(Source, on_delete=md.CASCADE)
    pub_date = md.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            md.Index(fields=['url']),
            md.Index(fields=['lang']),
        ]

    @classmethod
    def get_articles(cls, page=1, limit=20):
        q = cls.objects.order_by('-pub_date')
        total = q.count()
        return q[(page - 1) * limit:limit], total

    @classmethod
    def get_by_url(cls, url):
        if not url:
            return None
        try:
            return cls.objects.get(url=url.lower())
        except ObjectDoesNotExist:
            return False
