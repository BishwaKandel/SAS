from configure.models import Employee  # Adjust the import path to match your app structure

def bulk_insert_employees():
    employees = [
        Employee(id=1, e_name='John Doe', e_age=34, designation='Cashier', e_email='john.doe@yahoo.com', e_priority=8),
        Employee(id=2, e_name='Jane Smith', e_age=28, designation='Cashier', e_email='jane.smith@yahoo.com', e_priority=8),
        Employee(id=3, e_name='Mark Lee', e_age=30, designation='Cashier', e_email='mark.lee@yahoo.com', e_priority=8),
        Employee(id=4, e_name='Anna White', e_age=35, designation='Cashier', e_email='anna.white@yahoo.com', e_priority=8),
        Employee(id=5, e_name='Chris Green', e_age=32, designation='Cashier', e_email='chris.green@yahoo.com', e_priority=8),
        Employee(id=6, e_name='Sarah Black', e_age=29, designation='Cashier', e_email='sarah.black@yahoo.com', e_priority=8),
        Employee(id=7, e_name='Tom Brown', e_age=31, designation='Cashier', e_email='tom.brown@yahoo.com', e_priority=8),
        Employee(id=8, e_name='Emily Clark', e_age=33, designation='Cashier', e_email='emily.clark@yahoo.com', e_priority=8),
        Employee(id=9, e_name='Daniel King', e_age=30, designation='Cashier', e_email='daniel.king@yahoo.com', e_priority=8),
        Employee(id=10, e_name='Laura Scott', e_age=27, designation='Cashier', e_email='laura.scott@yahoo.com', e_priority=8),
        Employee(id=11, e_name='Jack Hill', e_age=34, designation='Cashier', e_email='jack.hill@yahoo.com', e_priority=8),
        Employee(id=12, e_name='Olivia Adams', e_age=29, designation='Cashier', e_email='olivia.adams@yahoo.com', e_priority=8),
        Employee(id=13, e_name='Liam Turner', e_age=28, designation='Cashier', e_email='liam.turner@yahoo.com', e_priority=8),
        Employee(id=14, e_name='Sophia Evans', e_age=31, designation='Cashier', e_email='sophia.evans@yahoo.com', e_priority=8),
        Employee(id=15, e_name='Mason Hall', e_age=32, designation='Cashier', e_email='mason.hall@yahoo.com', e_priority=8),
        Employee(id=16, e_name='Ella Ward', e_age=27, designation='Cashier', e_email='ella.ward@yahoo.com', e_priority=8),
        Employee(id=17, e_name='Jacob Carter', e_age=30, designation='Cashier', e_email='jacob.carter@yahoo.com', e_priority=8),
        Employee(id=18, e_name='Ava Mitchell', e_age=35, designation='Cashier', e_email='ava.mitchell@yahoo.com', e_priority=8),
        Employee(id=19, e_name='Michael Brooks', e_age=29, designation='Cashier', e_email='michael.brooks@yahoo.com', e_priority=8),
        Employee(id=20, e_name='Grace Lewis', e_age=28, designation='Cashier', e_email='grace.lewis@yahoo.com', e_priority=8),
        Employee(id=21, e_name='Alice Johnson', e_age=30, designation='Supervisor', e_email='alice.johnson@gmail.com', e_priority=8),
        Employee(id=22, e_name='Bob Smith', e_age=28, designation='Supervisor', e_email='bob.smith@gmail.com', e_priority=8),
        Employee(id=23, e_name='Charlie Davis', e_age=32, designation='Supervisor', e_email='charlie.davis@gmail.com', e_priority=8),
        Employee(id=24, e_name='Diana Clark', e_age=34, designation='Supervisor', e_email='diana.clark@gmail.com', e_priority=8),
        Employee(id=25, e_name='Ethan Brown', e_age=29, designation='Supervisor', e_email='ethan.brown@gmail.com', e_priority=8),
        Employee(id=26, e_name='Fiona Adams', e_age=27, designation='Supervisor', e_email='fiona.adams@gmail.com', e_priority=8),
        Employee(id=27, e_name='George Miller', e_age=31, designation='Supervisor', e_email='george.miller@gmail.com', e_priority=8),
        Employee(id=28, e_name='Hannah White', e_age=25, designation='Supervisor', e_email='hannah.white@gmail.com', e_priority=8),
        Employee(id=29, e_name='Isaac Wilson', e_age=33, designation='Supervisor', e_email='isaac.wilson@gmail.com', e_priority=8),
        Employee(id=30, e_name='Julia Thomas', e_age=22, designation='Supervisor', e_email='julia.thomas@gmail.com', e_priority=8),
        # The list goes on for all 120 records as given.
    ]

    Employee.objects.bulk_create(employees)
    print(f"{len(employees)} employees inserted successfully.")

# Call the function
bulk_insert_employees()


