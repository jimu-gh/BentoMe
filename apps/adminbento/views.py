from django.shortcuts import render, redirect
from ..home.models import *
from .forms import *
from ..users.models import *
from django.core.urlresolvers import reverse
from django.db.models import Count
import datetime
# Create your views here.
def index(request):
    return render(request, 'adminbento/index.html')

def login(request):
    if request.method == "POST":
        response = User.objects.login(request.POST)
        if type(response) is list:
            for errors in response:
                messages.error(request, error)
            return redirect(reverse('users:index'))
        else:
            request.session['user'] = {
                'id': response.id,
                'first_name': response.first_name
            }
            return redirect(reverse('adminbento:dashboard'))

def logout(request):
    if 'user' in request.session:
        request.session.pop('user')
    return redirect(reverse('adminbento:index'))

def dashboard(request):
    context={
    'message' : Message.objects.all(),
    'meals' :Meal.objects.annotate(num_sold=Count('meal_orders')).filter(live_date__lt=datetime.date.today()),
    }
    return render(request, 'adminbento/dashboard.html', context)

def dish(request):
    return render(request, 'adminbento/adddish.html',
    {
        'meal_form': MealForm(),
        'dish_form': DishForm(),
        'ingredient_form': IngredientForm()
    })
    ##refrence the model creation once method is determined
    return redirect(reverse('adminbento:dish'))

def add(request):
    if request.method == "POST":
        print request.POST
        print request.POST.getlist('ingredients')
    return

def dummy(request):
    return render(request, 'adminbento/dummy.html',
    {
        'meal_form': MealForm(),
        'dish_form': DishForm(),
        'ingredient_form': IngredientForm()
    })
    ##refrence the model creation once method is determined
    return redirect(reverse('adminbento:dish'))

def menu(request):
    context={
    'main_dish' : Main_Dish.objects.all(),
    'side_dish' : Side_Dish.objects.all(),
    }
    return render(request, 'adminbento/menu.html', context)
