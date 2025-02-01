import random
import pandas as pd
from pulp import LpProblem, LpVariable, lpSum, LpMinimize

# Define max working hours for each designation
MAX_WORKING_HOURS = {
    "Cashier": 36,
    "Inventory Manager": 28,
    "Customer Help": 42,
    "Cleaning Staff": 21,
    "Manager": 28,
    "Supervisor": 36
}

# Required number of employees per shift
REQUIRED_EMPLOYEES = {
    "M1": 2,  # Morning shift 8am to 11am
    "D1": 3,  # Day shift 11am to 2pm
    "E1": 3,  # Evening shift 2pm to 5pm
    "E2": 2,  # Evening shift 5pm to 8pm
    "N1": 1   # Night shift 8pm to 11pm
}

# Penalty for overstaffing (Cover)
COVER_PENALTY = {
    "M1": 5,  # Cover penalty for morning shift
    "D1": 3,  # Cover penalty for day shift
    "E1": 3,  # Cover penalty for evening shift
    "E2": 5,  # Cover penalty for evening shift
    "N1": 2   # Cover penalty for night shift
}

# Penalty for understaffing (Cunder)
CUNDER_PENALTY = {
    "M1": 4,  # Cunder penalty for morning shift
    "D1": 6,  # Cunder penalty for day shift
    "E1": 5,  # Cunder penalty for evening shift
    "E2": 4,  # Cunder penalty for evening shift
    "N1": 7   # Cunder penalty for night shift
}

# Employee data with leave status
employees = [
    {"e_id": 1, "e_name": "Alice Johnson", "no_of_hours_worked": 0, "designation": "Cashier", "leave": [], "e_priority": 8},
    {"e_id": 2, "e_name": "Bob Smith", "no_of_hours_worked": 0, "designation": "Inventory Manager", "leave": [], "e_priority": 7},
    {"e_id": 3, "e_name": "Carol Davis", "no_of_hours_worked": 0, "designation": "Customer Help", "leave": [], "e_priority": 8},
    {"e_id": 4, "e_name": "David Wilson", "no_of_hours_worked": 0, "designation": "Cleaning Staff", "leave": ["Day2"], "e_priority": 3},
    {"e_id": 5, "e_name": "Eva Brown", "no_of_hours_worked": 0, "designation": "Cashier", "leave": [], "e_priority": 8},
    {"e_id": 6, "e_name": "Shashank Katuwal", "no_of_hours_worked": 0, "designation": "Cashier", "leave": [], "e_priority": 8},
    {"e_id": 7, "e_name": "Bishwa Kandel", "no_of_hours_worked": 0, "designation": "Customer Help", "leave": [], "e_priority": 8},
    {"e_id": 8, "e_name": "Rabi Aryal", "no_of_hours_worked": 0, "designation": "Customer Help", "leave": [], "e_priority": 8},
    {"e_id": 9, "e_name": "Bishwa Kandel", "no_of_hours_worked": 0, "designation": "Manager", "leave": [], "e_priority": 8},
    {"e_id": 10, "e_name": "Sumesh Dhonju", "no_of_hours_worked": 0, "designation": "Supervisor", "leave": [], "e_priority": 8},
    {"e_id": 11, "e_name": "John Doe", "no_of_hours_worked": 0, "designation": "Inventory Manager", "leave": [], "e_priority": 7},
    {"e_id": 12, "e_name": "Jane Smith", "no_of_hours_worked": 0, "designation": "Cashier", "leave": [], "e_priority": 8},
    {"e_id": 13, "e_name": "Mike Brown", "no_of_hours_worked": 0, "designation": "Cleaning Staff", "leave": [], "e_priority": 3},
    {"e_id": 14, "e_name": "Emily Davis", "no_of_hours_worked": 0, "designation": "Customer Help", "leave": [], "e_priority": 8},
    {"e_id": 15, "e_name": "Chris Wilson", "no_of_hours_worked": 0, "designation": "Supervisor", "leave": [], "e_priority": 8},
    {"e_id": 16, "e_name": "Sophia Martinez", "no_of_hours_worked": 0, "designation": "Cashier", "leave": [], "e_priority": 8},
    {"e_id": 17, "e_name": "Liam Taylor", "no_of_hours_worked": 0, "designation": "Manager", "leave": [], "e_priority": 8},
    {"e_id": 18, "e_name": "Emma White", "no_of_hours_worked": 0, "designation": "Cleaning Staff", "leave": ["Day3"], "e_priority": 3},
    {"e_id": 19, "e_name": "Noah Harris", "no_of_hours_worked": 0, "designation": "Customer Help", "leave": [], "e_priority": 8}
]

# Clean up e_id values before converting them to integers
def clean_e_id(e_id):
    # Remove unwanted characters like parentheses or commas
    cleaned_id = ''.join(filter(str.isdigit, str(e_id)))
    return int(cleaned_id) if cleaned_id else None

# Apply cleaning function to employee data
for employee in employees:
    employee["e_id"] = clean_e_id(employee["e_id"])

# Shift data
shifts = {
    "Day1": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
             {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
             {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
             {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
             {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
    "Day2": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
             {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
             {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
             {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
             {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
    "Day3": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
             {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
             {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
             {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
             {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
    "Day4": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
             {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
             {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
             {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
             {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
  "Day5": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day6": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day7": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ]
}

# Function to assign shifts considering leave and penalties
def assign_shifts_with_leave_and_penalties(employees, shifts):
    schedule = {day: [] for day in shifts}
    total_penalty = 0

    for day, day_shifts in shifts.items():
        for shift in day_shifts:
            required_staff = REQUIRED_EMPLOYEES[shift["shift_id"]]
            cover_penalty = COVER_PENALTY[shift["shift_id"]]
            cunder_penalty = CUNDER_PENALTY[shift["shift_id"]]

            # Filter employees who are not on leave and have not exceeded max working hours
            available_employees = [e for e in employees if day not in e["leave"] and e["no_of_hours_worked"] < MAX_WORKING_HOURS[e["designation"]]]

            # Shuffle employees to ensure fairness
            random.shuffle(available_employees)

            # Calculate the number of employees needed and assign shifts
            assigned = available_employees[:required_staff]
            for employee in assigned:
                employee["no_of_hours_worked"] += shift["shift_duration"]
                schedule[day].append({"e_id": employee["e_id"], "e_name": employee["e_name"], "shift_id": shift["shift_id"]})

            # Calculate penalties for understaffing or overstaffing
            if len(assigned) < required_staff:
                total_penalty += cunder_penalty * (required_staff - len(assigned))
            elif len(assigned) > required_staff:
                total_penalty += cover_penalty * (len(assigned) - required_staff)

    return schedule, total_penalty

# Assign shifts and calculate total penalty
schedule, total_penalty = assign_shifts_with_leave_and_penalties(employees, shifts)

# Create a Pandas ExcelWriter to save the schedule
with pd.ExcelWriter('shift_schedule.xlsx') as writer:
    for day, day_schedule in schedule.items():
        df_schedule = pd.DataFrame(day_schedule)
        df_schedule.to_excel(writer, sheet_name=day, index=False)

# Output the total penalty
print(f"Total Penalty: {total_penalty}")
