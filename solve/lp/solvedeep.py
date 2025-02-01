import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary, LpStatus

# -----------------------------
# Data and Constants
# -----------------------------
# Define max working hours for each designation (you can adjust as needed; here we use the provided values)
# Define max working hours for each designation
MAX_WORKING_HOURS = {
    "Cashier": 36,
    "Inventory Manager": 28,
    "Customer Help": 42,
    "Cleaning Staff": 21,
    "Manager": 28,
    "Supervisor": 36
}

# Required number of employees per shift (adjust these if needed for the new shifts)
REQUIRED_EMPLOYEES = {
    "M": 2,  # Morning shift 8am to 2pm
    "D": 3,  # Day shift 2pm to 6pm
    "N": 1   # Night shift 6pm to 12am
}

# Penalty for overstaffing (Cover)
COVER_PENALTY = {
    "M": 5,
    "D": 3,
    "N": 2
}

# Penalty for understaffing (Cunder)
CUNDER_PENALTY = {
    "M": 4,
    "D": 6,
    "N": 7
}

# Employee data with leave status (all employees have a 'leave' key)
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
shifts = {
    "Day1": [
        {"shift_id": "M", "shift_duration": 6, "shift_timing": "8am to 2pm"},
        {"shift_id": "D", "shift_duration": 4, "shift_timing": "2pm to 6pm"},
        {"shift_id": "N", "shift_duration": 6, "shift_timing": "6pm to 12am"}
    ],
    "Day2": [
        {"shift_id": "M", "shift_duration": 6, "shift_timing": "8am to 2pm"},
        {"shift_id": "D", "shift_duration": 4, "shift_timing": "2pm to 6pm"},
        {"shift_id": "N", "shift_duration": 6, "shift_timing": "6pm to 12am"}
    ],
    "Day3": [
        {"shift_id": "M", "shift_duration": 6, "shift_timing": "8am to 2pm"},
        {"shift_id": "D", "shift_duration": 4, "shift_timing": "2pm to 6pm"},
        {"shift_id": "N", "shift_duration": 6, "shift_timing": "6pm to 12am"}
    ],
    "Day4": [
        {"shift_id": "M", "shift_duration": 6, "shift_timing": "8am to 2pm"},
        {"shift_id": "D", "shift_duration": 4, "shift_timing": "2pm to 6pm"},
        {"shift_id": "N", "shift_duration": 6, "shift_timing": "6pm to 12am"}
    ],
    "Day5": [
        {"shift_id": "M", "shift_duration": 6, "shift_timing": "8am to 2pm"},
        {"shift_id": "D", "shift_duration": 4, "shift_timing": "2pm to 6pm"},
        {"shift_id": "N", "shift_duration": 6, "shift_timing": "6pm to 12am"}
    ],
    "Day6": [
        {"shift_id": "M", "shift_duration": 6, "shift_timing": "8am to 2pm"},
        {"shift_id": "D", "shift_duration": 4, "shift_timing": "2pm to 6pm"},
        {"shift_id": "N", "shift_duration": 6, "shift_timing": "6pm to 12am"}
    ],
    "Day7": [
        {"shift_id": "M", "shift_duration": 6, "shift_timing": "8am to 2pm"},
        {"shift_id": "D", "shift_duration": 4, "shift_timing": "2pm to 6pm"},
        {"shift_id": "N", "shift_duration": 6, "shift_timing": "6pm to 12am"}
    ]
}


# Shift data for each day (for simplicity, each day has the same set of shifts)
# shifts = {
#     "Day1": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
#              {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
#              {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
#              {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
#              {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
#     "Day2": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
#              {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
#              {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
#              {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
#              {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
#     "Day3": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
#              {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
#              {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
#              {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
#              {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
#     "Day4": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
#              {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
#              {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
#              {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
#              {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
#     "Day5": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
#              {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
#              {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
#              {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
#              {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
#     "Day6": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
#              {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
#              {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
#              {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
#              {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}],
#     "Day7": [{"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
#              {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
#              {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
#              {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
#              {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}]
# }

# -----------------------------
# Create and Solve the LP Model
# -----------------------------
def create_and_solve_model(employees, shifts):
    model = LpProblem("Optimal_Shift_Scheduling", LpMinimize)

    # Generate all possible shift keys as (day, shift_id)
    all_shifts = [(day, shift['shift_id']) for day in shifts for shift in shifts[day]]

    # Create decision variables: assign_vars[e, day, shift_id] = 1 if employee e works that shift on that day
    assign_vars = LpVariable.dicts(
        "Assign",
        [(e['e_id'], day, shift['shift_id']) 
         for e in employees 
         for day in shifts 
         for shift in shifts[day] 
         if day not in e['leave']], 
        cat=LpBinary
    )

    # Create auxiliary variables for understaffing and overstaffing for each shift in each day
    under_vars = LpVariable.dicts("Under", all_shifts, lowBound=0, cat='Continuous')
    over_vars = LpVariable.dicts("Over", all_shifts, lowBound=0, cat='Continuous')

    # Objective function: Minimize total penalty for staffing deviations
    model += lpSum(
        under_vars[day, s_id] * CUNDER_PENALTY[s_id] + 
        over_vars[day, s_id] * COVER_PENALTY[s_id]
        for (day, s_id) in all_shifts
    ), "Total_Penalty"

    # Constraint: Maximum weekly hours per employee
    for e in employees:
        model += lpSum(
            assign_vars[e['e_id'], day, shift['shift_id']] * shift['shift_duration']
            for day in shifts 
            for shift in shifts[day]
            if day not in e['leave'] and (e['e_id'], day, shift['shift_id']) in assign_vars
        ) <= MAX_WORKING_HOURS[e['designation']], f"MaxHours_{e['e_id']}"

    # Constraint: Maximum of 2 shifts per day per employee
    for e in employees:
        for day in shifts:
            model += lpSum(
                assign_vars[e['e_id'], day, shift['shift_id']]
                for shift in shifts[day]
                if day not in e['leave'] and (e['e_id'], day, shift['shift_id']) in assign_vars
            ) <= 2, f"MaxShifts_{e['e_id']}_{day}"

    # Constraint: Staffing balance for each shift (soft constraint)
    for day in shifts:
        for shift in shifts[day]:
            s_id = shift['shift_id']
            model += (
                lpSum(
                    assign_vars[e['e_id'], day, s_id]
                    for e in employees
                    if day not in e['leave'] and (e['e_id'], day, s_id) in assign_vars
                ) + under_vars[day, s_id] - over_vars[day, s_id]
                == REQUIRED_EMPLOYEES[s_id]
            ), f"Staffing_{day}_{s_id}"

    # Solve the model
    start_time = time.time()
    model.solve()
    solve_time = time.time() - start_time

    print(f"Status: {LpStatus[model.status]}")
    print(f"Solve time: {solve_time:.2f} seconds")

    # Extract schedule
    schedule = {day: [] for day in shifts}
    for e in employees:
        for day in shifts:
            for shift in shifts[day]:
                s_id = shift["shift_id"]
                key = (e["e_id"], day, s_id)
                if key in assign_vars and assign_vars[key].varValue == 1:
                    schedule[day].append({
                        "e_id": e["e_id"],
                        "e_name": e["e_name"],
                        "shift_id": s_id,
                        "shift_duration": shift["shift_duration"]
                    })
    return model, schedule, under_vars, over_vars

# -----------------------------
# Validate Constraints
# -----------------------------
def validate_constraints(schedule, employees, shifts):
    # Validate maximum working hours
    for e in employees:
        total_hours = sum(
            shift['shift_duration'] for day in schedule 
            for shift in schedule[day] if shift['e_id'] == e['e_id']
        )
        assert total_hours <= MAX_WORKING_HOURS[e['designation']], f"Employee {e['e_id']} exceeds max hours"

    # Validate leave days
    for e in employees:
        for day in e['leave']:
            assert not any(shift['e_id'] == e['e_id'] for shift in schedule.get(day, [])), f"Employee {e['e_id']} assigned on leave day {day}"

    # Validate staffing requirements
    for day in shifts:
        for shift in shifts[day]:
            s_id = shift['shift_id']
            assigned = sum(1 for s in schedule[day] if s['shift_id'] == s_id)
            # Use a tolerance for floating point
            tol = 1e-5
            diff = assigned + under_vars[day, s_id].varValue - over_vars[day, s_id].varValue - REQUIRED_EMPLOYEES[s_id]
            assert abs(diff) < tol, f"Shift {s_id} on {day} has incorrect staffing (diff: {diff})"

# -----------------------------
# Visualize Schedule
# -----------------------------
def visualize_schedule(schedule):
    schedule_df = pd.DataFrame([
        {"Day": day, "Shift": shift['shift_id'], "Employee": shift['e_name']}
        for day in schedule for shift in schedule[day]
    ])
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=schedule_df, x="Day", y="Shift", hue="Employee", s=100)
    plt.title("Employee Shift Assignments")
    plt.show()

# -----------------------------
# Compare with a Random Schedule
# -----------------------------
def compare_with_random(schedule, employees, shifts):
    random_schedule = {day: [] for day in shifts}
    for day in shifts:
        for shift in shifts[day]:
            available_employees = [e for e in employees if day not in e['leave']]
            random.shuffle(available_employees)
            assigned = available_employees[:REQUIRED_EMPLOYEES[shift['shift_id']]]
            for emp in assigned:
                random_schedule[day].append({"e_id": emp['e_id'], "shift_id": shift['shift_id']})
    random_penalty = 0
    for day in shifts:
        for shift in shifts[day]:
            s_id = shift['shift_id']
            assigned = sum(1 for s in random_schedule[day] if s['shift_id'] == s_id)
            if assigned < REQUIRED_EMPLOYEES[s_id]:
                random_penalty += CUNDER_PENALTY[s_id] * (REQUIRED_EMPLOYEES[s_id] - assigned)
            elif assigned > REQUIRED_EMPLOYEES[s_id]:
                random_penalty += COVER_PENALTY[s_id] * (assigned - REQUIRED_EMPLOYEES[s_id])
    print(f"Optimized Penalty: {model.objective.value()}")
    print(f"Random Schedule Penalty: {random_penalty}")

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    # Create and solve model
    model, schedule, under_vars, over_vars = create_and_solve_model(employees, shifts)
    
    # Validate constraints
    validate_constraints(schedule, employees, shifts)
    
    # Visualize schedule
    visualize_schedule(schedule)
    
    # Compare with random schedule
    compare_with_random(schedule, employees, shifts)
    
    # Export schedule to Excel
    with pd.ExcelWriter("optimized_shift_schedule.xlsx") as writer:
        for day in shifts:
            df = pd.DataFrame(schedule[day])
            df.to_excel(writer, sheet_name=day, index=False)
    
    print("Excel file 'optimized_shift_schedule.xlsx' generated.")
