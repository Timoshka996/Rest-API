from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'Car'
urlpatterns = [
    path('car/create/', CreateCarView.as_view()),
    path('car/list/', ListCarView.as_view())
]