from django.urls import path
from .views import HRManagerAPI

urlpatterns = [
    path('login/', HRManagerAPI.as_view(), name='login_api'),
]
