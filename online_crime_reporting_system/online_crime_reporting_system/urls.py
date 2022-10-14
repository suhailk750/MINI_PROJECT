"""online_crime_reporting_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('complaint/',include('complaint.url')),
    url('criminal_list/',include('criminal_list.url')),
    url('emergency_number/',include('emergency_number.url')),
    url('login/',include('login.url')),
    url('missing_person/',include('missing_person.url')),
    url('police_registration/',include('police_registration.url')),
    url('user_registration/',include('user_registration.url')),
    url('temp/',include('temp.url')),
]
