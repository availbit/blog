from django.db import models
from django.utils import timezone


class MyUser(models.Model):
    username = models.CharField(max_length=200, primary_key=True, blank=False)
    password = models.CharField(max_length=7, blank=False)
    registered_date = models.DateTimeField(auto_now_add=True)
