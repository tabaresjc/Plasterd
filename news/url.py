# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import NewsView

# Generate pages following
# https://docs.djangoproject.com/en/1.11/topics/http/urls/#including-other-urlconfs
urlpatterns = [
    url(r'^$', NewsView.as_view()),
]
