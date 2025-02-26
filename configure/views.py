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
from .models import Employees
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView  


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










# List all employees and create a new one
class EmployeesListAPIView(APIView):
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, or delete a single employee
class EmployeesDetailAPIView(APIView):
    def get_employee(self, pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            return None  # We will handle the response inside each method

    def get(self, request, pk):
        employee = self.get_employee(pk)
        if not employee:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeesSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_employee(pk)
        if not employee:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # serializer = EmployeesSerializer(employee, data=request.data)
        # if serializer.is_valid():
        updated_data = {}

        # Check for each field in the request and add it to updated_data if it's provided
        if 'e_id' in request.data:
            updated_data['e_id'] = request.data['e_id']  # Update name if provided

        if 'e_name' in request.data:
            updated_data['e_name'] = request.data['e_name']  # Update name if provided
        
        if 'no_of_hours_worked' in request.data:
            updated_data['no_of_hours_worked'] = request.data['no_of_hours_worked']  # Update no_of_hours_worked if provided
        
        if 'designation' in request.data:
            updated_data['designation'] = request.data['designation']  # Update designation if provided

        if 'e_gmail' in request.data:
            updated_data['e_gmail'] = request.data['e_gmail']  # Update e_gmail if provided

        if 'e_priority' in request.data:
            updated_data['e_priority'] = request.data['e_priority']  # Update priority if provided

        
          # Fields to be updated based on the frontend request
        # fields_to_update = {
        #     'e_id': request.data.get('e_id'),
        #     'e_name': request.data.get('e_name'),
        #     'no_of_hours_worked': request.data.get('no_of_hours_worked'),
        #     'designation': request.data.get('designation'),
        #     'e_gmail': request.data.get('e_gmail'),
        #     'e_priority': request.data.get('e_priority'),
            
        # }


        # Update the employee object with new values for the modified fields
        for field, value in updated_data.items():
            setattr(employee, field, value)
            employee.save()
            serializer = EmployeesSerializer(employee)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_employee(pk)
        if not employee:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

