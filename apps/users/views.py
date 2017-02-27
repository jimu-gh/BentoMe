from django.shortcuts import render

from .forms import RegisterForm
# Create your views here.
def index(request):
    return render(request, 'users/index.html', {
        'register': RegisterForm()
    })
