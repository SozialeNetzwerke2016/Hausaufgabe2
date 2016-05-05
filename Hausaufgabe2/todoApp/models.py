from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=160)
    process = models.IntegerField(default = 0)
    date = models.DateTimeField(default=datetime.now, blank=True)


