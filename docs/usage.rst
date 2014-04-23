.. _usage:

Usage
=====

 * Generate API Keys for users.  This can be done through the admin interface.

 * Mark functions requiring API keys using the provided decorator and access
   data from post requests.

   .. code-block:: python

    @api_key_required
    def update_data(request):

        if request.method == 'POST':

            full_data = json.loads(request.body)

            data = full_data.get('payload', None)

            # do something useful with the data here

            return HttpResponse("SUCCESS")

        return HttpResponse("POST required", status=405)

 * Make calls to your api.

   .. note:: The version 0.1.1 implementation requires that post data be sent
      as json. The API key must be sent in the body of the message. The structure of the
      data should be as follows.
   .. code-block:: javascript

       {
         'api_key': 'the_api_key_for_the_user',
         'api_username': 'the_django_username_for_the_user',
         'payload': {} // Your data here in any valid format, name corresponds to your code.
       }

.. note:: You may additionally need or want to disable CSRF checking for your api calls by
   adding the
   `@csrf_exempt <https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#django.views.decorators.csrf.csrf_exempt>`_
   decorator depending on the use cases for your API.
