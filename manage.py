#!/usr/bin/env python
import os
import sys

ENV_CONFIGS = {
    'prod': 'production',
    'stag': 'staging',
    'test': 'testing',
    'dev': 'development'
}


def set_env(env="dev"):
    """
    setup local environment, env is in ['dev', 'stag', 'prod', ...]
    """
    setting_name = 'newsreader.settings.%s' % ENV_CONFIGS.get(env, 'dev')
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
