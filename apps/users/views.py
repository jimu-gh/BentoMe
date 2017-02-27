from django.shortcuts import render

from .forms import RegisterForm
# Create your views here.
def index(request):
    return render(request, 'users/templates/index.html', {
        'register': RegisterForm()
    })

def register(request):
    pass

def login(request):
    pass
