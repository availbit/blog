from django.db import models
from django.utils import timezone

# Create your models here.

class MyUser(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_legth=7)

    def __str__(self):
        return self.title

