import os
import django
import sys

sys.path.append('C:\\Users\\ASUS\\Desktop\\SASnew')

# Set the DJANGO_SETTINGS_MODULE environment variable to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Initialize Django
django.setup()

# Now you can import your models and interact with the database
from swap.models import Shift , ShiftSchedule


# Step 1: Create shifts if they don't exist

shifts = {
    f"Day{i}": [
        {"shift_id": "Morning", "shift_duration": 4, "shift_timing": "7am to 11am"},
        {"shift_id": "Day", "shift_duration": 4, "shift_timing": "11am to 3pm"},
        {"shift_id": "Evening", "shift_duration": 4, "shift_timing": "3pm to 7pm"},
        {"shift_id": "Night", "shift_duration": 4, "shift_timing": "7pm to 11pm"}
    ]
    for i in range(1, 8)  # Generates Day1 to Day7
}

# Create Shift objects if they don’t exist
for shift_list in shifts.values():
    for shift_data in shift_list:
        shift, created = Shift.objects.get_or_create(
            shift_id=shift_data["shift_id"],
            defaults={
                "shift_duration": shift_data["shift_duration"],
                "shift_timing": shift_data["shift_timing"]
            }
        )

# Create ShiftSchedule objects
for day, shift_list in shifts.items():
    for shift_data in shift_list:
        shift = Shift.objects.get(shift_id=shift_data["shift_id"])  # Get the existing Shift object
        ShiftSchedule.objects.get_or_create(
            day=day,
            shift=shift
        )

