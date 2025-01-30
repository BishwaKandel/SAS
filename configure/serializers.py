from restframework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['e_id', 'e_name', 'no_of_hours_worked', 'designation', 'e_gmail', 'e_priority']