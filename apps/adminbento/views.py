from django.shortcuts import render, redirect
from ..home.models import *
from .forms import *
from ..users.models import *
from django.core.urlresolvers import reverse
from django.db.models import Count
import datetime
from django.contrib import messages
from ..users.forms import RegisterForm, LoginForm
# Create your views here.
def index(request):
    if 'admin' in request.session:
        return redirect(reverse('adminbento:dashboard'))
    context = { 'login': LoginForm()}
    return render(request, 'adminbento/index.html', context)

def login(request):
    if request.method == "POST":
        response = User.objects.login(request.POST)
        print 'login path hit'
        if type(response) is list:
            for errors in response:
                messages.error(request, errors)
            return redirect(reverse('adminbento:index'))
        elif User.objects.get(id=response.id).admin == True:
            print response.admin
            request.session['user'] = {
                'id': response.id,
                'first_name': response.first_name,
                'admin' : True
            }
            return redirect(reverse('adminbento:dashboard'))
<<<<<<< HEAD
        else:
            return redirect(reverse('users:index'))
=======
>>>>>>> c883324d4af25811f3dfd31fbbddf7312148b618

def logout(request):
    if 'user' in request.session:
        request.session.pop('user')
    return redirect(reverse('adminbento:index'))

def dashboard(request):
    print 'dashboard route hit'
    print request.session['user']['admin']
    if  'admin' in request.session['user']:
        print 'admin detected'
        context={
        'message' : Message.objects.all(),
        'meals' :Meal.objects.annotate(num_sold=Count('meal_orders')).filter(live_date__lt=datetime.date.today()),
        }
        return render(request, 'adminbento/dashboard.html', context)
    else:
        print 'admin not detected'
        return redirect(reverse('adminbento:index'))
def dish(request):
<<<<<<< HEAD
    if  'admin' in request.session['user']:
        return render(request, 'adminbento/adddish.html',
        {
            'meal_form': MealForm(),
            'dish_form': DishForm(),
            'ingredient_form': IngredientForm()
        })
        ##refrence the model creation once method is determined
        return redirect(reverse('adminbento:dish'))
    else:
        print 'admin not detected'
        return redirect(reverse('adminbento:index'))
=======
    return render(request, 'adminbento/adddish.html',
    {
        'meal_form': MealForm(),
        'dish_form': DishForm(),
        'ingredient_form': IngredientForm()
    })
    ##refrence the model creation once method is determined
    return redirect(reverse('adminbento:dish'))
>>>>>>> c883324d4af25811f3dfd31fbbddf7312148b618

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
    if  'admin' in request.session['user']:
        context={
        'main_dish' : Main_Dish.objects.all(),
        'side_dish' : Side_Dish.objects.all(),
        }
        return render(request, 'adminbento/menu.html', context)
    else:
        print 'admin not detected'
        return redirect(reverse('adminbento:index'))

def logout(request):
    print "test"
    if 'user' in request.session:
        request.session.pop('user')
    return redirect(reverse('home:index'))
