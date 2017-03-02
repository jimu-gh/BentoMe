from django.shortcuts import render, redirect
from ..home.models import *
from .forms import *
from ..users.models import *
from django.core.urlresolvers import reverse
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
            return redirect(reverse('admin:dashboard'))

def logout(request):
    if 'user' in request.session:
        request.session.pop('user')
    return redirect(reverse('admin:index'))

def dashboard(request):
    context={
    'message' : Message.objects.all(),
    'meals' : Meal.objects.all()
    }
    return render(request, 'adminbento/dashboard.html')

def dish(request):
    return render(request, 'adminbento/adddish.html')

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
    return redirect(reverse('bentoadmin:dish'))

def menu(request):
    context={
    'main_dish' : Main_Dish.objects.all(),
    'side_dish' : Side_Dish.objects.all(),
    }
    return render(request, 'adminbento/menu.html', context)
