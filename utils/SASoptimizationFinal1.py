from pulp import LpProblem, LpVariable, lpSum, LpMinimize
import pandas as pd
import csv
import random


# defining MAX WORKING HOURS for each designation
MAX_WORKING_HOURS = {
    "Cashier": 36,
    "Inventory Manager": 28,
    "Customer Help": 42,
    "Cleaning Staff": 21,
    "Manager": 28,
    "Supervisor": 36
}

# Initialize the optimization model
model = LpProblem("Weekly_Shift_Schedule", LpMinimize)


# Function to get input counts
def get_employee_count_by_designation():
    designation_counts = {}
    for designation in MAX_WORKING_HOURS.keys():
        while True:
            try:
                count = int(
                    input(f"Enter the number of employees for {designation}: "))
                if count < 0:
                    print("Please enter a non-negative number.")
                else:
                    designation_counts[designation] = count
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return designation_counts




def assign_shifts_randomly(designation_counts, employees, shifts):
    # Initialize the schedule dictionary to group shifts by days
    schedule = {shift.shift_day: [] for shift in shifts}

    for shift in shifts:
        for designation, count in designation_counts.items():
            # Filter employees by designation
            available_employees = [
                emp for emp in employees if emp.designation == designation and emp.no_of_hours_worked < MAX_WORKING_HOURS[designation]
            ]

            # Shuffle employees randomly to ensure fairness
            random.shuffle(available_employees)

            # Assign the required number of employees for the shift
            assigned_employees = available_employees[:count]

            for emp in assigned_employees:
                # Calculate total hours after assignment
                total_hours = emp.no_of_hours_worked + shift.shift_duration

                # Check if assigning the shift exceeds the employee's max hours
                if total_hours <= MAX_WORKING_HOURS[designation]:
                    # Update the employee's working hours
                    emp.no_of_hours_worked = total_hours

                    # Add the employee to the schedule for the current shift day
                    schedule[shift.shift_day].append({
                        "e_id": emp.e_id,
                        "e_name": emp.e_name,
                        "designation": emp.designation,
                        "shift_id": shift.shift_id,
                        "shift_timing": shift.shift_timing,
                        "shift_day": shift.shift_day
                    })

    return schedule



# Get employee counts from the user
# designation_counts = get_employee_count_by_designation()

# Assign shifts based on input
#schedule = assign_shifts_randomly(designation_counts, employees, shifts)

# Exporting the schedule to the required CSV format


# Function to export the schedule to a CSV file
def export_schedule_to_csv(schedule, employees, output_file):
    # Create a dictionary to hold formatted data
    formatted_schedule = {"Employee ID": [], "Designation": []}

    # Add columns for each day
    for day in schedule.keys():
        formatted_schedule[day] = []

    # Fill the formatted data
    for employee in employees:
        formatted_schedule["Employee ID"].append(employee.e_id)  # Accessing e_id using dot notation
        formatted_schedule["Designation"].append(employee.designation)  # Accessing designation using dot notation
        for day in schedule.keys():
            # Find the assigned shift for this employee and day
            assigned_shift_timing = next(
                (entry["shift_timing"] for entry in schedule[day]
                 if entry["e_id"] == employee.e_id),
                "Leave"
            )
            formatted_schedule[day].append(assigned_shift_timing)

    # Convert to DataFrame and export to CSV
    df_formatted_schedule = pd.DataFrame(formatted_schedule)
    df_formatted_schedule.to_csv(output_file, index=False)
    print(f"Formatted schedule exported to {output_file}")

# Use the export function
output_file = "formatted_shift_scheduletest1.csv"

