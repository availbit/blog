from django.db import models
from django.utils import timezone


class MyUser(models.Model):
    username = models.CharField(max_length=200, primary_key=True, blank=False)
    password = models.CharField(max_length=7, blank=False)
    regdate  = timezone.now()

    def save(self):
        self.save()

    def __str__(self):
        return self.title
