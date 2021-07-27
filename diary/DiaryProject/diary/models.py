from typing import Tuple
from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=50, default='')
    body = models.TextField(default='')
    time = models.DateTimeField()
    photo = models.ImageField(upload_to="diary/", blank=True, null=True)
    weather = models.CharField(max_length=20, default='')

    def __str__(self) :
        return self.title