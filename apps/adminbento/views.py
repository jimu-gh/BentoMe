from django.shortcuts import render
from ..home.models import *
# Create your views here.
def index(request):
    return render(request, 'adminbento/index.html')

def dish(request):
    return render(request, 'adminbento/adddish.html')

def add(request):
    pass
