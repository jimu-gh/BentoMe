from django.shortcuts import render, redirect
from ..home.models import *

from .forms import *
from ..users.models import *
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    context={
    'message' : Message.objects.all(),
    'meals' : Meal.objects.all()
    }
    return render(request, 'adminbento/index.html')

def dish(request):
    return render(request, 'adminbento/adddish.html')

def add(request):
    pass

def dummy(request):
    return render(request, 'adminbento/dummy.html',
    {
        'meal_form': MealForm(),
        'dish_form': DishForm()
    })
    ##refrence the model creation once method is determined
    return redirect(reverse('bentoadmin:dish'))

def menu(request):
    context={
    'main_dish' : Main_Dish.objects.all(),
    'side_dish' : Side_Dish.objects.all()
    }
    return render(request, 'adminbento/menu.html', context)
