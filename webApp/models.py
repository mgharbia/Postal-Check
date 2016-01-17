from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=50)
    trackNumber = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
