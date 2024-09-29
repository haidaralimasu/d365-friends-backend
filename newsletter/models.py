from django.db import models
from datetime import datetime

class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subscribed = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email
