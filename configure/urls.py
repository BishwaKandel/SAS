from django.urls import path
from .views import configure_view

urlpatterns = [
    path('', configure_view, name='configure'),
]
