from django.db import models


class Administrator(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
