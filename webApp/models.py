from django.db import models

class Package(models.Model):
    Name = models.CharField(max_length=100)
    TrackNumber = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)