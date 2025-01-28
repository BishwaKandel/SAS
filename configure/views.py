from django.shortcuts import render
from utils.SASoptimizationFinal1 import assign_shifts_randomly, get_employee_count_by_designation , export_schedule_to_csv, output_file
from configure.models import Employee
from swap.models import Shift



def configure_view(request):
    # Fetch all employees and shifts from the database
    employees = Employee.objects.all()
    shifts = Shift.objects.all()

    # Print employees and shifts for debugging
    print("Employees:")
    for employee in employees:
        print(f"ID: {employee.e_id}, Name: {employee.e_name}, Designation: {employee.designation}")

    print("\nShifts:")
    for shift in shifts:
        print(f"ID: {shift.shift_id}, Day: {shift.shift_day}, Timing: {shift.shift_timing}, Priority: {shift.shift_priority}")

    # Fetch employee counts by designation (utility function)
    designation_counts = get_employee_count_by_designation()
    print("\nEmployee counts by designation:")
    print(designation_counts)

    # Assign shifts randomly (utility function)
    schedule =  assign_shifts_randomly(designation_counts, employees, shifts)
    export_schedule_to_csv(schedule, employees, output_file)
    # Render the configure.html template
    return render(request, 'configure.html', {
        'employees': employees,
        'shifts': shifts,
    })


#configure html ma dtl format ma input line ani tyo view ma