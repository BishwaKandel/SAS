from django.db import models

class Shift(models.Model):
    shift_id = models.IntegerField(primary_key=True)  # Integer primary key
    shift_duration = models.IntegerField()  # Integer field for duration
    shift_timing = models.CharField(max_length=50)  # CharField with max length 50
    shift_day = models.CharField(max_length=50)  # CharField with max length 50
    shift_priority = models.IntegerField() 
# Create your models here.
