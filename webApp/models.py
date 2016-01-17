from django.db import models

class Package(models.Model):
    Name = models.CharField(max_length=50)
    TrackNumber = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
