from django.urls import path
from .views import *

urlpatterns = [
    path('config/', configure_view, name='configure'),
    path('employees/', EmployeesView.as_view({'get': 'list'}), name='employees_list'),
]
