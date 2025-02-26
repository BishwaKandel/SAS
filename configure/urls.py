from django.urls import path, include
from .views import *


# urlpatterns = [
#     path('config/', configure_view, name='configure'),
#     path('employees/', EmployeesView.as_view({'get': 'list'}), name='employees_list'),
# ]



urlpatterns = [
    path('api/employees/', EmployeesListAPIView.as_view(), name='employee_list'),  # List & Create
    path('api/employees/<int:pk>/', EmployeesDetailAPIView.as_view(), name='employee_detail'),  # Retrieve, Update, Delete
]
