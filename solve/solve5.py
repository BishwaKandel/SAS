import pandas as pd
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary, LpStatus

# Existing constants and employee data remain unchanged
MAX_WORKING_HOURS = {
    "Cashier": 36,
    "Inventory Manager": 28,
    "Customer Help": 42,
    "Cleaning Staff": 21,
    "Manager": 28,
    "Supervisor": 36
}

REQUIRED_EMPLOYEES = {
    "M1": 2,
    "D1": 3,
    "E1": 3,
    "E2": 2,
    "N1": 1
}

COVER_PENALTY = {
    "M1": 5,
    "D1": 3,
    "E1": 3,
    "E2": 5,
    "N1": 2
}

CUNDER_PENALTY = {
    "M1": 4,
    "D1": 6,
    "E1": 5,
    "E2": 4,
    "N1": 7
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
# Shift data as defined earlier...

# Create the optimization model
model = LpProblem("Optimal_Shift_Scheduling", LpMinimize)

# Generate all possible shifts (day + shift_id combinations)
all_shifts = [(day, shift['shift_id']) for day in shifts.keys() for shift in shifts[day]]

# Create decision variables
assign_vars = LpVariable.dicts(
    "Assign", 
    [(e['e_id'], day, shift['shift_id']) 
     for e in employees 
     for day in shifts.keys() 
     for shift in shifts[day] 
     if day not in e['leave']], 
    cat=LpBinary
)

under_vars = LpVariable.dicts("Under", all_shifts, lowBound=0, cat='Continuous')
over_vars = LpVariable.dicts("Over", all_shifts, lowBound=0, cat='Continuous')

# Objective function: Minimize total penalty
model += lpSum(
    under_vars[day, shift_id] * CUNDER_PENALTY[shift_id] + 
    over_vars[day, shift_id] * COVER_PENALTY[shift_id] 
    for (day, shift_id) in all_shifts
)

# Constraints

# 1. Maximum weekly hours constraint
for e in employees:
    model += lpSum(
        assign_vars[e['e_id'], day, shift['shift_id']] * shift['shift_duration']
        for day in shifts.keys() 
        for shift in shifts[day]
        if day not in e['leave'] and (e['e_id'], day, shift['shift_id']) in assign_vars
    ) <= MAX_WORKING_HOURS[e['designation']]

# 2. Employee shift limit (No more than 2 shifts per day)
for e in employees:
    for day in shifts.keys():
        model += lpSum(
            assign_vars[e['e_id'], day, shift['shift_id']] 
            for shift in shifts[day]
            if day not in e['leave'] and (e['e_id'], day, shift['shift_id']) in assign_vars
        ) <= 2  # Max 2 shifts per day for each employee

# 3. Staffing balance constraint (For each shift)
for day in shifts.keys():
    for shift in shifts[day]:
        shift_id = shift['shift_id']
        model += (
            lpSum(
                assign_vars[e['e_id'], day, shift_id]
                for e in employees
                if day not in e['leave'] and (e['e_id'], day, shift_id) in assign_vars
            ) + under_vars[day, shift_id] - over_vars[day, shift_id] 
            == REQUIRED_EMPLOYEES[shift_id]
        )

# Solve the model
model.solve()
print(f"Status: {LpStatus[model.status]}")

# Extract results
schedule = {day: [] for day in shifts.keys()}
for var in model.variables():
    if "Assign" in var.name and var.varValue == 1:
        # Parse variable name
        parts = var.name.split('_')
        
        # Extract and clean e_id, day, and shift_id
        e_id = parts[1].replace("(", "").replace(",", "").strip()
        day = parts[2].replace(",", "").replace("'", "").strip()
        shift_id = parts[3].replace(")", "").replace("'", "").strip()
        
        # Convert e_id to integer
        e_id = int(e_id)
        
        # Find the employee
        emp = next(e for e in employees if e['e_id'] == e_id)
        
        # Add to schedule
        schedule[day].append({
            "e_id": e_id,
            "e_name": emp['e_name'],
            "shift_id": shift_id
        })

# Export to Excel
with pd.ExcelWriter('optimized_shift_schedule1.xlsx') as writer:
    for day in shifts.keys():
        df = pd.DataFrame(schedule[day])
        df.to_excel(writer, sheet_name=day, index=False)

print(f"Total Penalty: ${model.objective.value():.2f}")
