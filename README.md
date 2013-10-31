==============
Simple Api Key
==============

Simple Api Key is a simple Django app to provide users api keys.  A decorator is provided for requiring
the api_key and api_username in an HTTP Request.  This should only be used with secure connections, for
example when using SSL.

Quick start
-----------

1. Add "simple_api_key" to your INSTALLED_APPS setting like this::
        INSTALLED_APPS = (
                ...
                'simple_api_key',
        )
2. This app uses south to manage database migrations.
   Run `python manage.py migrate` to create the simple_api_key models.
