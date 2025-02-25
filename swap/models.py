from django.db import models

class Shift(models.Model):
    shift_id = models.CharField(max_length=50, primary_key=True)  # e.g., Morning, Day, Evening, Night
    shift_duration = models.IntegerField()  # e.g., 4 hours
    shift_timing = models.CharField(max_length=50)


class ShiftSchedule(models.Model):
    day = models.CharField(max_length=10)  # e.g., Day1, Day2
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    class Meta:
        # Ensures each day can have only one shift of each type
        unique_together = ('day', 'shift')