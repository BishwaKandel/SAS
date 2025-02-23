from django.shortcuts import render
from django.conf import settings
import os
import logging
from utils.opt2 import (
    get_employee_count_by_designation,
    export_schedule_to_excel,
    assign_shifts,
    employees_by_designation,
    MAX_WORKING_HOURS,
    iterate
)
from swap.models import Shift,ShiftSchedule
from configure.models import Employee

logger = logging.getLogger(__name__)


def configure_view(request):
    # Convert QuerySet to list of dictionaries
    employees = list(Employee.objects.all().values())

    # Group employees by designation (only call once!)
    data = iterate(employees)
    print(employees)

    shifts = Shift.objects.all()

    # Convert QuerySet to a dictionary
    shifts = Shift.objects.all()


# Get all shift schedules, including the associated shift details
    shift_schedules = ShiftSchedule.objects.select_related('shift').all()

    # Convert QuerySet to a dictionary
    shifts_dict = {}
    for shift_schedule in shift_schedules:
        shift = shift_schedule.shift  # Access the related Shift object
        day = shift_schedule.day  # Day from ShiftSchedule model

        shifts_dict.setdefault(day, []).append({
            "shift_id": shift.shift_id,
            "shift_duration": shift.shift_duration,
            "shift_timing": shift.shift_timing
        })



    # Debugging: Print the shift structure to confirm format
    print("Shifts Dict:", shifts_dict)

    # Assign shifts
    designation_counts = get_employee_count_by_designation()
    print("Designation Counts:", designation_counts)  # Debugging

    schedule = assign_shifts(
        shifts_dict, data, designation_counts, MAX_WORKING_HOURS)

    # Save to Excel
    output_file = os.path.join(
        settings.MEDIA_ROOT, "OPT22_with_Working_Hours.xlsx")
    export_schedule_to_excel(schedule, employees, output_file)

    return render(request, 'configure.html', {'employees': employees, 'shifts': shifts})
