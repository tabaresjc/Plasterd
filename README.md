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

There are two ways you can start the app for the inteded environment

1. Via Django Command line

```bash
$ python manage.py runserver ENV
.
Django version 1.11, using settings 'newsreader.settings.development'
```

`ENV` should be name of the file where your settings resides (development, testing or production). Also `ENV` can be left empty, in which case the app will fallback to **development**. 

2. Via environment setting

```bash
$ export DJANGO_SETTINGS_MODULE=newsreader.settings.ENV
$ python manage.py runserver
.
Django version 1.11, using settings 'newsreader.settings.development'
```

As before ENV can be development, testing or production

### Setup database

1. run `$ mkdir data`
2. run `$ python manage.py migrate`
