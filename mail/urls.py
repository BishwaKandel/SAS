from django.urls import path, include
from .views import *

urlpatterns = [
    path('', SendEmailView.as_view(), name='send_email'),
]
