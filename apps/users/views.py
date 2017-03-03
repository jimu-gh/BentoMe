from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm

from .models import *
from ..home.models import *

import stripe, datetime
# Create your views here.
def index(request):
    print User.objects.all()
    if 'user' in request.session:
        return redirect(reverse('home:dashboard'))

    context = {
        'register': RegisterForm(),
        'login': LoginForm()
    }

    return render(request, 'users/templates/index.html', context)

def register(request):
    user = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():

            print form.cleaned_data['stripe_token']

            customer = stripe.Customer.create(
                description = form.cleaned_data['email'],
                email = form.cleaned_data['email'],
                card = form.cleaned_data['stripe_token'],
            )

            user = User(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                student = form.cleaned_data['student'],
                last_4_digits = form.cleaned_data['last_4_digits'],
                stripe_id = customer.id
            )
            user.set_password(form.cleaned_data['password1'])

            try:
                user.save()
            except IntegrityError:
                form.addError(user.email + ' is already a member')
            else:
                request.session['user'] = {
                    'id': user.id,
                    'first_name': user.first_name
                }
                return redirect(reverse('home:dashboard'))
        for error in form.errors:
            messages.error(request, form.errors[error])

        return redirect(reverse('users:index'))

def login(request):
    if request.method == "POST":
        response = User.objects.login(request.POST)
        if type(response) is list:
            for error in response:
                messages.error(request, error)
            return redirect(reverse('users:index'))
        else:
            request.session['user'] = {
                'id': response.id,
                'first_name': response.first_name
            }
            return redirect(reverse('home:dashboard'))

def logout(request):
    print "test"
    if 'user' in request.session:
        request.session.pop('user')
    return redirect(reverse('home:index'))

def show(request, user_id):
    if 'user' not in request.session:
        return redirect(reverse('users:index'))
    if int(request.session['user']['id']) != int(user_id):
        messages.error(request, "Cannot access another user's information")
        print int(request.session['user']['id']) ==  int(user_id)
        return redirect(reverse('home:dashboard'))

    today = datetime.datetime.now().date()

    user_orders = Meal.objects.filter(meal_orders__user__id=user_id)

    context = {
        'user': User.objects.get(id=user_id),
        'current_orders': user_orders.filter(live_date__lte=today),
        'past_orders': [{'meal': meal, 'rating': meal.meal_ratings.filter(user__id=user_id)} for meal in user_orders]
    }

    return render(request, 'users/templates/show.html', context)

def edit_card(request):
    if 'user' not in request.session:
        return redirect(reverse('users:index'))

    if request.method == "POST":
        customer = User.objects.get(id=request.session['user']['id'])

        customer.card = request.POST['stripe_token']

        customer.save()

        return redirect(reverse('home:dashboard'))
