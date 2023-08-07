from django.urls import path
from . import views
from django.urls import reverse_lazy
from .models import Food

idfood = Food.id;
url = reverse_lazy('ranfood', kwargs={'food_id': idfood})

urlpatterns = [
    path('', views.foods, name='foods'),
    path('<int:food_id>', views.food, name='food'),
    path('ranfood', views.ranfood, name='ranfood') 
]