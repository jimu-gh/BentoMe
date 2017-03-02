from django.shortcuts import render
from ..home.models import *

from .forms import *
# Create your views here.
def index(request):
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
