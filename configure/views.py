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
from .models import Employee
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView  
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ShiftAssignmentSerializer
from configure.models import Employee 
from swap.models import ShiftSchedule, Shift
from utils.opt2 import assign_shifts, iterate, export_schedule_to_excel, MAX_WORKING_HOURS, MAX_SHIFTS_PER_DAY
import os
from django.conf import settings
import pandas as pd

@api_view(['POST'])
def assign_shifts_api(request):
    serializer = ShiftAssignmentSerializer(data=request.data)

    if serializer.is_valid():
        designation_counts = serializer.validated_data['designation_counts']

        employee = list(Employee.objects.all().values())
        employee_by_designation = iterate(employee)

        # ✅ Fetch shifts directly from Shift model (not ShiftSchedule)
        shifts_dict = {}
        shift_objects = Shift.objects.all()

        for shift in shift_objects:
            shifts_dict.setdefault(shift.day, []).append({
                "shift_id": shift.shift_id,
                "shift_duration": shift.shift_duration,
                "shift_timing": shift.shift_timing
            })

        # ✅ Assign shifts based on fetched Shift objects
        schedule = assign_shifts(shifts_dict, employee_by_designation, designation_counts, MAX_WORKING_HOURS, MAX_SHIFTS_PER_DAY)

        # ✅ Save schedule as Excel & CSV
        excel_file = os.path.join(settings.MEDIA_ROOT, "Updated_Schedule.xlsx")
        csv_file = os.path.join(settings.MEDIA_ROOT, "Updated_Schedule.csv")

        export_schedule_to_excel(schedule, employee, excel_file)

        df = pd.read_excel(excel_file)
        df.to_csv(csv_file, index=False)

        return JsonResponse({
            "message": "Shift assignment successful",
            "schedule_file": excel_file,
            "csv_file": csv_file
        }, status=200)

    return JsonResponse({"error": serializer.errors}, status=400)







# List all employees and create a new one
class EmployeeListAPIView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation Errors:", serializer.errors)  # Print errors to console
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, or delete a single employee
class EmployeeDetailAPIView(APIView):
    def get_employee(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None  # We will handle the response inside each method

    def get(self, request, pk):
        employee = self.get_employee(pk)
        if not employee:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_employee(pk)
        if not employee:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # serializer = EmployeeSerializer(employee, data=request.data)
        # if serializer.is_valid():
        updated_data = {}

       
          # Fields to be updated based on the frontend request
        fields_to_update = {
            'e_id': request.data.get('e_id'),
            'e_name': request.data.get('e_name'),
            'no_of_hours_worked': request.data.get('no_of_hours_worked'),
            'designation': request.data.get('designation'),
            'e_gmail': request.data.get('e_gmail'),
            'e_priority': request.data.get('e_priority'),
            
        }


        # Update the employee object with new values for the modified fields
        for field, value in fields_to_update.items():
            if value is not None:  # Ensuring only provided fields are updated
               setattr(employee, field, value)

    # Save the updated employee object after modifying all required fields
        employee.save()

    # Serialize and return the updated employee object
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        employee = self.get_employee(pk)
        if not employee:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

