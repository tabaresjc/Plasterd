# -*- coding: utf-8 -*-
""" Model for Authors.

Use the Django ORM library to build the models.

source:
https://docs.djangoproject.com/en/1.11/intro/overview/#design-your-model
"""
from __future__ import unicode_literals
from django.db import models as md


class Author(md.Model):
    name = md.CharField(max_length=100)

    def __str__(self):
        return self.name
