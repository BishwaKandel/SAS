from django.urls import path
from .views import swap_view

urlpatterns = [
    path('', swap_view, name='swap'),
]
