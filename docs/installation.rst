.. _installation:

Requirements
============

 * `south <http://south.readthedocs.org/>`_

Installation
============

 * To install ::

    pip install django-simple-api-key

 * Add ``'simple_api_key'`` to your ``INSTALLED_APPS`` setting

   .. code-block:: python

    INSTALLED_APPS = (
        ...
        'simple_api_key',
    )

 * Create the simple_api_key models ::

    python manage.py migrate



