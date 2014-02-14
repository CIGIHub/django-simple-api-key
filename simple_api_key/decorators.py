from models import APIKey
from django.http import HttpResponseForbidden
import json
import functools


class api_key_required(object):

    def __init__(self, func):
        self.func = func
        functools.wraps(self.func)(self)

    def __call__(self, request, *args, **kwargs):
        data = json.loads(request.body)

        key = data.get('api_key', None)
        username = data.get('api_username', None)

        if key is None:
            return HttpResponseForbidden('Invalid or disabled api key')

        api_key = None
        try:
            api_key = APIKey.objects.get(key=key)
        except APIKey.DoesNotExist:
            return HttpResponseForbidden('Invalid or disabled api key')

        if api_key.user.username != username:
            return HttpResponseForbidden('Invalid or disabled api key')

        return self.func(request, *args, **kwargs)