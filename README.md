# Plasterd

Web Application built with Django to fetch and display global news

## Getting Started

### Prerequisites

Install the following software on your PC
- Python 2.7.X
- Git

### Installation 

1. Clone the repository `$ git clone <path to repository>` and `$ cd` into it
2. Run `$ pip install -r requeriments.txt`

### Setup the environment

Before launching the application from your local webserver or from the Django command-line utility, please take your time to setup the environment.

You should try hard not to put any license key, password or any other parameter that is used by any service or API, use the separate settings file for your environment.

Take a look at the folder `newsreader/settings`, there you can find a list of files that will target an specific environment. Just take one file, say development.py.txt and save it as `development.py`.

This file should inherit all settings from newsreader/settings/base.py, and override specifics settings when needed.

```bash
$ export DJANGO_SETTINGS_MODULE=newsreader.settings.development
$ python manage.py runserver
.
.
Django version 1.11, using settings 'newsreader.settings.development'
```

Make sure to fill the following setting with the correct info

```bash
NEWS_API_URL = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = None
NEWS_API_DEFAULT_SOURCE = 'bbc-news'
```

### Setup database

1. run `$ mkdir data`
2. run `$ python manage.py migrate`

### Initialize the database with some data

```bash
$ python manage.py fetchnews
fetching page 1...
fetching page 2...
.
.
```

### Start the application

You may start the application with the following command

```bash
$ python manage.py runserver
.
.
Django version 1.11, using settings 'newsreader.settings.development'
```
