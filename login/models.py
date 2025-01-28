from django.db import models

class HRManager(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=50)  # Renamed 'pass' to avoid conflicts
    name = models.CharField(max_length=50)
