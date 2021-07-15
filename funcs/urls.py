from django.contrib import admin
from django.urls import path, include

from funcs import views
# from funcs.views import load_file
from funcs.views import validate_date, check_date

urlpatterns = [
    path('', views.home, name='home'),
    path('check_date/', check_date, name="check_date"),
]
