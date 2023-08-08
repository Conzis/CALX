from django.http.response import HttpResponseRedirect
from django.shortcuts import render,reverse
from app_foods.models import Food
from app_general.forms import BMRform

def about(request):
    return render(request, 'app_general/about.html')

latest_x = None  # Store the latest input data

def home(request):
    calculated_bmr_values = []  # List to store calculated BMR values
    
    if latest_x:
        calculated_bmr = calculate_BMR(latest_x)
        calculated_bmr_values.append({'index': "Latest Input", 'bmr': calculated_bmr})

    return render(request, 'app_general/home.html', {'calculated_bmr_values': calculated_bmr_values})

def Bmr(request):
    global latest_x

    if request.method == 'POST':
        form = BMRform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            x = {
                'gender': data['gender'],
                'weight': data['weight'],
                'height': data['high'],
                'age': data['age']
            }

            latest_x = x  # Update the latest input data
            return HttpResponseRedirect(reverse('home'))
    else:
        form = BMRform()

    context = {'form': form}
    return render(request, 'app_general/homeBMR.html', context)

def calculate_BMR(x):
    if x['gender'] == 'male':
        calculated_bmr = 66 + (13.7 * x['weight']) + (5 * x['height']) - (6.8 * x['age'])
    else:
        calculated_bmr = 655 + (9.6 * x['weight']) + (1.8 * x['height']) - (4.7 * x['age'])

    return calculated_bmr




