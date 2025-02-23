import pandas as pd
import csv
import random
import os
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# Maximum working hours for each designation
MAX_WORKING_HOURS = {
    "Cashier": 46,
    "Inventory Manager": 38,
    "Customer Help": 42,
    "Cleaning Staff": 48,
    "Manager": 58,
    "Supervisor": 56
}

# Maximum shifts an employee can work per day
MAX_SHIFTS_PER_DAY = 2

# Group employees by designation
employees_by_designation = {}

def iterate(employees):
    for emp in employees:
        designation = emp.get("designation", "Unknown") 
        if designation not in employees_by_designation:
            employees_by_designation[designation] = []

        employees_by_designation[designation].append(emp) 
        
    return employees_by_designation


def get_employee_count_by_designation():
    designation_counts = {}
    shift_types = ["Morning", "Day", "Evening", "Night"]

    # List of all the designations
    designations = ["Cashier", "Manager", "Supervisor",
                    "Cleaning Staff", "Inventory Manager", "Customer Help"]

    for designation in designations:
        designation_counts[designation] = {}

        for shift in shift_types:
            while True:
                try:
                    count = int(
                        input(f"Enter the number of {designation} for {shift} Shift: "))
                    if count < 0:
                        print("Please enter a non-negative number.")
                    else:
                        designation_counts[designation][shift] = count
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    return designation_counts


def assign_shifts(shifts, employees_by_designation, designation_counts, MAX_WORKING_HOURS):
    schedule = []  # Stores shift assignments


    for day, day_shifts in shifts.items():
        assigned_today = {}  # Track how many shifts each employee has today

        for shift in day_shifts:
            shift_id = shift["shift_id"]
            shift_duration = shift["shift_duration"]
            shift_timing = shift["shift_timing"]

            # Assign employees based on their designation
            for designation, req_dict in designation_counts.items():
                # Get required employees for this shift
                required_count = req_dict.get(shift_id, 0)

                for slot in range(required_count):
                    # Find available employees for the current shift
                    available_emps = [
                        emp for emp in employees_by_designation.get(designation, [])
                        if assigned_today.get(emp["e_id"], 0) < MAX_SHIFTS_PER_DAY and
                        (emp["no_of_hours_worked"] + shift_duration <=
                         MAX_WORKING_HOURS[designation])
                    ]

                    # Sort employees by least working hours for fairness
                    available_emps.sort(key=lambda x: x["no_of_hours_worked"])

                    if available_emps:
                        chosen_emp = available_emps[0]
                        # Update employee's total working hours
                        chosen_emp["no_of_hours_worked"] += shift_duration
                        assigned_today[chosen_emp["e_id"]] = assigned_today.get(
                            chosen_emp["e_id"], 0) + 1

                        schedule.append({
                            "Day": day,
                            "Shift": shift_id,
                            "Shift Timing": shift_timing,
                            "Designation": designation,
                            "Employee ID": chosen_emp["e_id"],
                            "Employee Name": chosen_emp["e_name"],
                            "Email": chosen_emp["e_gmail"],
                            "Hours Assigned": shift_duration,
                            "Total Hours After Assignment": chosen_emp["no_of_hours_worked"]
                        })
                    else:
                        # No employee available -> Assign Leave
                        schedule.append({
                            "Day": day,
                            "Shift": shift_id,
                            "Shift Timing": shift_timing,
                            "Designation": designation,
                            "Employee ID": "Leave",
                            "Employee Name": "Leave",
                            "Email": "",
                            "Hours Assigned": 0,
                            "Total Hours After Assignment": None
                        })

    return schedule


def export_schedule_to_excel(schedule, employees, output_file):
    formatted_schedule = {"Employee ID": [], "Employee Name": [], "Designation": [], "Working Hours": []}

    unique_days = sorted(set(entry["Day"] for entry in schedule))

    # Add columns for each day
    for day in unique_days:
        formatted_schedule[day] = []

    # Add a separate dictionary to track total working hours for each employee
    total_working_hours = {emp["e_id"]: emp["no_of_hours_worked"] for emp in employees}

    for employee in employees:
        formatted_schedule["Employee ID"].append(employee["e_id"])
        formatted_schedule["Employee Name"].append(employee["e_name"])
        formatted_schedule["Designation"].append(employee["designation"])
        formatted_schedule["Working Hours"].append(total_working_hours.get(employee["e_id"], 0))

        for day in unique_days:
            assigned_shifts = [
                entry["Shift"] for entry in schedule
                if entry["Day"] == day and entry["Employee ID"] == employee["e_id"]
            ]
            formatted_schedule[day].append(
                ", ".join(assigned_shifts) if assigned_shifts else "Leave")

    df_formatted_schedule = pd.DataFrame(formatted_schedule)
    df_formatted_schedule.to_excel(output_file, index=False)
    print(f"Formatted shift schedule exported to {output_file}")
    os.startfile(output_file)  # Auto-open the file


# Call shift assignment function
# designation_counts = get_employee_count_by_designation()
# schedule = assign_shifts(shifts, employees_by_designation,
#                          designation_counts, MAX_WORKING_HOURS)

# Export results to Excel with total working hours
output_file = "OPT18_with_Working_Hours.xlsx"
# export_schedule_to_excel(schedule, employees, output_file)

