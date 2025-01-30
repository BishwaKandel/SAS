import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Initialize Django
django.setup()

# Now you can import your models and interact with the database
from swap.models import Shift



# Define the data as a list of tuples
shift_data = [
    (3, 'M1', 'Day1', 1),
    (3, 'D2', 'Day1', 2),
    (3, 'D2', 'Day1', 3),
    (3, 'E1', 'Day1', 1),
    (3, 'N1', 'Day1', 1),
    (3, 'M1', 'Day2', 1),
    (3, 'D2', 'Day2', 2),
    (3, 'D2', 'Day2', 3),
    (3, 'E1', 'Day2', 1),
    (3, 'N1', 'Day2', 1),
    (3, 'M1', 'Day3', 1),
    (3, 'D2', 'Day3', 2),
    (3, 'D2', 'Day3', 3),
    (3, 'E1', 'Day3', 1),
    (3, 'N1', 'Day3', 1),
    (3, 'M1', 'Day4', 1),
    (3, 'D2', 'Day4', 2),
    (3, 'D2', 'Day4', 3),
    (3, 'E1', 'Day4', 1),
    (3, 'N1', 'Day4', 1),
    (3, 'M1', 'Day5', 1),
    (3, 'D2', 'Day5', 2),
    (3, 'D2', 'Day5', 3),
    (3, 'E1', 'Day5', 1),
    (3, 'N1', 'Day5', 1),
    (3, 'M1', 'Day6', 1),
    (3, 'D2', 'Day6', 2),
    (3, 'D2', 'Day6', 3),
    (3, 'E1', 'Day6', 1),
    (3, 'N1', 'Day6', 1),
    (3, 'M1', 'Day7', 1),
    (3, 'D2', 'Day7', 2),
    (3, 'D2', 'Day7', 3),
    (3, 'E1', 'Day7', 1),
    (3, 'N1', 'Day7', 1),
]

# Insert the data into the Shift model
for shift in shift_data:
    Shift.objects.create(shift_duration=shift[0], shift_timing=shift[1], shift_day=shift[2], shift_priority=shift[3])
