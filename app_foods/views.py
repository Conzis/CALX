from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Food
from app_general.views import calculate_BMR

def foods(request):
    all_foods = Food.objects.order_by('-cal')
    context = { 'foods': all_foods }
    return render(request, 'app_foods/foods.html', context)

def food(request, food_id):
    one_food = Food.objects.get(id=food_id)
    context = { 'food' : one_food}
    return render(request, 'app_foods/food.html', context)

def ranfood(request):
    foodid = Food.objects.all()
    context = {'foodid' : foodid}
    return render(request, 'app_foods/ranfood.html', context,)

def BMRshow(request):
    mybmr = calculate_BMR
    context = {'mybmr' : mybmr}
    return render(request, 'app_foods/ranfood.html', context,)

