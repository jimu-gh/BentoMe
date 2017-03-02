from django.shortcuts import render, redirect
from ..home.models import *
# Create your views here.
def index(request):
    return render(request, 'admin/index.html')

def dish(request):
    return render(request, 'admin/adddish.html')

def add(request):
    ##refrence the model creation once method is determined
    return redirect ('/dish')

def menu(request):
    context={
    'main_dish' : main_dish.objects.all(),
    'side_dish' : side_dish.objects.all()
    }
    return render(request, 'admin/menu.html', context)
