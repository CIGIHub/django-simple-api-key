from django.db import models
from django.contrib.auth.models import User
import string
import random


def generate_key(size=40, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class APIKey(models.Model):
    user = models.ForeignKey(User)
    key = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return "%s: %s" % (self.user, self.key)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = generate_key()

        super(APIKey, self).save(*args, **kwargs)
