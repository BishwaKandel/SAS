"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from login.views import *
from configure.views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register', RegisterView.as_view()),
    path('api/auth/login', LoginView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),
    path('configure/', configure_view),
    # path('employees/', EmployeesView.as_view({'get': 'list'})),
    path('api/employees/', EmployeesListAPIView.as_view()),
    path('api/employees/<int:pk>/', EmployeesDetailAPIView.as_view()),
    path('sendmail/', include('mail.urls')),

]
