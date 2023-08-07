from django.http.response import HttpResponse
from django.shortcuts import render
from app_foods.models import Food
from app_BMR.views import calculateBMR as calculate_BMR_from_app_BMR

# Create your views here.


def home(request):
    calculate_bmr_data = calculate_BMR_from_app_BMR(request)
    realBMR = calculate_bmr_data.get('realBMR', [])
    print(realBMR) 
    return render(request, 'app_general/home.html', {'realBMR': realBMR})

def about(request):
    return render(request, 'app_general/about.html')




