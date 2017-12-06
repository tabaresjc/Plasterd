#!/usr/bin/env python
import os
import sys


def set_env():
    """
    setup local environment, env is in ['development', 'testing', 'production']
    """
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        setting_name = 'newsreader.settings.development'
        os.environ['DJANGO_SETTINGS_MODULE'] = setting_name


if __name__ == "__main__":
    set_env()

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
            print(django.get_version())
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
