from django.shortcuts import render
from ..home.models import
# Create your views here.
def index(request):
    return render(request, 'admin/index.html')

def dish(request):
    return render(request, 'admin/adddish.html')
