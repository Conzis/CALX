from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bmr, name="BMR")
]