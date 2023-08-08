from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from app_BMR.forms import BMRform
from .models import BMR


# Create your views here.
def Bmr(request):
    if request.method =='POST':
        form = BMRform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_BMR = BMR()
            new_BMR.gender = data['gender']
            new_BMR.weight = data['weight']
            new_BMR.high = data['high']
            new_BMR.age = data['age']
            new_BMR.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = BMRform()
    form = BMRform()
    context = {'form' : form}
    return render(request, 'app_BMR/homeBMR.html', context)

def calculateBMR(request):
    realBMR = BMR.objects.all()
    context = {'realBMR': realBMR}
    return context

def calculateBMR(request):
    realBMR = BMR.objects.all()
    
    for bmr in realBMR:
        if bmr.gender == 'ชาย': 
            bmr.calculated_bmr = 66 + (13.7 * bmr.weight) + (5 * bmr.high) - (6.8 * bmr.age)
        else:
            bmr.calculated_bmr = 655 + (9.6 * bmr.weight) + (1.8 * bmr.high) - (4.7 * bmr.age)
        bmr.save()
    context = {'realBMR': realBMR}
    return context