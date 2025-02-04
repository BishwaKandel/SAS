import pandas as pd

# ----- Data Setup -----
employees = [
    {"e_id": 1, "e_name": "Alice Johnson", "no_of_hours_worked": 0, "designation": "Cashier", "e_gmail": "alice.johnson@email.com", "e_priority": 8},
    {"e_id": 2, "e_name": "Bob Smith", "no_of_hours_worked": 0, "designation": "Inventory Manager", "e_gmail": "bob.smith@email.com", "e_priority": 7},
    {"e_id": 3, "e_name": "Carol Davis", "no_of_hours_worked": 0, "designation": "Customer Help", "e_gmail": "carol.davis@email.com", "e_priority": 8},
    {"e_id": 4, "e_name": "David Wilson", "no_of_hours_worked": 0, "designation": "Cleaning Staff", "e_gmail": "david.wilson@email.com", "e_priority": 3},
    {"e_id": 5, "e_name": "Eva Brown", "no_of_hours_worked": 0, "designation": "Cashier", "e_gmail": "eva.brown@email.com", "e_priority": 8},
    {"e_id": 6, "e_name": "Shashank Katuwal", "no_of_hours_worked": 0, "designation": "Cashier", "e_gmail": "katu@email.com", "e_priority": 8},
    {"e_id": 7, "e_name": "Bishwa Kandel", "no_of_hours_worked": 0, "designation": "Customer Help", "e_gmail": "carolbishwa@email.com", "e_priority": 8},
    {"e_id": 8, "e_name": "Rabi Aryal", "no_of_hours_worked": 0, "designation": "Customer Help", "e_gmail": "carolRabi@email.com", "e_priority": 8},
    {"e_id": 9, "e_name": "Bishwa Kandel", "no_of_hours_worked": 0, "designation": "Manager", "e_gmail": "carolbis@email.com", "e_priority": 8},
    {"e_id": 10, "e_name": "Sumesh Dhonju", "no_of_hours_worked": 0, "designation": "Supervisor", "e_gmail": "carolSum@email.com", "e_priority": 8},
    {"e_id": 11, "e_name": "John Doe", "no_of_hours_worked": 0, "designation": "Inventory Manager", "e_gmail": "john.doe@email.com", "e_priority": 7},
    {"e_id": 12, "e_name": "Jane Smith", "no_of_hours_worked": 0, "designation": "Cashier", "e_gmail": "jane.smith@email.com", "e_priority": 8},
    {"e_id": 13, "e_name": "Mike Brown", "no_of_hours_worked": 0, "designation": "Cleaning Staff", "e_gmail": "mike.brown@email.com", "e_priority": 3},
    {"e_id": 14, "e_name": "Emily Davis", "no_of_hours_worked": 0, "designation": "Customer Help", "e_gmail": "emily.davis@email.com", "e_priority": 8},
    {"e_id": 15, "e_name": "Chris Wilson", "no_of_hours_worked": 0, "designation": "Supervisor", "e_gmail": "chris.wilson@email.com", "e_priority": 8},
    {"e_id": 16, "e_name": "Sophia Martinez", "no_of_hours_worked": 0, "designation": "Cashier", "e_gmail": "sophia.martinez@email.com", "e_priority": 8},
    {"e_id": 17, "e_name": "Liam Taylor", "no_of_hours_worked": 0, "designation": "Manager", "e_gmail": "liam.taylor@email.com", "e_priority": 8},
    {"e_id": 18, "e_name": "Emma White", "no_of_hours_worked": 0, "designation": "Cleaning Staff", "e_gmail": "emma.white@email.com", "e_priority": 3},
    {"e_id": 19, "e_name": "Noah Harris", "no_of_hours_worked": 0, "designation": "Customer Help", "e_gmail": "noah.harris@email.com", "e_priority": 8},
]

shifts = {
    "Day1": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day2": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day3": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day4": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
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

# Maximum working hours by designation
MAX_WORKING_HOURS = {
    "Cashier": 36,
    "Inventory Manager": 28,
    "Customer Help": 42,
    "Cleaning Staff": 21,
    "Manager": 28,
    "Supervisor": 36
}

# ----- Allowed Shifts per Day for Each Position -----
# This parameter determines how many shifts an employee of a given designation can work in one day.
allowed_shifts_per_day = {
    "Cashier": 2,
    "Inventory Manager": 2,
    "Customer Help": 3,
    "Cleaning Staff": 1,
    "Manager": 1,
    "Supervisor": 2
}

# ----- Required Employees Configuration -----
required_employees_config = {
    "Cashier": {"M1": 1, "D1": 2, "E1": 2, "E2": 2, "N1": 1},
    "Inventory Manager": {"M1": 1, "D1": 1, "E1": 1, "E2": 1, "N1": 1},
    "Customer Help": {"M1": 1, "D1": 2, "E1": 2, "E2": 2, "N1": 1},
    "Cleaning Staff": {"M1": 0, "D1": 1, "E1": 1, "E2": 1, "N1": 0},
    "Manager": {"M1": 0, "D1": 1, "E1": 1, "E2": 1, "N1": 0},
    "Supervisor": {"M1": 0, "D1": 1, "E1": 1, "E2": 1, "N1": 0}
}

# ----- Helper Function -----
def get_available_employees(designation, shift_duration, day):
    """
    Returns a list of eligible employees for the given designation who can work
    an additional shift of the given duration on the specified day.
    Eligibility is determined by:
      - The total working hours (including this shift) must not exceed the maximum.
      - The number of shifts already assigned on that day must be less than the allowed limit.
    The returned list is sorted by priority (descending) and then by the number of hours already worked (ascending).
    """
    eligible = []
    for emp in employees:
        if emp["designation"] == designation:
            # Check maximum working hours constraint.
            if emp["no_of_hours_worked"] + shift_duration > MAX_WORKING_HOURS.get(designation, 0):
                continue

            # Count shifts already assigned for the current day.
            assigned_today = sum(1 for shift in emp.get("assigned_shifts", []) if shift["day"] == day)
            # Check against the allowed number of shifts per day.
            if assigned_today >= allowed_shifts_per_day.get(designation, 0):
                continue

            eligible.append(emp)
    eligible.sort(key=lambda x: (-x["e_priority"], x["no_of_hours_worked"]))
    return eligible

# ----- Shift Allocation Algorithm -----
# Loop over each day and each shift; for each designation, determine the required count based on the shift.
for day, day_shifts in shifts.items():
    for shift in day_shifts:
        shift_id = shift["shift_id"]
        shift_duration = shift["shift_duration"]
        shift_timing = shift["shift_timing"]

        for designation, config in required_employees_config.items():
            # Get required number for this designation and shift.
            required_count = config.get(shift_id, 0)
            if required_count == 0:
                continue  # Skip if none required.

            eligible_emps = get_available_employees(designation, shift_duration, day)
            if len(eligible_emps) < required_count:
                print(f"[ERROR] On {day} shift {shift_id} ({shift_timing}) for '{designation}': "
                      f"Required {required_count}, but found only {len(eligible_emps)} eligible employees.")
            else:
                selected_emps = eligible_emps[:required_count]
                for emp in selected_emps:
                    emp["no_of_hours_worked"] += shift_duration
                    if "assigned_shifts" not in emp:
                        emp["assigned_shifts"] = []
                    emp["assigned_shifts"].append({
                        "day": day,
                        "shift_id": shift_id,
                        "shift_timing": shift_timing,
                        "shift_duration": shift_duration
                    })

# ----- Build Aggregated Report -----
# Report columns: "Employee ID", "Employee Name", "Department", "Position",
# "Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7", "Total Working Hours"
days = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7"]
report_rows = []
for emp in employees:
    row = {
        "Employee ID": emp["e_id"],
        "Employee Name": emp["e_name"],
        "Department": "ND",  # Department not provided.
        "Position": emp["designation"]
    }
    day_shifts = {day: [] for day in days}
    if "assigned_shifts" in emp:
        for assign in emp["assigned_shifts"]:
            day_shifts[assign["day"]].append(assign["shift_id"])
    # If no shift is assigned for a given day, record "NE"
    for day in days:
        row[day] = ", ".join(day_shifts[day]) if day_shifts[day] else "NE"
    row["Total Working Hours"] = emp["no_of_hours_worked"]
    report_rows.append(row)

df_report = pd.DataFrame(report_rows,
    columns=["Employee ID", "Employee Name", "Department", "Position",
             "Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7",
             "Total Working Hours"])

# ----- Write Excel Report with Custom Formatting -----
# Group rows by Position with a blank row between groups and assign each group a background color.
group_order = ["Cashier", "Inventory Manager", "Customer Help", "Cleaning Staff", "Manager", "Supervisor"]
group_colors = {
    "Cashier": "#ADD8E6",            # Light Blue
    "Inventory Manager": "#90EE90",  # Light Green
    "Customer Help": "#FFFFE0",      # Light Yellow
    "Cleaning Staff": "#FFDAB9",     # Light Peach
    "Manager": "#D3D3D3",            # Light Gray
    "Supervisor": "#FFB6C1"          # Light Pink
}

excel_filename = "shift_assignments_report.xlsx"
with pd.ExcelWriter(excel_filename, engine="xlsxwriter") as writer:
    workbook = writer.book
    worksheet = workbook.add_worksheet("Report")
    
    # Write the header in row 0.
    header = df_report.columns.tolist()
    for col_num, col_name in enumerate(header):
        worksheet.write(0, col_num, col_name)
    
    current_row = 1
    # Write rows group by group.
    for group in group_order:
        group_df = df_report[df_report["Position"] == group]
        if not group_df.empty:
            if current_row > 1:
                current_row += 1  # Insert a blank row between groups.
            fmt = workbook.add_format({"bg_color": group_colors[group]})
            for _, row in group_df.iterrows():
                for col_num, value in enumerate(row):
                    worksheet.write(current_row, col_num, value, fmt)
                current_row += 1

print(f"Shift assignment completed. Excel workbook generated: {excel_filename}")
